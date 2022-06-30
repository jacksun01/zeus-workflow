<template>
  <div class="chart-container">
    <Normal2HPieChart height="100%" width="100%" :chartData="chartData" :settings="settings"/>
  </div>
</template>

<script>
  import {Normal2HPieChart} from '@/components/Charts/pie'

  export default {
    name: 'pieChart',
    components: {Normal2HPieChart},
    data() {
      return {
        chartData: {
            innerData: {
              name: '访问来源',
              'data': [ {value: 700, name: '行业大类1'},
                { value: 679, name: '行业大类2'},
                { value: 1548, name: '行业大类3' }
                ]
            },
            outData: { 'name': '访问来源1',
              'data': [{ value: 310, name: '邮件营销' },
                {
                  value: 234,
                  name: '联盟广告'
                },
                {
                  value: 335,
                  name: '视频广告'
                },
                {
                  value: 548,
                  name: '百度'
                },
                {
                  value: 351,
                  name: '谷歌'
                },
                {
                  value: 247,
                  name: '必应'
                }
              ]
            }
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
