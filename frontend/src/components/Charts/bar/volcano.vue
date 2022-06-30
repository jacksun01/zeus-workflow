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
        var title = ''
        if (this.settings.hasOwnProperty('title')) {
          title = this.settings.title
        }
        this.chart.setOption({
          backgroundColor: "#38445E",
          tooltip: {
            trigger: 'axis',
            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
              type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
          },
          grid: {
            left: '8%',
            top: '5%',
            bottom: '19%',
            right: '8%'
          },
          xAxis: {
            data: xData,
            axisTick: {
              show: false
            },
            axisLine: {
              lineStyle: {
                color: 'rgba(255, 129, 109, 0.1)',
                width: 1 //这里是为了突出显示加上的
              },
            },
            axisLabel: {
              textStyle: {
                color: '#999',
                fontSize: 10
              },
              formatter: function (val) {
                return val.split("").join("\n");
              },
            },
          },
          yAxis: [{
            splitNumber: 2,
            axisTick: {
              show: false
            },
            axisLine: {
              lineStyle: {
                color: 'rgba(255, 129, 109, 0.1)',
                width: 1 //这里是为了突出显示加上的
              }
            },
            axisLabel: {
              textStyle: {
                color: '#999'
              }
            },
            splitArea: {
              areaStyle: {
                color: 'rgba(255,255,255,.5)'
              }
            },
            splitLine: {
              show: true,
              lineStyle: {
                color: 'rgba(255, 129, 109, 0.1)',
                width: 0.5,
                type: 'dashed'
              }
            }
          }
          ],
          series: [{
            name: title,
            type: 'pictorialBar',
            barCategoryGap: '0%',
            symbol: 'path://M0,10 L10,10 C5.5,10 5.5,5 5,0 C4.5,5 4.5,10 0,10 z',
            label: {
              show: true,
              position: 'top',
              distance: 15,
              color: '#DB5E6A',
              fontWeight: 'bolder',
              fontSize: 16,
            },
            itemStyle: {
              normal: {
                color: {
                  type: 'linear',
                  x: 0,
                  y: 0,
                  x2: 0,
                  y2: 1,
                  colorStops: [{
                    offset: 0,
                    color: 'rgba(232, 94, 106, .8)' //  0%  处的颜色
                  },
                    {
                      offset: 1,
                      color: 'rgba(22, 94, 106, .18)' //  100%  处的颜色
                    }
                  ],
                  global: false //  缺省为  false
                }
              },
              emphasis: {
                opacity: 1
              }
            },
            data: yData,
            z: 10
          }]
        })
      }
    }
  }
</script>
