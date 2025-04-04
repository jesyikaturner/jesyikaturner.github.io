---
title: Portfolio
subtitle: 
description: 
featured_image: 
---

### Client-work

Select pieces from freelance jobs:

- Mecha Card Game
- Aura of Worlds
- Three in a Rogue

<div class="gallery" data-columns="3">

{% for file in site.static_files %}
  {% if file.path contains '/images/portfolio/client-work' %}

  <img src="{{file.path}}" />
    
  {% endif %}
{% endfor %}

</div>

### Pixel Art

<div class="gallery" data-columns="3">

{% for file in site.static_files %}
  {% if file.path contains '/images/portfolio/pixel-art' %}

  <img src="{{file.path}}" width="500">
    
  {% endif %}
{% endfor %}

</div>

### Digital Art

<div class="gallery" data-columns="3">

{% for file in site.static_files %}
  {% if file.path contains '/images/portfolio/digital-art' %}

  <img src="{{file.path}}" width="500">
    
  {% endif %}
{% endfor %}

</div>

### Traditional

<div class="gallery" data-columns="3">

{% for file in site.static_files %}
  {% if file.path contains '/images/portfolio/traditional' %}

  <img src="{{file.path}}" width="500">
    
  {% endif %}
{% endfor %}

</div>


