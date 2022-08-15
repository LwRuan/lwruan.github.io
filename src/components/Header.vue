<script setup lang="ts">
const { t, availableLocales, locale } = useI18n()

const toggleLocales = () => {
  // change to some real logic
  const locales = availableLocales
  locale.value = locales[(locales.indexOf(locale.value) + 1) % locales.length]
}
</script>

<template>
  <header class="pt-4 text-2xl">
    <!-- left -->
    <nav class="flex w-full justify-between">
      <RouterLink class="icon-btn ml-4" to="/" :title="t('button.home')">
        <div i-carbon-cube />
      </RouterLink>
      <!-- right -->
      <div class="pr-2">
        <RouterLink class="icon-btn mx-2" to="/blogs" :title="t('button.blogs')">
          <div i-carbon-document/>
        </RouterLink>
        <button class="icon-btn mx-2 !outline-none" :title="t('button.toggle_dark')" @click="toggleDark()">
          <div i="carbon-moon dark:carbon-sun" />
        </button>
        <a class="icon-btn mx-2" :title="t('button.toggle_langs')" @click="toggleLocales()">
          <div i-carbon-language />
        </a>
        <a class="icon-btn mx-2" rel="noreferrer" href="https://github.com/lwruan" target="_blank" title="GitHub">
          <div i-carbon-logo-github />
        </a>
      </div>
    </nav>
  </header>
</template>