---
layout: page
title: Staff
nav_order: 3
has_children: false
has_toc: false
description: A listing of all the course staff members.
released: true
---

## Instructors

<div class="role">
{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}
</div>

## TAs

<div class="role">
{% assign teaching_assistants = site.staffers | where: 'role', 'ta' %}
{% assign num_teaching_assistants = teaching_assistants | size %}
{% if num_teaching_assistants != 0 %}

{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}

{% assign teaching_assistants = site.staffers | where: 'role', 'tutor' %}
{% assign num_teaching_assistants = teaching_assistants | size %}
{% if num_teaching_assistants != 0 %}
</div>

## Tutors

<div class="role">
{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}
</div>
