<template>
  <div class="chart-container">
    <MulDataBar height="100%" width="100%" :chartData="chartData" :settings="settings"/>
  </div>
</template>

<script>
  import {MulDataBar} from '@/components/Charts/bar'

  export default {
    name: 'MixChart',
    components: {MulDataBar},
    data() {
      return {
        chartData: {
          'xData': ["中国移动","中国联通"],
          'yData':["北京","河北"],
          "seriesData":[
            {'name':"中国移动","data":[802,303,434,423,356,610,298]},
            {'name':"中国联通","data":[910,303,434,120,356,610,298]},
          ]
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
