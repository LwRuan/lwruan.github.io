<script setup lang="ts">
</script>
  
<template>
  <div class="max-w-300 mx-auto">
    <div>
      <img src="/pubs-static/3DBoatWater2000013.jpg" class="w-full h-100 object-cover overflow-hidden rounded">
    </div>
    <div class="text-center text-3xl pt-10">
      Solid-Fluid Interaction with Surface-Tension-Dominant Contact
    </div>
    <div class="text-center">
      <div class="inline font-bold">
        Liangwang Ruan*
      </div>
      , Jinyuan Liu*, Bo Zhu, Shinjiro Sueda, Bin Wang, Baoquan Chen (* for joint first authors), August 2021 In
      SIGGRAPH
    </div>
    <div class="flex flex-row">
      <div class="flex-grow"></div>
      <a href="/pubs-static/waterstrider.pdf" download class="text-3xl">
        <div class="i-carbon-document-pdf text-blue-500" />
      </a>
      <a href="https://www.youtube.com/watch?v=3ejKNbtdfnY" class="text-3xl ml-3 mr-1">
        <div class="i-carbon-logo-youtube text-blue-500" />
      </a>
      <a href="/pubs-static/waterstrider-slides.pdf" download class="text-3xl mx-2">
        <div class="i-uil-presentation text-blue-500" />
      </a>
      <div class="flex-grow"></div>
    </div>
    <div class="pt-10">
      We propose a novel three-way coupling method to model the contact interaction between solid and fluid driven by
      strong surface tension. At the heart of our physical model is a thin liquid membrane that simultaneously couples
      to both the liquid volume and the rigid objects, facilitating accurate momentum transfer, collision processing,
      and surface tension calculation. This model is implemented numerically under a hybrid Eulerian-Lagrangian
      framework where the membrane is modelled as a simplicial mesh and the liquid volume is simulated on a background
      Cartesian grid. We devise a monolithic solver to solve the interactions among the three systems of liquid, solid,
      and membrane. We demonstrate the efficacy of our method through an array of rigid-fluid contact simulations
      dominated by strong surface tension, which enables the faithful modeling of a host of new surface-tension-dominant
      phenomena includings: objects with higher density than water that remains afloat; 'Cheerios effect' where floating
      objects attract one another; and surface tension weakening effect caused by surface-active constituents.
    </div>
    <div class="pt-10">
      <iframe src="//player.bilibili.com/player.html?aid=972946493&bvid=BV18p4y14761&cid=335033830&page=1"
        scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" class="md:mx-auto w-full md:w-160 aspect-video rounded">
      </iframe>
    </div>
    <div class="mt-10 pl-4 mx-auto bg-light-300 dark:bg-dark-100 rounded">
      @article{Ruan2021,<br />
      author = {Ruan, Liangwang and Liu, Jinyuan and Zhu, Bo and Sueda, Shinjiro and Wang, Bin and Chen, Baoquan},<br />
      title = {Solid-Fluid Interaction with Surface-Tension-Dominant Contact},<br />
      year = {2021},<br />
      issue_date = {August 2021},<br />
      publisher = {Association for Computing Machinery},<br />
      address = {New York, NY, USA},<br />
      volume = {40},<br />
      number = {4},<br />
      issn = {0730-0301},<br />
      url = {https://doi.org/10.1145/3450626.3459862},<br />
      doi = {10.1145/3450626.3459862},<br />
      journal = {ACM Trans. Graph.},<br />
      month = {jul},<br />
      articleno = {120},<br />
      numpages = {12},<br />
      }
    </div>
  </div>
</template>
  
<route lang="yaml">
meta:
  layout: home
</route>
  