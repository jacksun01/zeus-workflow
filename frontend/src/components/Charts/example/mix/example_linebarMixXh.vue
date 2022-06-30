<template>
  <div class="chart-container">
    <linebarMixXh height="100%" width="100%" :chartData="chartData" :settings="settings"/>
  </div>
</template>

<script>
  import {linebarMixXh} from '@/components/Charts/mix'

  export default {
    name: 'lineChart',
    components: {linebarMixXh},
    data() {
      return {
        chartData: {
          'xData': ['芝罘区','福山区','莱山区','牟平区','海阳市','莱阳市','蓬莱市','栖霞市','龙口市','长岛县','招远市','莱州市','开发区','高新区','昆嵛山','龙海','机场','核电'],
          'yData': [
            {'name':'female','data':[10758,3975,2980,1831,2122,3018,3525,1729,2764,380,3988,2333,3596,453,365,9,67,48]},
            {'name':'female','data':[28,4.4,5.9,0.9,0.7,1.1,2.1,0.4,1.9,3.8,1.6,0.7,5.7,6.1]},
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
