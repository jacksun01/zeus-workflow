<template>
  <div class="chart-container">
    <normal2XBar height="300px" width="500px" :chartData="chartData" :settings="settings"/>
  </div>
</template>

<script>
  import {normal2XBar} from '@/components/Charts/bar'

  export default {
    name: 'xhChart',
    components: {normal2XBar},
    data() {
      return {
        chartData: {
          xData: ['花溪区', '南明区', '观山湖区', '钟山区', '六枝特区', '红花岗区', '汇川区', '遵义县', '西秀区', '平坝县', '玉屏县'],
          xper:[
            {name:'贵州',per:'29.2727%',color:'rgba(134,176,237, .5)'},
            {name:'六盘水市',per:'18.1818%',color:'rgba(40,191,126, .5)'},
            {name:'遵义市',per:'27.2727%',color:'rgba(237,124,47, .5)'},
            {name:'安顺市',per:'27.2727%',color:'rgba(242,169,59, .5)'},
            {name:'安顺市',per:'9.0909%',color:'rgba(249,207,54, .5)'},
            ],
          yData: [0.1, 0.15, 0.18, 0.25, 0.23, 0.32, 0.33, 0.36, 0.57, 0.72, 0.45]
        },
        settings: {'title': '静态数据'},
      }
    },
  }
</script>

<style scoped>
  .chart-container {
    position: relative;
    width: 100%;
    height: calc(100vh - 84px);
  }
</style>
