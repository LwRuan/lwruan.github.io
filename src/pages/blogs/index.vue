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
  <div>
    <div class="text-4xl">
      {{t('button.blogs')}}
    </div>
    <div class="flex-col mt-10">
      <RouterLink class="text-xl" to="/blogs/2022-08-15-games">
        2022GAMES研究生学术成长论坛分享 <div i-uil-letter-chinese-a class="text-blue-500"></div>
      </RouterLink>
    </div>
  </div>
</template>

<route lang="yaml">
meta:
  layout: default
</route>
