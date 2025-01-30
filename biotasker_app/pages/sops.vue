<script setup lang="ts">
const people = [{
  id: 1,
  sop_name: 'Aedes aegypti',
  num_stages: '5',
  total_duration: '20 days'
}, {
  id: 1,
  sop_name: 'Maintenance',
  num_stages: '3',
  total_duration: '12 days'
}]
</script>
<template>

    <div>
        Create New SOP<br>
        SOPs<br>
        <UTable :rows="people" />
    </div>
  </template>
