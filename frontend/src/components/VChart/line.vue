<template>
  <span>
  <ve-line :title="attrs.title" :data="chartData" :url="url" :width="attrs.width" :height="attrs.height" :settings="settings"></ve-line>
    </span>
</template>

<script>
  import request from '@/utils/request'
  export default {
    name: 'VChartLine',
    props: {
      url: {
        type: String,
      },
    },
    data() {
      return {
        attrs: {'title': {text: ''}, width: 'auto', height: '400px'},
        settings: {},
        chartData: {
          columns: [],
          rows: []
        }
      }
    },
    created() {
      request.get(this.url).then(response => {
        this.chartData.columns = response.data.columns
        this.chartData.rows = response.data.rows
        if(response.data.attrs.hasOwnProperty('title')) {this.attrs.title = response.data.attrs.title}
        if(response.data.attrs.hasOwnProperty('height')) {this.attrs.height = response.data.attrs.height}
        if(response.data.attrs.hasOwnProperty('width')) {this.attrs.width = response.data.attrs.width}
        if(response.data.hasOwnProperty('settings')) {this.attrs.settings = response.data.settings}
      })
    },
  }
</script>
