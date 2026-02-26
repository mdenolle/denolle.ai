---
layout: default
title: Blog
permalink: /blog/
---
<section class="section">
  <div class="container prose">
    <h1>Blog</h1>
    <p>Short updates on research, field deployments, and AI-enabled Earth systems methods.</p>
    <ul class="post-list">
      {% for post in site.posts %}
        <li>
          <article>
            <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
            <p class="post-meta">{{ post.date | date: "%B %-d, %Y" }}</p>
            {% if post.excerpt %}
              <p>{{ post.excerpt | strip_html }}</p>
            {% endif %}
          </article>
        </li>
      {% endfor %}
    </ul>
  </div>
</section>
