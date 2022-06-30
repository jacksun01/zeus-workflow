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
        chartid: 'chartid'
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

        var startValue = xData[0]
        if (xData.length > 100) {
          startValue = xData[xData.length - 100]
        }


        var titleColor = '#999'
        if (this.settings.hasOwnProperty('titleColor')) {
          titleColor = this.settings['titleColor']
        }
        var title = "信息详情"
        if (this.settings.hasOwnProperty('title')) {
          title = this.settings['title']
        }
        var series = []
        for (var i = 0; i < yData.length; i++) {
          var serie = {
            name: yData[i]['name'],
            type: 'line',
            smooth: true,
            data: yData[i]['data']
          }
          series.push(serie)
        }
        console.log('initchart---', xData, yData, series)
        this.chart.setOption(
          {
            title: {
              text: title
            },
            tooltip: {
              trigger: 'axis'
            },
            xAxis: {
              data: xData
            },
            yAxis: {
              splitLine: {
                show: false
              }
            },
            dataZoom: [
              {
                startValue: startValue,
              }, {
                type: 'inside'
              }
            ],
            series: series,
          }
        )
      }
    }
  }
</script>
<style>
  .chartDiv {
    width: 100%;
    height: 100%;
    margin: 0 auto;
  }
</style>
