<script setup lang="ts">
</script>

<template>
  <div class="mx-auto max-w-300">
    <!-- intro -->
    <div class="flex flex-col place-content-center md:flex-row">
      <img src="/avatar-small.jpg" class="mx-auto my-auto h-58 w-58 rounded-lg md:mx-0 md:mr-4">
      <div class="mt-4 flex-grow p-4 text-left md:mt-0">
        <div class="pb-5 text-center text-4xl md:text-left">
          Liangwang Ruan 阮良旺
        </div>
        <div class="text-xl">
          I'm currently a fourth-year Ph.D student from School of Computer Science, Peking University, advised by <a href="http://cfcs.pku.edu.cn/baoquan/" class="underline">Prof. Baoquan Chen</a>. I also got my Bachelor's degree in Computer Science from Peking University in 2021. I'm interested in developing new simulation techniques for all kinds of nature phenomena including fluids, solids, clothes and their interactions.
        </div>
        <!-- <div class="text-xl">
          {{t('author.intro1')}}
          <a href="http://cfcs.pku.edu.cn/baoquan/" class="underline">{{t('author.adviser')}}</a>
          {{t('author.intro2')}}
        </div> -->
        <div class="pt-2 text-xl">
          <div i-carbon-email class="align-middle" /> <div class="inline underline">
            ruanliangwang@pku.edu.cn
          </div>
          <a href="/resume.pdf" download class="ml-4">
            <div i-carbon-document class="align-middle" />
            <div class="inline underline">Resume </div>
          </a>
          <a href="https://rlw1999.github.io" class="ml-4">
            <div i-carbon-blog class="align-middle" />
            <div class="inline underline">Blog </div>
          </a>
        </div>
      </div>
    </div>

    <!-- news -->
    <!-- <div class="pt-10 text-3xl text-center">
      {{t('section.news')}}
    </div>
    <ul class="pt-10 list-disc pl-10 text-xl">
      <li>
        Our new paper is demonstrated in the <a href="https://www.youtube.com/watch?v=D6EznsTblj8" class="underline">Technical Papers Trailer</a> <div i-uil-grin/> [November, 2022]

      </li>
      <li>
        Our new paper on surface tension in PBD is officially accepted by SIGGRAPH Asia! [September 18, 2022]
      </li>
      <li>
        I attend the on-site GAMES seminar in Hunan, great experience! XD
        <RouterLink class="text-xl text-blue-500" to="/blogs/2022-08-15-games">
          <div i-uil-letter-chinese-a></div>
        </RouterLink>
        [August 12, 2022]
      </li>
    </ul> -->

    <!-- pubs -->
    <div class="pt-10 text-center text-3xl">
      Publications
    </div>
    <div class="flex flex-col place-content-center pt-10">
      <div class="flex flex-row py-6">
        <div class="my-auto w-58 flex-grow md:flex-grow-0">
          <RouterLink to="/pubs/minnie">
            <img src="/pubs-static/torus.gif" alt="" class="w-full rounded-lg">
          </RouterLink>
        </div>
        <div class="hidden w-0 pl-4 md:block md:flex-grow">
          <RouterLink to="/pubs/minnie" class="text-2xl">
            MiNNIE: a Mixed Multigrid Method for Real-time Simulation of Nonlinear Near-Incompressible Elastics
          </RouterLink>
          <div class="text-xl">
            <div class="inline font-bold">
              Liangwang Ruan
            </div>
            , Bin Wang, Tiantian Liu, Baoquan Chen, December 2024 In SIGGRAPH Asia
          </div>
          <div class="flex flex-row pt-2">
            <a href="/pubs-static/minnie.pdf" download class="text-xl">
              <div class="i-carbon-document-pdf text-blue-500" />
            </a>
            <a href="https://github.com/LwRuan/MiNNIE" download class="ml-3 mr-1 text-xl">
              <div class="i-carbon-logo-github text-blue-500" />
            </a>
            <a href="https://www.bilibili.com/video/BV1xZS4YXE65" class="ml-3 mr-1 text-xl">
              <div class="i-carbon-logo-youtube text-blue-500" />
            </a>
          </div>
        </div>
      </div>
      <div class="flex flex-row py-6">
        <div class="my-auto w-58 flex-grow md:flex-grow-0">
          <RouterLink to="/pubs/vortex-bubble">
            <img src="/pubs-static/half-bubble.jpg" alt="" class="w-full rounded-lg">
          </RouterLink>
        </div>
        <div class="hidden w-0 pl-4 md:block md:flex-grow">
          <RouterLink to="/pubs/vortex-bubble" class="text-2xl">
            A Vortex Particle-on-Mesh Method for Soap Film Simulation
          </RouterLink>
          <div class="text-xl">
            Ningxiao Tao,
            <div class="inline font-bold">
              Liangwang Ruan
            </div>
            , Yitong Deng, Bo Zhu, Bin Wang, Baoquan Chen, August 2024 In SIGGRAPH
          </div>
          <div class="flex flex-row pt-2">
            <a href="/pubs-static/vortex-bubble.pdf" download class="text-xl">
              <div class="i-carbon-document-pdf text-blue-500" />
            </a>
            <a href="https://www.bilibili.com/video/BV1Mm421G7g7" class="ml-3 mr-1 text-xl">
              <div class="i-carbon-logo-youtube text-blue-500" />
            </a>
          </div>
        </div>
      </div>
      <!-- pbd-st -->
      <div class="flex flex-row py-6">
        <div class="my-auto w-58 flex-grow md:flex-grow-0">
          <RouterLink to="/pubs/pbd-st">
            <img src="/pubs-static/pbd-st-small.gif" alt="" class="w-full rounded-lg">
          </RouterLink>
        </div>
        <div class="hidden w-0 pl-4 md:block md:flex-grow">
          <RouterLink to="/pubs/pbd-st" class="text-2xl">
            Position-based Surface Tension Flow
          </RouterLink>
          <div class="text-xl">
            Jingrui Xing*,
            <div class="inline font-bold">
              Liangwang Ruan*
            </div>
            , Bin Wang, Bo Zhu, Baoquan Chen (* for joint first authors), November 2022 In SIGGRAPH Asia
          </div>
          <div class="flex flex-row pt-2">
            <a href="/pubs-static/pbd-st.pdf" download class="text-xl">
              <div class="i-carbon-document-pdf text-blue-500" />
            </a>
            <a href="https://www.bilibili.com/video/BV1414y1H734" class="ml-3 mr-1 text-xl">
              <div class="i-carbon-logo-youtube text-blue-500" />
            </a>
          </div>
        </div>
      </div>
      <!-- waterstrider -->
      <div class="flex flex-row py-6">
        <div class="my-auto w-58 flex-grow md:flex-grow-0">
          <RouterLink to="/pubs/waterstrider">
            <img src="/pubs-static/boat_leaf.gif" alt="" class="w-full rounded-lg">
          </RouterLink>
        </div>
        <div class="hidden w-0 pl-4 md:block md:flex-grow">
          <RouterLink to="/pubs/waterstrider" class="text-2xl">
            Solid-Fluid Interaction with Surface-Tension-Dominant Contact
          </RouterLink>
          <div class="text-xl">
            <div class="inline font-bold">
              Liangwang Ruan*
            </div>
            , Jinyuan Liu*, Bo Zhu, Shinjiro Sueda, Bin Wang, Baoquan Chen (* for joint first authors), August 2021 In SIGGRAPH
          </div>
          <div class="flex flex-row pt-2">
            <a href="/pubs-static/waterstrider.pdf" download class="text-xl">
              <div class="i-carbon-document-pdf text-blue-500" />
            </a>
            <a href="https://www.youtube.com/watch?v=3ejKNbtdfnY" class="ml-3 mr-1 text-xl">
              <div class="i-carbon-logo-youtube text-blue-500" />
            </a>
            <a href="/pubs-static/waterstrider-slides.pdf" download class="mx-2 text-xl">
              <div class="i-uil-presentation text-blue-500" />
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- <div>
    <div text-4xl>
      <div i-carbon-campsite inline-block />
    </div>
    <p>
      <a rel="noreferrer" href="https://github.com/antfu/vitesse" download>
        Vitesse
      </a>
    </p>
    <p>
      <em text-sm opacity-75>{{ t('intro.desc') }}</em>
    </p>

    <div py-4 />

    <input
      id="input"
      v-model="name"
      :placeholder="t('intro.whats-your-name')"
      :aria-label="t('intro.whats-your-name')"
      type="text"
      autocomplete="false"
      p="x4 y2"
      w="250px"
      text="center"
      bg="transparent"
      border="~ rounded gray-200 dark:gray-700"
      outline="none active:none"
      @keydown.enter="go"
    >
    <label class="hidden" for="input">{{ t('intro.whats-your-name') }}</label>

    <div>
      <button
        btn m-3 text-sm
        :disabled="!name"
        @click="go"
      >
        {{ t('button.go') }}
      </button>
    </div>
  </div> -->
</template>

<route lang="yaml">
meta:
  layout: home
</route>
