<script setup lang="ts">
const people = [{
  id: 1,
  description: 'Maintain Strain SV01',
  sop_name: 'Aedes aegypti',
  assignee: 'Michelle',
  start_date: '01/23/2024'
}, {
  id: 2,
  description: 'Maintain Strain SV05',
  sop_name: 'Aedes aegypti',
  assignee: 'Junru',
  start_date: '01/29/2024'
}]
</script>

<template>
    <div>Experiments</div>
    <UTable :rows="people" />
  </template>
