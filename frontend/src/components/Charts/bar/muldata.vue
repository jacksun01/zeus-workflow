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
        var seriesData = this.chartData['seriesData']

        var series = []
        for (var i = 0; i < seriesData.length; i++) {
          series.push(
            {
              name: seriesData[i]['name'],
              type: 'bar',
              stack: '总量',
              label: {
                show: true,
                position: 'insideRight'
              },
              data: seriesData[i]['data']
            })
        }

        var title = ''
        if (this.settings.hasOwnProperty('title')) {
          title = this.settings.title
        }

        var title = this.settings['title']
        var titleColor = '#999'
        if (this.settings.hasOwnProperty('titleColor')) {
          titleColor = this.settings['titleColor']
        }
        var opt = {
          title: {
            text: title,
            textStyle: {
              fontSize: 16,
              color: titleColor
            },
            left: "2%"
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
              type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
          },
          legend: {
            data: xData,
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: {
            type: 'value'
          },
          yAxis: {
            type: 'category',
            data: yData,
          },
          series: series,
        }
        this.chart.setOption(opt)
      }
    }
  }
</script>
