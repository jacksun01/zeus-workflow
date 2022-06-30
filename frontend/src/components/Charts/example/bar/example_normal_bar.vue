<template>
  <div class="chart-container">
    <normalBar height="100%" width="100%" :chartData="chartData" :settings="settings"/>
  </div>
</template>

<script>
  import {normalBar} from '@/components/Charts/bar'

  export default {
    name: 'MixChart',
    components: {normalBar},
    data() {
      return {
        chartData: {
          'xData': ['1month', '2month', '3month', '4month', '5month', '6month', '7month',],
          'yData':[709, 1917,2455,2610,1544,1830,5000,]
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
