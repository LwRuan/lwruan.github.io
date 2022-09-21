<script setup lang="ts">
// const user = useUserStore()
// const name = $ref(user.savedName)

// const router = useRouter()
// const go = () => {
//   if (name)
//     router.push(`/hi/${encodeURIComponent(name)}`)
// }

const { t } = useI18n()
</script>

<template>
  <div class="max-w-300 mx-auto">
    <!-- intro -->
    <div class="flex flex-col md:flex-row place-content-center">
      <img src="/avatar.jpg" class="w-58 h-58 rounded-lg mx-auto my-auto md:mx-0 md:mr-4">
      <div class="flex-grow p-4 mt-4 md:mt-0 text-left">
        <div class="text-4xl text-center pb-5 md:text-left">
          {{t('author.name')}}
        </div>
        <div class="text-xl">
          {{t('author.intro1')}}
          <a href="http://cfcs.pku.edu.cn/baoquan/" class="underline">{{t('author.adviser')}}</a>
          {{t('author.intro2')}}
        </div>
        <div class="text-xl pt-4">
          <div i-carbon-email class="align-middle"/> ruanliangwang@pku.edu.cn
        </div>
      </div>
    </div>

    <!-- news -->
    <div class="pt-10 text-3xl text-center">
      {{t('section.news')}}
    </div>
    <ul class="pt-10 list-disc pl-10 text-xl">
      <li>
        Our new paper on surface tension in PBD is officially accepted by SIGGRAPH Asia! [September 18, 2022]
      </li>
      <li>
        I attend the on-site GAMES seminar in Hunan, great experience!
        <RouterLink class="text-xl text-blue-500" to="/blogs/2022-08-15-games">
          <div i-uil-letter-chinese-a></div>
        </RouterLink> 
        [August 12, 2022]
      </li>
    </ul>

    <!-- pubs -->
    <div class="pt-10 text-3xl text-center">
      {{t('section.pub')}}
    </div>
    <div class="pt-10 flex flex-col place-content-center">
      <div class="flex flex-row">
        <div class="w-58 my-auto flex-grow md:flex-grow-0">
          <RouterLink to="/pubs/pbd-st">
            <img src="/pubs-static/pbd-st-small.gif" alt="" class="w-full rounded-lg">
          </RouterLink>
        </div>
        <div class="pl-4 hidden w-0 md:block md:flex-grow">
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
            TBD
          </div>
        </div>
      </div>
      <!-- waterstrider-->
      <div class="flex flex-row py-6">
        <div class="w-58 my-auto flex-grow md:flex-grow-0">
          <RouterLink to="/pubs/waterstrider">
            <img src="/pubs-static/boat_leaf.gif" alt="" class="w-full rounded-lg">
          </RouterLink>
        </div>
        <div class="pl-4 hidden w-0 md:block md:flex-grow">
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
            <a href="/pubs-static/waterstrider.pdf" class="text-xl">
              <div class="i-carbon-document-pdf text-blue-500"/>
            </a>
            <a href="https://www.youtube.com/watch?v=3ejKNbtdfnY" class="text-xl ml-3 mr-1">
              <div class="i-carbon-logo-youtube text-blue-500"/>
            </a>
            <a href="/pubs-static/waterstrider-slides.pdf" class="text-xl mx-2">
              <div class="i-uil-presentation text-blue-500"/>
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
      <a rel="noreferrer" href="https://github.com/antfu/vitesse" target="_blank">
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
