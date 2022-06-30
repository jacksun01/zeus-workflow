<template>
  <div class="chart-container">
    <normalLineBarChart height="100%" width="100%" :chartData="chartData" :settings="settings"/>
  </div>
</template>

<script>
  import {normalLineBarChart} from '@/components/Charts/linebar'

  export default {
    name: 'MixChart',
    components: {normalLineBarChart},
    data() {
      return {
        chartData: {
          'xData': ['1month', '2month', '3month', '4month', '5month', '6month', '7month',],
          'yData': [
            {'name':'female','type':'bar','data':[709, 1917,2455,2610,1544,1830,5000,3920.1293,2394,3201,2930,6303]},
            {'name':'avg','type':'line','data':[12,56,676,44,25,57,49,192,23,89,303]},
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
