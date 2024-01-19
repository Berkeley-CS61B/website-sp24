---
title: Home
layout: page
nav_order: 0
hide_title: true
released: true
---

{%- if site.outdated -%}

<p class="warning">
This site is outdated! For the latest content, please visit the <a href="https://fa23.datastructur.es/">Fall 2023 website</a>
</p>
{%- endif -%}

{%- if site.under_construction -%}

<p class="warning">
This site is under construction. All dates and policies are tentative until this message goes away.
</p>
{%- endif -%}

<img align="right" alt="CS61Bee" width="150px" src="assets/images/bee.png">

# {{ site.title }}

<!-- ## Announcements

{{ site.announcements.last }} -->

<!-- [Past announcements](announcements.md){: .btn .btn-outline .fs-3 } -->

**Instructors:** Justin Yokota, Peyrin Kao / **Lecture:** 1-2PM MWF, Dwinelle 155, [Zoom]({{ site.links.lecture }})

## Weekly Schedule

[Skip to current week](#week-{{ 'now' | date: '%U' }}){: .btn .btn-outline .fs-3 }

<div>
{%- include syllabus.html -%}
</div>
