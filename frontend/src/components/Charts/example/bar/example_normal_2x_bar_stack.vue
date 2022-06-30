<template>
  <div class="chart-container">
    <normal2XBar height="500px" width="900px" :chartData="chartData" :settings="settings"/>
  </div>
</template>

<script>
  import {normal2XBar} from '@/components/Charts/bar'

  export default {
    name: 'xhChart',
    components: {normal2XBar},
    data() {
      return {
        chartData: {
          xData: ['项目1', '项目2', '项目3', '项目4', '项目5', '项目6', '项目7', '项目8', '项目9', '项目10','项目11'],
          xper: [
            {name: '用户运营', per: '27.2727%', color: 'rgba(134,176,237, .5)'},
            {name: '学习交易', per: '18.1818%', color: 'rgba(40,191,126, .5)'},
            {name: '平台研发', per: '27.2727%', color: 'rgba(237,124,47, .5)'},
            {name: '大数据', per: '18.1818%', color: 'rgba(242,169,59, .5)'},
            {name: '通讯研发', per: '9.0909%', color: 'rgba(249,207,54, .5)'},
          ],
          yData: [
            {"name": 'cpu', 'data': [0.1, 0.15, 0.18, 0.23, 0.24, 0.32, 0.31, 0.36, 0.57, 0.72, 0.45]},
            {"name": 'mem', 'data': [0.2, 0.11, 0.11, 0.2, 0.21, 0.32, 0.33, 0.34, 0.56, 0.71, 0.41]},
            {"name": 'disk', 'data': [0.2, 0.15, 0.18, 0.25, 0.23, 0.31, 0.36, 0.31, 0.51, 0.72, 0.45],}
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
