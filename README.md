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
### Update key links in one place
Edit `_config.yml`:
- `project_links.*` for project/button URLs
- `social_links.*` for footer/contact links

### Update landing page copy
Edit `index.html`.

### Add a blog post
Create a new file in `_posts/` named:
`YYYY-MM-DD-title.md`

Example front matter:

```md
---
layout: default
title: "Post Title"
---
Your content here.
```

### Update styling
Edit `assets/styles.css`.
