<template>
  <ve-line :title="title" :data="data" :width="width" :height="height" :settings="settings"></ve-line>
</template>

<script>
  export default {
    name: 'VChartLine',
    props: {
      title: {
        type: String,
        required: true,
      },
      width: {
        type: String,
        default: 'auto',
      },
      height: {
        type: String,
        default: '400px',
      },
      data: {
        type: String,
        required: true,
      },
      settings: {
        type: Object,
        default: {},
      }
    },
  }
</script>
