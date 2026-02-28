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
discussion:
   url: "https://github.com/YOUR_REPO_OWNER/YOUR_REPO_NAME/discussions/123"
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
- `discussion.url: "..."` – direct link to the GitHub Discussion for this post

Posts with this series tag will automatically appear on `/blog/` with optional links rendered below each post.

### Add GitHub Discussions to your blog posts
Readers discuss each post on GitHub Discussions.

#### Setup steps

**1. Enable Discussions in your GitHub repository**
- Open your repository Settings
- Scroll to "Discussions" and enable it
- (Optional) Configure title and description for your discussion categories

**2. Create a discussion manually for the post**
- In your repository, open the **Discussions** tab
- Click **New discussion**
- Use a title matching your blog post title (or close variation)
- Publish the discussion and copy its URL

**3. Link the discussion in post front matter**
Add this to the post front matter:

```yaml
discussion:
  url: "https://github.com/YOUR_REPO_OWNER/YOUR_REPO_NAME/discussions/123"
```

Once saved, the post will automatically show a **Discuss this post →** link and a discussion section.

#### Publish checklist (recommended)
For each new blog post:
1. Publish the markdown post in `_posts/`
2. Create the matching GitHub Discussion
3. Paste the discussion link into `discussion.url`
4. Run `bundle exec jekyll build` to verify the site build

#### Troubleshooting

**Discussion link does not appear in the post**
- Check that front matter includes `discussion.url`
- Check indentation under `discussion:` (two spaces before `url`)

**GitHub discussion not found / 404**
- Verify the copied URL is correct and public to your readers

**Discussions tab is missing in your repository**
- Enable Discussions in your repository Settings (see step 1 above)

### Update styling
Edit `assets/styles.css`.
