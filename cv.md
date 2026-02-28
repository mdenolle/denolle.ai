---
layout: default
title: CV
permalink: /cv/
---
<section class="section">
  <div class="container prose">
    <h1>Curriculum Vitae</h1>
    {% if site.site_profile.cv_pdf_url and site.site_profile.cv_pdf_url != "" %}
      <p>
        <a class="btn btn-secondary" href="{{ site.site_profile.cv_pdf_url }}" target="_blank" rel="noopener noreferrer">Open CV in new tab</a>
      </p>
    {% else %}
      <p>CV PDF link is not configured yet.</p>
      {% if site.site_profile.cv_repo_url and site.site_profile.cv_repo_url != "" %}
        <p><a href="{{ site.site_profile.cv_repo_url }}" target="_blank" rel="noopener noreferrer">View CV repository</a></p>
      {% endif %}
    {% endif %}
  </div>
</section>
