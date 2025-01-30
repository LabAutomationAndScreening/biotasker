
<script setup lang="ts">
const links = [{
  label: "Today's Tasks",
  badge: 100,
  to: '/'
}, {
  label: 'Experiments',
  to: '/experiments'
}, {
  label: 'SOPs',
  to: '/sops'
}]
</script>
<template>
  <UHorizontalNavigation :links="links" />
  <NuxtPage/>
</template>
