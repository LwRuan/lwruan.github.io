#!/usr/bin/ruby
require 'find'

puts "Generate all slides"
Find.find('_slides-md') do |path|
    if path != '_slides-md'
        output_path = path.sub("_slides-md/", "_slides/").sub(".md", ".html")
        puts "source file: " + path
        puts "output file: " + output_path
        system "pandoc -t revealjs -s -o " + output_path + " " + path + 
        " -V revealjs-url=/assets/reveal.js --mathjax --slide-level 2 -V theme=white -V touch=false"
    end
end

puts "Start server"
exec "bundle exec jekyll serve --draft"
