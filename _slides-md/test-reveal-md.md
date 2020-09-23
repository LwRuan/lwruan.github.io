---
author: Liangwang Ruan
title: Demo Slide
date: 2020/9/21
---

# First Slides

some introduction

## Verticle?

go down

## Incremental lists

::: incremental

* Hello
* Another
* $F=ma$

:::

## Wait

just wait for a moment

. . .

Surprise!

::: notes

This is my note.

- It can contain Markdown
- like this list

:::

# Columns

:::::: {.columns}
::: {.column width="40%"}

```markdown
:::: {.columns}
::: {.column width="40%"}
contents...
:::
::: {.column width="60%"}
contents...
:::
::::
```

:::
::: {.column width="60%"}
contents...
:::
::::::

# Code

:::::: {.columns}
::: {.column}

```ruby
#!/usr/bin/ruby
require 'find'

puts "Generate all slides"
Find.find('_slides-md') do |path|
    if path != '_slides-md'
        output_path = path.sub("_slides-md/", "_slides/").sub(".md", ".html")
        puts "source file: " + path
        puts "output file: " + output_path
        system "pandoc -t revealjs -s -o " + output_path + " " + path + 
        " -V revealjs-url=/assets/reveal.js --slide-level 2 -V theme=white"
    end
end

puts "Start server"
exec "bundle exec jekyll serve --draft"
```

:::
::: {.column}

![](/assets/images/Woman-with-a-Parasol.jpg){height="400px"}

:::
::::::

# test image
![image test](/assets/images/Woman-with-a-Parasol.jpg)

# test equation

$$G_{\mu\nu}=8\pi T_{\mu\nu}$$