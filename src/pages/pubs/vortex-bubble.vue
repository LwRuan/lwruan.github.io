<script setup lang="ts">
</script>
  
<template>
  <div class="max-w-300 mx-auto">
    <div>
      <img src="/pubs-static/half-bubble.jpg" class="w-full h-100 object-cover overflow-hidden rounded">
    </div>
    <div class="text-center text-3xl pt-10">
      A Vortex Particle-on-Mesh Method for Soap Film Simulation
    </div>
    <div class="text-center">
      Ningxiao Tao,
      <div class="inline font-bold">
        Liangwang Ruan
      </div>
      , Yitong Deng, Bo Zhu, Bin Wang, Baoquan Chen, August 2024 In SIGGRAPH
    </div>
    <div class="flex flex-row">
      <div class="flex-grow"></div>
      <a :href="`/pubs-static/vortex-bubble.pdf`" download class="text-3xl">
        <div class="i-carbon-document-pdf text-blue-500" />
      </a>
      <!-- <a href="https://www.bilibili.com/video/BV1414y1H734" class="text-3xl ml-3 mr-1">
        <div class="i-carbon-logo-youtube text-blue-500" />
      </a> -->
      <div class="flex-grow"></div>
    </div>
    <div class="pt-10">
      This paper introduces a novel physically-based vortex fluid model for films,
      aimed at accurately simulating cascading vortical structures on deforming thin films. 
      Central to our approach is a novel mechanism decomposing the
      film's tangential velocity into circulation and dilatation components. These
      components are then evolved using a hybrid particle-mesh method, enabling
      the effective reconstruction of three-dimensional tangential velocities and
      seamlessly integrating surfactant and thickness dynamics into a unified
      framework. By coupling with its normal component and surface-tension
      model, our method is particularly adept at depicting complex interactions
      between in-plane vortices and out-of-plane physical phenomena, such as
      gravity, surfactant dynamics, and solid boundary, leading to highly realistic
      simulations of complex thin-film dynamics, achieving an unprecedented
      level of vortical details and physical realism.
    </div>
    <!-- <div class="pt-10">
      <iframe src="//player.bilibili.com/player.html?aid=775238515&bvid=BV1414y1H734&cid=892459446&page=1"
        scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" class="md:mx-auto w-full md:w-160 aspect-video rounded">
      </iframe>
    </div> -->
    <div class="mt-10 pl-4 mx-auto bg-light-300 dark:bg-dark-100 rounded">
      @article{Tao2024,<br />
      author = {Tao, Ningxiao and Ruan, Liangwang and Deng, Yitong and Zhu, Bo and Wang, Bin and Chen, Baoquan},<br />
      title = {A Vortex Particle-on-Mesh Method for Soap Film Simulation},<br />
      year = {2024},<br />
      issue_date = {Auguest 2024},<br />
      publisher = {Association for Computing Machinery},<br />
      address = {New York, NY, USA},<br />
      volume = {43},<br />
      number = {4},<br />
      url = {https://doi.org/10.1145/3658165},<br />
      doi = {10.1145/3658165},<br />
      journal = {ACM Trans. Graph.},<br />
      month = {aug},<br />
      articleno = {53},<br />
      numpages = {14},<br />
      }
    </div>
  </div>
</template>
  
<route lang="yaml">
meta:
  layout: home
</route>
  