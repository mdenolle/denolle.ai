#!/usr/bin/env python3
"""
Create a GitHub Discussion for a blog post and update its frontmatter.

Usage:
    python scripts/create_discussion.py path/to/_posts/YYYY-MM-DD-title.md

Environment variables:
    GH_TOKEN: GitHub personal access token (required)

Requirements:
    - GitHub Discussions enabled in repository
    - Category "Blog Discussions" exists (or custom category ID in frontmatter)
    - GH_TOKEN env var set with appropriate scopes
"""

import os
import sys
import re
import json
import subprocess
from pathlib import Path
from urllib.parse import urlparse


def get_repo_info():
    """Extract owner/repo from remote origin."""
    try:
        result = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            capture_output=True,
            text=True,
            check=True,
        )
        url = result.stdout.strip()
        # Handle both HTTPS and SSH URLs
        if url.startswith("git@"):
            # git@github.com:owner/repo.git
            match = re.search(r"github\.com[:/](.+?)/(.+?)(?:\.git)?$", url)
            if match:
                return match.group(1), match.group(2)
        else:
            # https://github.com/owner/repo.git
            match = re.search(r"github\.com/(.+?)/(.+?)(?:\.git)?$", url)
            if match:
                return match.group(1), match.group(2)
    except subprocess.CalledProcessError:
        pass
    return None, None


def read_post_frontmatter(file_path):
    """Parse YAML frontmatter from markdown file."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract frontmatter between --- markers
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        raise ValueError("No frontmatter found in post file")

    frontmatter_str = match.group(1)
    body_start = match.end()
    body = content[body_start:]

    return frontmatter_str, body, content[: match.start()]


def parse_yaml_simple(yaml_str):
    """Simple YAML parser for basic key: value pairs (no complex nesting)."""
    data = {}
    lines = yaml_str.strip().split("\n")
    for line in lines:
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            data[key.strip()] = val.strip().strip('"\'')
    return data


def get_category_id_from_repo(owner, repo, gh_token, category_name="Blog Discussions"):
    """Fetch the category ID for Discussions in the repo."""
    query = """
    query {
      repository(owner: "%s", name: "%s") {
        discussionCategories(first: 100) {
          edges {
            node {
              id
              name
            }
          }
        }
      }
    }
    """ % (
        owner,
        repo,
    )

    result = _graphql_request(gh_token, query)
    if "errors" in result:
        raise Exception(f"GitHub API error: {result['errors']}")

    categories = result.get("data", {}).get("repository", {}).get("discussionCategories", {}).get("edges", [])
    for edge in categories:
        if edge["node"]["name"] == category_name:
            return edge["node"]["id"]

    raise Exception(
        f'Category "{category_name}" not found. Available categories: '
        + ", ".join(e["node"]["name"] for e in categories)
    )


def create_discussion(owner, repo, gh_token, title, category_id, body_text=""):
    """Create a GitHub Discussion via GraphQL API."""
    mutation = """
    mutation {
      createDiscussion(input: {
        repositoryId: "%s"
        categoryId: "%s"
        title: "%s"
        body: "%s"
      }) {
        discussion {
          url
        }
      }
    }
    """ % (
        owner,
        repo,
        title.replace('"', '\\"'),
        (body_text or "").replace('"', '\\"').replace("\n", "\\n")[:500],  # Limit to 500 chars
    )

    # Get repo node ID first
    query = """
    query {
      repository(owner: "%s", name: "%s") {
        id
      }
    }
    """ % (
        owner,
        repo,
    )

    repo_result = _graphql_request(gh_token, query)
    if "errors" in repo_result:
        raise Exception(f"GitHub API error fetching repo: {repo_result['errors']}")

    repo_id = repo_result["data"]["repository"]["id"]

    # Now create the discussion with the correct repo ID
    mutation = """
    mutation {
      createDiscussion(input: {
        repositoryId: "%s"
        categoryId: "%s"
        title: "%s"
        body: "%s"
      }) {
        discussion {
          url
        }
      }
    }
    """ % (
        repo_id,
        category_id,
        title.replace('"', '\\"'),
        (body_text or "").replace('"', '\\"').replace("\n", "\\n")[:500],
    )

    result = _graphql_request(gh_token, mutation)
    if "errors" in result:
        raise Exception(f"GitHub API error creating discussion: {result['errors']}")

    return result["data"]["createDiscussion"]["discussion"]["url"]


def _graphql_request(gh_token, query):
    """Execute a GraphQL request to GitHub API."""
    headers = {
        "Authorization": f"Bearer {gh_token}",
        "Content-Type": "application/json",
    }
    payload = json.dumps({"query": query})

    import urllib.request

    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload.encode("utf-8"),
        headers=headers,
        method="POST",
    )

    try:
        with urllib.request.urlopen(request) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        raise Exception(f"GitHub API request failed: {e}")


def update_frontmatter_with_discussion(file_path, discussion_url):
    """Update post frontmatter to include discussion URL."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract frontmatter
    match = re.match(r"^(---\n)(.*?)(\n---\n)", content, re.DOTALL)
    if not match:
        raise ValueError("Could not parse frontmatter")

    fm_start, fm_content, fm_end_marker = match.group(1), match.group(2), match.group(3)
    body = content[match.end() :]

    # Parse existing frontmatter to check if discussion already exists
    lines = fm_content.strip().split("\n")
    new_lines = []
    discussion_added = False

    for line in lines:
        # Skip existing discussion block
        if line.strip().startswith("discussion:") or (
            discussion_added and (line.startswith("  ") or not line.strip())
        ):
            continue
        new_lines.append(line)

    # Add discussion block
    new_fm = "\n".join(new_lines).rstrip() + "\n"
    new_fm += "discussion:\n"
    new_fm += f'  url: "{discussion_url}"\n'
    new_fm += '  category: "Blog Discussions"\n'

    # Reconstruct file
    new_content = fm_start + new_fm + fm_end_marker + body

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✓ Updated {file_path} with discussion URL")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    post_file = Path(sys.argv[1])
    if not post_file.exists():
        print(f"Error: File not found: {post_file}", file=sys.stderr)
        sys.exit(1)

    # Check for GH_TOKEN
    gh_token = os.getenv("GH_TOKEN")
    if not gh_token:
        print("Error: GH_TOKEN environment variable not set", file=sys.stderr)
        print("  Set it with: export GH_TOKEN=your_github_token", file=sys.stderr)
        sys.exit(1)

    # Get repo info
    owner, repo = get_repo_info()
    if not owner or not repo:
        print(
            "Error: Could not determine GitHub repo from git remote origin",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Repository: {owner}/{repo}")

    # Read post
    try:
        fm_str, body, fm_prefix = read_post_frontmatter(post_file)
    except Exception as e:
        print(f"Error reading post: {e}", file=sys.stderr)
        sys.exit(1)

    # Parse frontmatter
    fm_data = parse_yaml_simple(fm_str)
    title = fm_data.get("title", post_file.stem)

    # Check if discussion already exists
    if "discussion:" in fm_str:
        print("Discussion already configured in this post. Skipping.")
        sys.exit(0)

    # Get category ID
    try:
        print("Fetching discussion categories...")
        category_id = get_category_id_from_repo(
            owner, repo, gh_token, "Blog Discussions"
        )
        print(f"✓ Found category ID: {category_id}")
    except Exception as e:
        print(f"Error fetching categories: {e}", file=sys.stderr)
        sys.exit(1)

    # Create discussion
    try:
        print(f"Creating discussion for: {title}")
        discussion_url = create_discussion(
            owner, repo, gh_token, title, category_id, body[:200]
        )
        print(f"✓ Discussion created: {discussion_url}")
    except Exception as e:
        print(f"Error creating discussion: {e}", file=sys.stderr)
        sys.exit(1)

    # Update frontmatter
    try:
        update_frontmatter_with_discussion(post_file, discussion_url)
    except Exception as e:
        print(f"Error updating frontmatter: {e}", file=sys.stderr)
        sys.exit(1)

    print("Done!")


if __name__ == "__main__":
    main()
