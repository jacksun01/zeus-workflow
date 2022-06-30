<template>
  <div class="chart-container">
    <linePieMix height="100%" width="100%" :chartData="chartData" :settings="settings"/>
  </div>
</template>

<script>
  import {linePieMix} from '@/components/Charts/mix'

  export default {
    name: 'lineChart',
    components: {linePieMix},
    data() {
      return {
        chartData: {
          'xData': ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'],
          'yData': {
            'lineData':[
                {'name':'机器','data':[10758,3975,2980,1831,2122,3018,3525,1729,2764,380,3988,2333,3596,453,365,9,67,48]},
                {'name':'磁盘','data':[28,4.4,5.9,0.9,0.7,1.1,2.1,0.4,1.9,3.8,1.6,0.7,5.7,6.1]},
                {'name':'其他','data':[28,4.4,5.9,0.9,0.7,1.1,2.1,0.4,1.9,3.8,1.6,0.7,5.7,6.1]},
              ],
            'pie1Data':[
                {'name':'机器','value':180},
                {'name':'磁盘','value':280},
                {'name':'其他','value':122},
              ],
            'pie2Data':[
                {'name':'机器1','value':180},
                {'name':'磁盘1','value':233},
                {'name':'其他1','value':129},
              ]
          }
        },
        settings: {'title': '静态数据','subTitle':'子标题1'},
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
