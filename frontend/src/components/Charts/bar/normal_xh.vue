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
        var barColor = '#563b80'
        if (this.settings.hasOwnProperty('barcolor')) {
          barColor = this.settings['barcolor']
        }
        var title = this.settings['title']
        var titleColor = '#999'
        if (this.settings.hasOwnProperty('titleColor')) {
          titleColor = this.settings['titleColor']
        }
        var totalStr = ''
        if (this.settings.hasOwnProperty('totalStr')) {
          totalStr = this.settings['totalStr']
        }
        this.chart.setOption(
          {
            grid: {
              left: '10%',
              right: '1%',
              top: '10%',
              bottom: '20%',
            },
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
            xAxis: [
              {
                type: 'category',
                boundaryGap: true,
                show: true,
                axisTick: {
                  show: false
                },
                axisLabel: {
                  fontSize: 15,
                  color: '#505050',
                  margin: 8,
                  interval: 0,
//                  formatter: function (val) {
//                    return val.split("").join("\n");
//                  }
                },
                axisLine: {
                  lineStyle: {
                    type: 'solid',
                    color: '#4e608b',//左边线的颜色
                    width: '1'//坐标线的宽度
                  }
                },
                data: xData
              }
            ],
            yAxis: [
              {
                type: 'value',
                scale: true,
                name: '',
                axisLine: {
                  show: false
                },
                axisLabel: {
                  fontSize: 10,
                  color: '#161616',
                  margin: 1,
                },
                // max: 4000,
                min: 0,
                boundaryGap: [0.2, 0.2]
              },
            ],
            series: [
              {
                name: yData['name'],
                type: 'bar',
                label: {
                  normal: {
                    show: true,
                    position: 'top',
                    textStyle: {
                      color: '#1dacfe'
                    }
                  }
                },
                itemStyle: {
                  normal: {
                    color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                      offset: 0,
                      color: "#4889fb" // 0% 处的颜色
                    }, {
                      offset: 1,
                      color: "#15b3ff" // 100% 处的颜色
                    }], false)
                  }
                },
                barWidth: '40%',
                yAxisIndex: 0,
                data: yData['data']
              },

            ]
          }
        )
      }
    }
  }
</script>
