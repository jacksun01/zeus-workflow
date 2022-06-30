<template>
  <div class="chart-container">
    <lineNormalTime height="100%" width="100%" :chartData="chartData" :settings="settings"/>
  </div>
</template>

<script>
  import {lineNormalTime} from '@/components/Charts/line'

  export default {
    name: 'lineChart',
    components: {lineNormalTime},
    data() {
      return {
        chartData: {
          'xData': ['1month', '2month', '3month', '4month', '5month', '6month', '7month',],
          'yData': [
            {'name':'female','data':[709, 1917,2455,2610,1544,1830,5000,]},
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
