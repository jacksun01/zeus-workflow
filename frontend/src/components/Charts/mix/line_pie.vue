<template>
  <div :id="chartid" :style="testyle"/>
</template>

<script>
  import echarts from 'echarts'
  import {genUuid, COLORLIST} from '@/utils'

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

        var titleColor = '#999'
        if (this.settings.hasOwnProperty('titleColor')) {
          titleColor = this.settings['titleColor']
        }
        var series = []
        var colorlist = []
        var legendData = []
        var num = 0
        for (var i = 0; i < yData['lineData'].length; i++) {
          legendData.push(yData['lineData'][i].name)
          series.push({
            name: yData['lineData'][i].name,
            smooth: true,
            type: 'line',
            symbolSize: 8,
            symbol: 'circle',
            data: yData['lineData'][i].data
          })
          if (i < COLORLIST.length) {
            colorlist.push(COLORLIST[num])
          } else {
            num = 0
            colorlist.push(COLORLIST[num])
          }
          num = num + 1
        }
        console.log(series)

        if (yData.hasOwnProperty("pie1Data")) {
          var pie1Series = []
          var num = 0
          for (var i = 0; i < yData['pie1Data'].length; i++) {
            var item = yData['pie1Data'][i]

            var colortmp = ""
            if (i < COLORLIST.length) {
              colortmp = COLORLIST[num]
            } else {
              num = 0
              colortmp = COLORLIST[num]
            }
            num = num + 1
            pie1Series.push(
              {
                value: item['value'],
                name: item['name'],
                tooltip: {
                  show: false
                },
                itemStyle: {
                  normal: {
                    color: colortmp
                  }
                },
                label: {
                  normal: {
                    textStyle: {
                      color: colortmp,
                    },
                    formatter: item['name'] + ' {d} % \n',
                    fontSize: 15
                  }
                }
              }
            )
          }
          series.push({
            type: 'pie',
            center: ['83%', '33%'],
            radius: ['20%', '25%'],
            data: pie1Series,
          })
        }

        if (yData.hasOwnProperty("pie2Data")) {
          var pie2Series = []
          var num = 0
          for (var i = 0; i < yData['pie2Data'].length; i++) {
            var item = yData['pie2Data'][i]
            var colortmp = ""
            if (i < COLORLIST.length) {
              colortmp = COLORLIST[num]
            } else {
              num = 0
              colortmp = COLORLIST[num]
            }
            num = num + 1
            pie2Series.push(
              {
                value: item['value'],
                name: item['name'],
                tooltip: {
                  show: false
                },
                itemStyle: {
                  normal: {
                    color: colortmp
                  }
                },
                label: {
                  normal: {
                    textStyle: {
                      color: colortmp,
                    },
                    formatter: item['value'] + ' {d} % \n',
                    fontSize: 15
                  }
                }
              }
            )
          }
          series.push(
            {
              type: 'pie',
              center: ['83%', '72%'],
              radius: ['20%', '25%'],
              data: pie2Series,
            })
        }

        var subTitle = "子标题"
        if (this.settings.hasOwnProperty("subTitle")) {
          subTitle = this.settings['subTitle']
        }
        this.chart.setOption(
          {
            color: colorlist,
            title: [{
              text: this.settings['title'],
              left: '1%',
              top: '6%',
              textStyle: {
                color: '#999'
              }
            }, {
              text: subTitle,
              left: '83%',
              top: '6%',
              textAlign: 'center',
              textStyle: {
                color: '#999'
              }
            }],
            tooltip: {
              trigger: 'axis'
            },
            legend: {
              x: 300,
              top: '7%',
              textStyle: {
                color: '#999',
              },
              data: legendData,
            },
            grid: {
              left: '1%',
              right: '35%',
              top: '16%',
              bottom: '6%',
              containLabel: true
            },
            xAxis: {
              type: 'category',
              "axisLine": {
                lineStyle: {
                  color: '#000000'
                }
              },
              "axisTick": {
                "show": false
              },
              axisLabel: {
                textStyle: {
                  color: '#000000'
                }
              },
              boundaryGap: false,
              data: xData,
            },
            yAxis: {
              "axisLine": {
                lineStyle: {
                  color: '#000000'
                }
              },
              splitLine: {
                show: true,
                lineStyle: {
                  color: '#000000'
                }
              },
              "axisTick": {
                "show": false
              },
              axisLabel: {
                textStyle: {
                  color: '#000000'
                }
              },
              type: 'value'
            },
            series: series,
          }
        )
      }
    }
  }
</script>
