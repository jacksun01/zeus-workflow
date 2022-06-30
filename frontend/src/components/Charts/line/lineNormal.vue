<template>
  <div :id="chartid" :style="testyle"/>
</template>

<script>
  import echarts from 'echarts'
  import {genUuid} from '@/utils'
  export default {
    props: {
      chartData: {
        type: Object,
        default: {},
        require: true,
      },
      settings: {
        type: Object,
        default: {},
      },
      chartid: {
        type: String,
        default: 'chartid',
      },
      width: {
        type: String,
        default: '500px'
      },
      height: {
        type: String,
        default: '500px'
      }
    },
    data() {
      return {
        chart: null,
        testyle: '',
      }
    },
    mounted() {
      this.initChart()
    },
    beforeDestroy() {
      if (!this.chart) {
        return
      }
      this.chart.dispose()
      this.chart = null
    },
    created() {
      this.testyle = "height:" + this.height + ";" + "width:" + this.width + ";"
      if (this.settings.hasOwnProperty('chartid')) {
        this.chartid = this.chartid + this.settings['chartid']
      } else {
        this.chartid = this.chartid + '' + genUuid()
      }
    },
    methods: {
      initChart() {
        this.chart = echarts.init(document.getElementById(this.chartid))

        var xData = this.chartData['xData']
        var yData = this.chartData['yData']
        var legendData = []

        var series=[]
        for(var i=0;i<yData.length;i++){
          var serie={'name':yData[i]['name'],'type':'line','data':yData[i]['data'],smooth: true}
          series.push(serie)
          legendData.push(yData[i]['name'])
        }

        this.chart.setOption(
          {
            title: {
              text: this.settings['title']
            },
            tooltip: {
              trigger: 'axis'
            },
            legend: {'data':legendData},
            grid: {
              left: '3%',
              right: '4%',
              bottom: '3%',
              containLabel: true
            },
            toolbox: {
              feature: {
                saveAsImage: {}
              }
            },
            xAxis: {
              type: 'category',
              boundaryGap: false,
              data: xData
            },
            yAxis: {
              type: 'value'
            },
            series: series,
          }
      )
      }
    }
  }
</script>
