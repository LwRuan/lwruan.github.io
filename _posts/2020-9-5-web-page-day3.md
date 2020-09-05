---
title: "Blog Setup Day3"
categories: "jekyll"
tags: 
date: 2020-09-04
---

## Categories

In minimal-mistakes, there is `categories.html` and `category.html` in layout, the difference is `categories.html` is like `posts.html` that lists all the posts but grouped in categories, `category.html` is to show all the posts belongs to one category in one page. For me I would like to create a seperate page for each category so I can add more explainations to it. 

The idea is that I can make every category a summary page in `_categories`, set its `permalink` to `/categories/<category name>`, and its `layout` to `category`. I tried to add a default front matter in `_config.yml` but it didn't work, so I guess I need to manually set every summary page's layout.

The next step should be grouping all the summary pages in one `categories` page and set its link in navigator, but as I said `categories` layout in minimal-mistakes list all the posts but not category pages, so I need to create my custom categories page's layout. I did some research and I found it might not be a easy task, so I simply add this lines in `posts.html` instead:
```html
<!--to avoid ambiguity I change all {} to []-->
[% assign categories_max = 0 %]
[% for category in site.categories %]
  [% if category[1].size > categories_max %]
    [% assign categories_max = category[1].size %]
  [% endif %]
[% endfor %]

<h1 class="page__title"> by Categories </h1>
[% assign entries_layout = page.entries_layout | default: 'list' %]
<ul class="taxonomy__index">
[% for i in (1..categories_max) reversed %]
  [% for category in site.categories %]
    [% if category[1].size == i %]
        <li>
          <a href="/categories/{{ category[0] | slugify }}">
            <strong>{{ category[0] }}</strong> <span class="taxonomy__count">{{ i }}</span>
          </a>
        </li>
    [% endif %]
  [% endfor %]
[% endfor %]
</ul>
<br>
```
Now my `BLOG` page will look like this:  
![screenshot](/assets/images/2020-09-05-screenshot.png)  

Click the `jekyll` category will lead you `categories/jekyll` page, exactlly as I expected. And also one thing need to change is the bottom `category list` at each post's page, click it you will find you go to `categories/#jekyll`, this is not the page we want but the position in minimal-mistakes's `categories` layout. To modify this, go to `_include/category-list.html` and change `[% assign path_type = "#" %]` to `[% assign path_type = "" %]`, this will delete the `#` in relative path.
