<template>
  <div :class="className" id="chartid" :style="{height:height,width:width}"/>
</template>

<script>
  import echarts from 'echarts'
  import resize from '../mixins/resize'
  import {basecolors} from '@/utils'

  const colorArr = ["#218de0", "#01cbb3", "#85e647", "#5d5cda", "#05c5b0", "#c29927"];
  const colorAlpha = ['rgba(60,170,211,0.05)', 'rgba(1,203,179,0.05)', 'rgba(133,230,71,0.05)', 'rgba(93,92,218,0.05)', 'rgba(5,197,176,0.05)', 'rgba(194,153,39,0.05)']
  export default {
    mixins: [resize],
    props: {
      settings: {
        type: Object,
        require: true,
        default: {'title': '', 'legend': []}
      },
      chartData: {
        type: Object,
        require: true,
        default: {'xData': [], 'yData': []}
      },
      className: {
        type: String,
        default: 'chart'
      },
      id: {
        type: String,
        default: 'chart'
      },
      width: {
        type: String,
        default: '500px'
      },
      height: {
        type: String,
        default: '500px'
      },
    },
    data() {
      return {
        chart: null,
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
    methods: {
      initChart() {
        this.chart = echarts.init(document.getElementById("chartid"))
        var data_list = []
        var colornum = 0
        var chartdata_list=this.chartData['data']
        for (var i = 0; i < chartdata_list.length; i++) {
          if (i >= colorArr.length) {
            colornum = 0
          }
          var data = {
            value: chartdata_list[i]['value'],
            name: chartdata_list[i]['name'],
            itemStyle: {
              borderColor: colorArr[colornum],
              borderWidth: 2,
              shadowBlur: 20,
              shadowColor: colorArr[colornum],
              shadowOffsetx: 25,
              shadowOffsety: 20,
              color: colorAlpha[colornum]
            }
          }
          colornum=colornum+1
          data_list.push(data)
        }

        this.chart.setOption(
          {
            backgroundColor: "#090e36",
            title: {
              text: this.settings['title'],
              textStyle: {
                color: '#fff',
                fontSize: '22',
                fontWeight: 'normal',
              },
              subtextStyle: {
                color: '#90979c',
                fontSize: '16',
              },
            },
            grid: {
              left: -100,
              top: 50,
              bottom: 10,
              right: 10,
              containLabel: true
            },
            tooltip: {
              trigger: 'item',
              formatter: "{b} : {c} ({d}%)"
            },
            legend: {
              show: false
            },
            polar: {},
            angleAxis: {
              interval: 1,
              type: 'category',
              data: [],
              z: 10,
              axisLine: {
                show: false,
                lineStyle: {
                  color: "#0B4A6B",
                  width: 1,
                  type: "solid"
                },
              },
              axisLabel: {
                interval: 0,
                show: true,
                color: "#0B4A6B",
                margin: 8,
                fontSize: 16
              },
            },
            radiusAxis: {
              min: 20,
              max: 120,
              interval: 20,
              axisLine: {
                show: false,
                lineStyle: {
                  color: "#0B3E5E",
                  width: 1,
                  type: "solid"
                },
              },
              axisLabel: {
                formatter: '{value} %',
                show: false,
                padding: [0, 0, 20, 0],
                color: "#0B3E5E",
                fontSize: 16
              },
              splitLine: {
                lineStyle: {
                  color: "#07385e",
                  width: 2,
                  type: "dashed"
                }
              }
            },
            calculable: true,
            series: [{
              stack: 'a',
              type: 'pie',
              radius: '80%',
              roseType: 'radius',
              zlevel: 10,
              startAngle: 100,
              label: {
                normal: {
                  formatter: ['{b|{b}}', '{d|{d}%}'].join('\n'),
                  rich: {
                    b: {
                      color: '#3bd2fe',
                      fontSize: 14,
                      lineHeight: 20
                    },
                    d: {
                      color: '#d0fffc',
                      fontSize: 14,
                      height: 20
                    },
                  },
                }
              },
              labelLine: {
                normal: {
                  show: true,
                  length: 10,
                  length2: 45,
                  lineStyle: {
                    color: '#0096b1'

                  }
                },
                emphasis: {
                  show: false
                }
              },
              data: data_list,
            }]
          })
      }
    }
  }
</script>
