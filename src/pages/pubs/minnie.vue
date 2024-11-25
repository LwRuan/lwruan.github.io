<script setup lang="ts">
</script>

<template>
  <div class="mx-auto max-w-300">
    <div>
      <img src="/pubs-static/torus.png" class="h-100 w-full overflow-hidden rounded object-cover">
    </div>
    <div class="pt-10 text-center text-3xl">
      MiNNIE: a Mixed Multigrid Method for Real-time Simulation of Nonlinear Near-Incompressible Elastics
    </div>
    <div class="text-center">
      <div class="inline font-bold">
        Liangwang Ruan
      </div>
      , Bin Wang, Tiantian Liu, Baoquan Chen, December 2024 In SIGGRAPH Asia
    </div>
    <div class="flex flex-row">
      <div class="flex-grow" />
      <a href="/pubs-static/minnie.pdf" download class="mx-2 text-2xl">
        <div class="i-carbon-document-pdf align-middle" />
        <div class="hidden underline md:inline">Paper</div>
      </a>
      <a href="/pubs-static/minnie-sup.pdf" download class="mx-2 text-2xl">
        <div class="i-carbon-document-pdf align-middle" />
        <div class="hidden underline md:inline">Supplemental Material</div>
        <div class="inline text-xl md:hidden">(supp)</div>
      </a>
      <a href="https://github.com/LwRuan/MiNNIE" download class="mx-2 text-2xl">
        <div class="i-carbon-logo-github align-middle" />
        <div class="hidden underline md:inline">Code</div>
      </a>
      <!-- <a href="https://www.youtube.com/watch?v=3ejKNbtdfnY" class="text-3xl ml-3 mr-1">
        <div class="i-carbon-logo-youtube text-blue-500" />
      </a> -->
      <!-- <a href="/pubs-static/waterstrider-slides.pdf" download class="text-3xl mx-2">
        <div class="i-uil-presentation text-blue-500" />
      </a> -->
      <div class="flex-grow" />
    </div>
    <div class="pt-10">
      We propose MiNNIE, a simple yet comprehensive framework for real-time simulation of nonlinear near-incompressible elastics. To avoid the common volumetric locking issues at high Poisson's ratios of linear finite element methods (FEM), we build MiNNIE upon a mixed FEM framework and further incorporate a pressure stabilization term to ensure excellent convergence of multigrid solvers. Our pressure stabilization strategy injects bounded influence on nodal displacement which can be eliminated using a quasi-Newton method. MiNNIE has a specially tailored GPU multigrid solver including a modified skinning-space interpolation scheme, a novel vertex Vanka smoother, and an efficient dense solver using Schur complement. MiNNIE supports various elastic material models and simulates them in real-time, supporting a full range of Poisson's ratios up to 0.5 while handling large deformations, element inversions, and self-collisions at the same time.
      <iframe
        src="//player.bilibili.com/player.html?isOutside=true&aid=113390190202875&bvid=BV1xZS4YXE65&cid=26518816097&p=1"
        scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" class="mt-10 aspect-video w-full rounded md:mx-auto md:w-200"
      />
    </div>
    <div class="mx-auto mt-10 rounded bg-light-300 pl-4 dark:bg-dark-100">
      @article{Ruan2024MiNNIE,<br>
      author = {Ruan, Liangwang and Wang, bin and Liu, Tiantian and Chen, Baoquan},<br>
      title = {MiNNIE: a Mixed Multigrid Method for Real-time Simulation of Nonlinear Near-Incompressible Elastics},<br>
      year = {2024},<br>
      issue_date = {December 2021},<br>
      publisher = {Association for Computing Machinery},<br>
      address = {New York, NY, USA},<br>
      volume = {43},<br>
      number = {6},<br>
      issn = {0730-0301},<br>
      url = {https://doi.org/10.1145/3687758},<br>
      doi = {10.1145/3687758},<br>
      journal = {ACM Trans. Graph.},<br>
      month = {dec},<br>
      articleno = {258},<br>
      numpages = {15},<br>
      }
    </div>
  </div>
</template>

<route lang="yaml">
  meta:
    layout: home
  </route>