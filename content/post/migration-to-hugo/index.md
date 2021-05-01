---
title: Migration to Hugo
subtitle: Build a website using [Hugo Academic](https://wowchemy.com)

# Summary for listings and search engines
summary: Build a website using [Hugo Academic](https://wowchemy.com)

# Link this post with a project
projects: []

# Date published
date: "2021-05-01T00:00:00Z"

# Date updated
lastmod: "2021-05-01T00:00:00Z"

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
  preview_only: true

authors:
- admin

tags:
- Hugo

categories:
- Website
---

## Why Hugo?

The main reason I switch to Hugo is that I find many researchers use [Hugo Academic](https://wowchemy.com)(now named as Wowchemy) to build their website rather than Jekyll. After finishing the migration to Hugo, I understand why. Essentially Hugo and Jekyll are both static content generators, but Hugo Academic has more good built-in features like publication pages, project pages, and presentation pages. The configuration for Hugo is also much easier since I don't have to deal with those extensions. Although Hugo might not be as flexible as Jekyll, it can cover most of my demands without great effort. 

## Set Up

Hugo Academic does not work like other Hugo themes, so Hugo's tutorial is not adequate. Wowchemy offers a tutorial on its website, but it's based on its online platform using Netlify. To keep things simple, the best way to build a website is to directly clone their Github repository [starter-academic](https://github.com/wowchemy/starter-academic) and put it in your `<user-name>.github.io` repository. To preview the website, go to the repository's folder and run `hugo server`. Running `hugo` can generate the website under the `public` folder, this behavior can be changed using `--publishDir`.  

I use a [Github Action](https://github.com/features/actions) to publish my website following the instruction from [Hugo Tutorial](https://gohugo.io/hosting-and-deployment/hosting-on-github/). Whenever I commit to `master` branch, the action can be automatically triggered, running commands to publish the website to `gh-pages` branch. The action's configuration file is in `.github/workflows/gh-pages.yml`:
```yml
name: github pages

on:
  push:
    branches:
      - master  # Set a branch to deploy

jobs:
  deploy:
    runs-on: ubuntu-18.04
    steps:
      - uses: actions/checkout@v2
        with:
          submodules: true  # Fetch Hugo themes (true OR recursive)
          fetch-depth: 0    # Fetch all history for .GitInfo and .Lastmod

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: '0.82.1'
          extended: true

      - name: Build
        run: hugo --minify

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_branch: gh-pages
          cname: lwruan.com
```
This workflow use [actions-hugo](https://github.com/peaceiris/actions-hugo) and [actions-gh-pages](https://github.com/peaceiris/actions-gh-pages) from [Shohei Ueda](https://github.com/peaceiris), it does nothing more than using Hugo to generate the website, push the files to `gh-pages` branch, and add `CNAME` file in the directory. This process only takes few seconds, after that the files in `gh-pages` branch are updated. The last thing is to tell Github to find the `index.html` in `gh-pages` branch, this can be done in repository's settings.