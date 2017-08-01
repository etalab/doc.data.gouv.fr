---
title: {{ title }}
date: {{ date.strftime('%Y-%m-%d %H:%M') }}
modified: {{ date.strftime('%Y-%m-%d %H:%M') }}
image: https://placehold.it/1920x1080
tags:{% for tag in tags %}
  - {{ tag|trim }}
  {%- endfor %}
slug: {{ slug }}
name: {{ name }}
lang: {{ lang }}
{% if category -%}
category: {{ category }}
{% endif -%}
authors: Axel Haustant
summary: {{ summary }}
{% if is_article -%}
status: draft
{% endif -%}
---
