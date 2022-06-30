<template>
  <div class="chart-container">
    <normalMapChart height="100%" width="100%" :chartData="chartData" :settings="settings"/>
  </div>
</template>

<script>
  import {normalMapChart} from '@/components/Charts/map'

  export default {
    name: 'MixChart',
    components: {normalMapChart},
    data() {
      return {
        chartData: {
          'xData': ['1month', '2month', '3month', '4month', '5month', '6month', '7month',],
          'yData': [
            {'name':'female','type':'bar','data':[709, 1917,2455,2610,1544,1830,5000,]},
            {'name':'male','type':'bar','data':[327,1776,507,1200,800,482,204,]},
            {'name':'child','type':'bar','data':[200,1276,1507,2200,500,1482,904,]},
            {'name':'sum','type':'line','data':[709,1917,2455,2610,1719,1433,1544,]},
            {'name':'avg','type':'line','data':[1036,3693,2962,3810,2519,1915,1748,]},
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
