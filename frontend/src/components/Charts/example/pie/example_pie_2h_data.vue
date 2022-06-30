<template>
  <div class="chart-container">
    <Normal2HDataPieChart height="100%" width="100%" :chartData="chartData" :settings="settings"/>
  </div>
</template>

<script>
  import {Normal2HDataPieChart} from '@/components/Charts/pie'

  export default {
    name: 'pieChart',
    components: {Normal2HDataPieChart},
    data() {
      return {
        chartData: {
          'data': [{
            value: 3661,
            name: '<10w'
          }, {
            value: 5713,
            name: '10w-50w'
          }, {
            value: 9938,
            name: '50w-100w'
          }, {
            value: 17623,
            name: '100w-500w'
          }, {
            value: 3299,
            name: '>500w'
          }]
        },
        settings: {'title': '静态数据','centerTitle':'总费用','centerSubTitle':'abc',"unit":'家'},
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
