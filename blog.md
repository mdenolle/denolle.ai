---
layout: default
title: Agents for Academic Practice
permalink: /blog/
---
<section class="section">
  <div class="container prose">
    <h1>Agents for Academic Practice</h1>
    <p>Field notes from an active researcher integrating generative AI into teaching, proposals, code, and mentoring — documenting what works, what fails, and what I haven't resolved.</p>
    <p><strong>Posting format:</strong> each post is a single markdown page, and can include a link to the public GitHub repository containing skills/instructions files.</p>
    <p><strong>Community note:</strong> to comment, open a post and click <em>Discuss this post →</em>. Discussions happen on GitHub to keep the conversation open, searchable, and collegial.</p>

    {% assign agent_posts = site.posts | where: "series", "agents-for-academic-practice" %}

    {% if agent_posts.size > 0 %}
    <ul class="post-list">
      {% for post in agent_posts %}
        <li>
          <article>
            <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
            <p class="post-meta">{{ post.date | date: "%B %-d, %Y" }}</p>
            {% if post.excerpt %}
              <p>{{ post.excerpt | strip_html }}</p>
            {% endif %}
            {% if post.repo_url and post.repo_url != "" %}
              <p><a href="{{ post.repo_url }}" target="_blank" rel="noopener noreferrer">Related GitHub repository</a></p>
            {% endif %}
            {% if post.skills_url and post.skills_url != "" %}
              <p><a href="{{ post.skills_url }}" target="_blank" rel="noopener noreferrer">Skills / instructions files</a></p>
            {% endif %}
          </article>
        </li>
      {% endfor %}
    </ul>
    {% else %}
      <p>No posts in this series yet. Add a markdown file in <code>_posts/</code> with <code>series: agents-for-academic-practice</code> in front matter to publish here.</p>
    {% endif %}
  </div>
</section>
