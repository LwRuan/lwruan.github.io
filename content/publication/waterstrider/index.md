---
title: "Solid-Fluid Interaction with Surface-Tension-Dominant Contact"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Jinyuan Liu
- Bo Zhu
- Shinjiro Sueda
- Bin Wang
- Baoquan Chen

# Author notes (optional)
author_notes:
- "Equal contribution"
- "Equal contribution"
-
-
- "Corresponding Authors"
- "Corresponding Authors"


date: "2021-08-01T00:00:00Z"
doi: "10.1145/3450626.3459862"

# Schedule page publish date (NOT publication's date).
publishDate: "2021-04-30T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *ACM Transactions on Graphics(Proceedings of SIGGRAPH 2021)*
publication_short: In *SIGGRAPH*

abstract: "We propose a novel three-way coupling method to model the contact interaction between solid and fluid driven by strong surface tension. At the heart of
our physical model is a thin liquid membrane that simultaneously couples to
both the liquid volume and the rigid objects, facilitating accurate momentum
transfer, collision processing, and surface tension calculation. This model is
implemented numerically under a hybrid Eulerian-Lagrangian framework
where the membrane is modelled as a simplicial mesh and the liquid volume is simulated on a background Cartesian grid. We devise a monolithic
solver to solve the interactions among the three systems of liquid, solid, and
membrane. We demonstrate the efficacy of our method through an array of
rigid-fluid contact simulations dominated by strong surface tension, which
enables the faithful modeling of a host of new surface-tension-dominant
phenomena includings: objects with higher density than water that remains
afloat; ‘Cheerios effect’ where floating objects attract one another; and surface tension weakening effect caused by surface-active constituents."

# Summary. An optional shortened abstract.
summary: We propose a novel three-way coupling framework to simulate the surface-tension-dominant contact between rigid and fluid, which uses a Lagrangian surface membrane to handle the interactions between solids and fluid.

tags: [Simulation]

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: "www.youtube.com/watch?v=3ejKNbtdfnY"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  #caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
#projects:
#- example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
#slides: example
---
