<template>
  <div class="chart-container">
    <PieRoseChart height="100%" width="100%" :chartData="chartData" :settings="settings"/>
  </div>
</template>

<script>
  import {PieRoseChart} from '@/components/Charts/pie'

  export default {
    name: 'pieChart',
    components: {PieRoseChart},
    data() {
      return {
        chartData: {
          'data': [
            {'name':'小学','value':63},
            {'name':'幼儿园','value':27},
            {'name':'初中','value':7},
            {'name':'高中','value':10},
            {'name':'大学','value':15},
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
