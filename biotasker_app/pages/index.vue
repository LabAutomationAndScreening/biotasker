<script setup lang="ts">
const columns = [{
  key: 'stage_name',
  label: 'Stage Name',
  sortable: true
},{
  key: 'experiment',
  label: 'Experiment'
},  {
  key: 'sop',
  label: 'SOP',
  sortable: true
}]
const people = [{

experiment: 'Maintain Strain SV99',
stage_name: 'Set up Cage',
sop: 'Aedes aegypti',
},{

  experiment: 'Maintain Strain SV01',
  stage_name: 'Hatch Egg Cup',
  sop: 'Aedes aegypti',
}, {

experiment: 'Maintain Strain SV05',
stage_name: 'Set up Cage',
sop: 'Aedes aegypti',
}
, ]
</script>

<template>
    <div>Tasks</div>
    <UTable :rows="people" :columns="columns"/>
  </template>
