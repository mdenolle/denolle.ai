# Marine Denolle - GitHub Pages Site

Minimal, fast, accessible Jekyll site for Marine Denolle.

## Stack
- Jekyll (theme-free, no remote theme)
- Single stylesheet: `assets/styles.css`
- Markdown blog posts in `_posts/`

## Repository structure
- `_config.yml`: site config + centralized outbound links
- `_layouts/default.html`: base semantic layout/navigation/footer
- `index.html`: landing page
- `contact.md`: contact page (`/contact/`)
- `blog.md`: blog index (`/blog/`)
- `_posts/*.md`: blog posts
- `assets/styles.css`: responsive, accessible styles

## Deploy on GitHub Pages (main branch, /root)
1. Push this repository to GitHub.
2. In GitHub, open **Settings -> Pages**.
3. Under **Build and deployment**:
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/ (root)`
4. Save. GitHub Pages will build and publish automatically.

## Local development (optional)
If you want to preview locally:

```bash
bundle install
bundle exec jekyll serve
```

Open `http://127.0.0.1:4000`.

## Edit content guide
### Update key links and profile in one place
Edit `_config.yml`:
- `site_profile.portrait_url` – homepage hero portrait image URL (supports external URLs like GitHub avatars)
- `site_profile.cv_pdf_url` – direct link to your CV PDF (displays in top-nav and `/cv/`)
- `site_profile.cv_repo_url` – GitHub repository URL for your CV source
- `project_links.*` – project/button URLs on homepage
- `social_links.*` – footer/contact links
- `media.featured_video.*` – featured video title and links for Media section
- `media.posts` – list of talks/media links for Media section

### Update landing page copy
Edit `index.html`.

### Add a blog post
Create a new file in `_posts/` named:
`YYYY-MM-DD-title.md`

#### Agents for Academic Practice series
To post in the main "Agents for Academic Practice" blog series, use this front matter:

```md
---
layout: default
title: "Your Post Title"
series: agents-for-academic-practice
repo_url: "https://github.com/username/repo-for-this-post"
skills_url: ""
---
Your post content here.
```

**Required fields:**
- `layout: default`
- `title: "..."`
- `series: agents-for-academic-practice` (to appear on `/blog/`)

**Optional fields:**
- `repo_url: "..."` – link to GitHub repository with related skills/instructions
- `skills_url: "..."` – direct link to skills/instructions file

Posts with this series tag will automatically appear on `/blog/` with optional links rendered below each post.

### Add GitHub Discussions to your blog posts
Readers can discuss each post directly on GitHub Discussions, with an optional giscus comment thread embedded in the post.

#### Setup steps

**1. Enable Discussions in your GitHub repository**
- Open your repository Settings
- Scroll to "Discussions" and enable it
- (Optional) Configure title and description for your discussion categories

**2. Find your Discussion Category ID**
To auto-create discussions for posts, you need the numeric category ID. Get it via GitHub GraphQL Explorer:

1. Go to [GitHub GraphQL Explorer](https://docs.github.com/en/graphql/overview/explorer)
2. Sign in with your GitHub account
3. Paste this query, replacing `YOUR_REPO_OWNER` and `YOUR_REPO_NAME`:
    ```graphql
    query {
       repository(owner: "YOUR_REPO_OWNER", name: "YOUR_REPO_NAME") {
          discussionCategories(first: 10) {
             nodes {
                id
                name
             }
          }
       }
    }
    ```
4. Click the play button. Copy the `id` of the category you want (e.g., "Blog Discussions" or similar).

**3. Set your GitHub token**
The automation script needs a GitHub Personal Access Token to create discussions on your behalf.

1. Go to [GitHub Settings → Personal Access Tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Give it a name like "Discussion Auto-Create"
4. Check scopes: `repo`, `discussions`
5. Generate and copy the token
6. Save it as an environment variable: `export GH_TOKEN=ghp_xxxxxxxxxxxx`

**4. Auto-create a discussion for a post**
Once your post is created with the frontmatter above, run:

```bash
export GH_TOKEN=your_token_here
python scripts/create_discussion.py _posts/YYYY-MM-DD-title.md
```

The script will:
- Read your post frontmatter
- Create a discussion on GitHub with the post title
- Update your post file with the discussion URL in the frontmatter
- Print success or error messages

**Example output:**
```
✓ Repository: marinedenolle/denolle.ai
✓ Discussion created: https://github.com/marinedenolle/denolle.ai/discussions/42
✓ Updated _posts/2026-02-26-welcome.md with discussion URL
```

#### Enable optional giscus comment embed (advanced)
By default, posts link to GitHub Discussions but don't embed comments. To add a giscus-powered comment thread in each post:

1. Find your repository ID via GraphQL:
    ```graphql
    query {
       repository(owner: "YOUR_REPO_OWNER", name: "YOUR_REPO_NAME") {
          id
       }
    }
    ```
    Copy the ID (e.g., `R_kgDOLN4fFg`).

2. Find your Discussion Category ID (from step 2 above, e.g., `DIC_kwDOLN4fFg4CiPzp`).

3. Edit `_config.yml` and uncomment/fill in the giscus section:
    ```yaml
    giscus:
       enabled: true
       repo: "YOUR_REPO_OWNER/YOUR_REPO_NAME"
       repo_id: "R_kgDOLN4fFg"  # from GraphQL
       category: "Blog Discussions"
       category_id: "DIC_kwDOLN4fFg4CiPzp"  # from GraphQL
       mapping: "pathname"
       theme: "light"
    ```

4. Rebuild your site. New posts will now show a giscus comment thread below the discussion link.

#### Troubleshooting

**Scripts fails: "GH_TOKEN not found"**
- Run: `export GH_TOKEN=your_token_here` before running the script

**Script fails: "Discussions not enabled"**
- Enable Discussions in your repository Settings (see step 1 above)

**Script fails: "Post file not found"**
- Check the file path; it should be relative to the repository root (e.g., `_posts/2026-02-26-welcome.md`)

**Script fails: "Category not found"**
- Verify category ID in _config.yml (or use GraphQL Explorer to get the right ID)

**Discussion link appears but comment thread doesn't show**
- Check that `giscus.enabled: true` in `_config.yml`
- Verify `giscus.repo` and `giscus.repo_id` are correct
- Rebuild the site

### Update styling
Edit `assets/styles.css`.
