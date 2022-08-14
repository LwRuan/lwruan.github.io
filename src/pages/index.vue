<script setup lang="ts">
const user = useUserStore()
const name = $ref(user.savedName)

const router = useRouter()
const go = () => {
  if (name)
    router.push(`/hi/${encodeURIComponent(name)}`)
}

const { t } = useI18n()
</script>

<template>
  <div class="max-w-300 mx-auto">
    <!-- intro -->
    <div class="flex flex-col md:flex-row place-content-center">
      <img src="avatar.jpg" class="w-56 h-56 rounded-lg mx-auto my-auto md:mx-0 md:mr-4">
      <div class="flex-grow p-4 mt-4 md:mt-0 text-left">
        <div class="text-4xl text-center pb-5 md:text-left">
          {{t('author.name')}}
        </div>
        <div class="text-xl">
          {{t('author.intro1')}}
          <a href="http://cfcs.pku.edu.cn/baoquan/" class="underline">{{t('author.adviser')}}</a>
          {{t('author.intro2')}}
        </div>
      </div>
    </div>

    <!-- pubs -->
    <div class="pt-10 flex flex-col place-content-center">
      <div>

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
