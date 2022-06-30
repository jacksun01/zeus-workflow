<template>
  <div class="chart-container">
    <normalXhBar height="300px" width="800px" :chartData="chartData" :settings="settings"/>
  </div>
</template>

<script>
  import {normalXhBar} from '@/components/Charts/bar'

  export default {
    name: 'xhChart',
    components: {normalXhBar},
    data() {
      return {
        chartData: {
          'xData':['芝罘区', '福山区', '莱山区', '牟平区', '海阳市', '莱阳市', '蓬莱市', '栖霞市', '龙口市', '长岛县', '招远市', '莱州市', '开发区', '高新区', '昆嵛山', '龙海', '机场', '核电'],
          'yData':[10758, 3975, 2980, 1831, 2122, 3018, 3525, 1729, 2764, 380, 3988, 2333, 3596, 453, 365, 9, 67, 48],
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
