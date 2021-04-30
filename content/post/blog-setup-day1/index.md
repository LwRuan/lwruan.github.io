---
title: Blog Setup Day1
subtitle: Set up my personal website using Jekyll

# Summary for listings and search engines
summary: Set up my personal website using Jekyll

# Link this post with a project
projects: []

# Date published
date: "2020-08-29T00:00:00Z"

# Date updated
lastmod: "2020-08-29T00:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  #caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/CpkOjOcXdUY)'
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- admin

tags:
- Jekyll

categories:
- Website
---

## Basic Tools

I use [jekyll](https://jekyllrb.com) and github page to setup my blog, there are many online tutorials on how to build this thing up already, but you may come cross some detail problems as I do. The basic steps are like this:

* install `ruby`, `bundler` and `jekyll`
* create a github page repository \<user name\>.github.io
* fork a theme repository's master branch, here I use [minimal-mistakes](https://github.com/mmistakes/minimal-mistakes) and copy everything to your github repository (or use theme repository as template when create your github repository)
* run `bundle install`

The first problem is that you need to config `Gemfile` before you can see your web page, notice that you should config this in `remote theme` way. Then the second error may occur that [the version of `github-pages` is not compatible with the latest version of `jekyll`](https://github.com/github/pages-gem/issues/577). I solve these problems by config my `Gemfile` in the following way.

```
source "https://rubygems.org"
  
gem "jekyll", "~> 3.8.7"
# gem "minimal-mistakes-jekyll"
gem "github-pages", "~> 206", group: :jekyll_plugins
  
gem "wdm", "~> 0.1.0" if Gem.win_platform?

group :jekyll_plugins do
   gem "jekyll-include-cache"
   gem "faraday", "~> 0.17.3"
   gem "jekyll-feed", "~> 0.13.0"
end

```
Now you can see your web page by running `bundle exec jekyll serve`, and also see the remote site after `git push`.

## How Jekyll Generate Page

The master branch of `minimal-mistakes` is quite empty, but it's a good start point. First you should look through `_config.yml`, this is the main configuration file we need to edit. The [Step by Step Tutorial](https://jekyllrb.com/docs/step-by-step/01-setup/) is a good document to understand what's going on. Basically the content of web page can be written in `markdown` or `html`, the format of the page is specified by `Front Matter`:
```
---
title: "FooBar"
layout: default
categories: 
---
```
Jekyll can read from this metadata and compile the final web page. All the layout files are in `_layouts` directory, like `default.html`, open it you can see it's `html` with some `jekyll` syntax. 
The best example of this pipeline is `index.html` in home directory:
```
---
layout: home
author_profile: true
---
```
`home` means it uses `home.html` in `_layouts` as template, `author_profile: true` means it includes your profile in home page.

Now let's write our first post. create a `_posts` directory, add a markdown file in this format(required by jekyll)`YY-MM-DD-title.md` in it, write front matter and your content, reopen the server you should see your post in the home page, if you change the layout to any layout in `_layouts`, you should also see the change.

It's not a good idea to specify layout in every post, so `jekyll` provides a default configuration for different files in `_config.yml`. Go to this file and scroll down you can see config like this:
```
defaults:
  # _posts
  - scope:
      path: ""
      type: posts
    values:
      layout: single
      author_profile: true
      read_time: true
      comments: true
      share: true
      related: true
```
The config here means all the files in `_posts` will add these `values` in its front matter, so actually you can just write `title` and `author` in every post, `jekyll` will automatically generate page using `single` layout. If you want to do something different, you can also add `layout:` in front matter, it will override the settings in `_config.yml`.

## How Jekyll Organize Pages

Most of the time besides writting posts, we also want a page to display all the posts in different categories, this requires us to write an `archive` page. Pages like archive, curriculum are different from post, they don't need to update so much. We can put them just in home directory like `index.html`, I prefer to put them in `_pages`. To do so, we need to include `_pages` in `_config.yml` (already included in `minimal-mistakes`). 

Apart from that, we may also want to navigate through these pages in title bar, this configuration is stored in `_data/navigation.yml`:
```
main:
    - title: "Quick-Start Guide"
      url: https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide      /

```
This config is also straight forward, the problem is how jekyll determine the url for pages.

It turns out jekyll uses `permalink` to config page's position. Suppose you add `curriculum.md` in `_pages` like this:
```
---
title: "Curriculum"
permalink: /curriculum/
layout: single
---

Something about yourself.
```
then this page will show up in `\<user name\>.github.io/curriculum`, to link this url to title bar, you can just change the `url`'s value in `navigation.yml` to `/curriculum/`.

For all the posts, jekyll also provide default settings for them. In `_config.yml`, there is a line for `permalink`. If it's `/:categories/:title.html`, it means the post you write will be stored in `\<user name\>.github.io/\<post's categority\>/title.html`, you can see [this document](https://jekyllrb.com/docs/permalinks/) for more information on how to change this.