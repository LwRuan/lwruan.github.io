---
title: "Blog Setup Day2"
categories: "jekyll"
tags: 
date: 2020-08-30
---

## Image and Math Support

One can easily import image in `Markdown` using `![image name](image path)`, another way of doing this is to use `html` syntax:
```html
<div align="center"><img src="pic/image.png" alt="Image" style="zoom:%;" /></div>
```
In this way you can change the position and size of the image. From official guide, it's recommanded to store all the images in `asssets/images/`, and also name the image like your post:`YY-MM-DD-title.jpg`.(html style of image is not originally supported in jekyll, so you might need some trick to set the right path for image)

To add math support the most common choice is [mathjax](https://www.mathjax.org/). Just add these lines to the `default.html` layout before `<head>`:
```html
<script type="text/x-mathjax-config">
     MathJax.Hub.Config({
         tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
     });
 </script>
 <script type="text/javascript" async
   src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
```
The config here means you can use `$...$` or `\\(...\\)` for inline math because `$...$` is not naturally support by `mathjax`.

## Custom Page Style

To change some of the default style like fonts, colors, margins one needs to modify some of the settings in `layout` and `css`. For me, I don't like the footer to show up in every page, so I go to `_includes/footer.html` and comment everything in it, then the footer disappear. I also don't like the title links have grey color, so I go to `_sass/minimal-mistakes/_variables.scss` to change the `link-color` in it. Here I won't explain every configuration's position to you, but show how I find them.

Basically every style configuration start from `_layouts`, every layout file might include components in `_includes`, the file in `_includes` tells what to show in every components, and the style of the components are in `_sass`. If you want to change someting, first you can use the consoler of your web browser (F12 for chrome and firefox) to find the name of the component you want to modify, then search through files in those folders using `grep -R` to locate the variables you want. One thing to notice is that most colors and fonts are defined in `_sass/minimal-mistakes/_variables.scss`.

## Drafts

Jekyll provide draft function to write post. Put the draft post in `_drafts`, then use `bundle exec jekyll serve --draft`, the posts in `_drafts` will be shown using the day time you run the command.
