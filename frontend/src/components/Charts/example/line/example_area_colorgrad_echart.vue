<template>
  <div class="chart-container" style="padding: 10px">
    <AreaColorGradChart height="100%" width="100%" :chartData="chartData" :settings="settings"/>
  </div>
</template>

<script>
  import {AreaColorGradChart} from '@/components/Charts/line'

  export default {
    name: 'colorGradLineChart',
    components: {AreaColorGradChart},
    data() {
      return {
        chartData: {
          'xData': ['1month', '2month', '3month', '4month', '5month', '6month'],
          'yData': [
            {'name':'幼儿园','color':'#1a9bfc','data':[13.7, 3.4, 13.5, 16.1, 7.4, 15.2]},
            {'name':'小学','data':[17.4, 13.7, 13.5, 3.4, 15.2, 13.5]},
            {'name':'初中','color':'#e32f46','data':[13.4, 7.4, 13.7, 13.5, 16.1, 13.7]},
            {'name':'高中','color':'#7049f0','data':[3.5, 15.2, 16.1, 17.4, 13.4, 6.1]},
            {'name':'大学','data':[16.1, 13.5, 3.7, 17.4, 15.2, 18.9]},
            {'name':'研究生','color':'#01babc','data':[17.4, 6.1, 13.4, 15.2, 13.7, 5.2]},
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
