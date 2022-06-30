<template>
  <div :class="className" :id="chartid" :style="{height:height,width:width}"/>
</template>

<script>
  import echarts from 'echarts'
  import {genUuid} from '@/utils'

  export default {
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
        chartid: 'chart'
      }
    },
    created() {
      this.chartid = 'chart' + genUuid()
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
        this.chart = echarts.init(document.getElementById(this.chartid))
        var innerData = this.chartData['innerData']
        var outData = this.chartData['outData']
        var title = this.settings['title']
        var titleColor = '#999'
        if (this.settings.hasOwnProperty('titleColor')) {
          titleColor = this.settings['titleColor']
        }
        this.chart.setOption(
          {
            title: {
              text: title,
              textStyle: {
                fontSize: 16,
                color: titleColor
              },
              left: "2%"
            },
            backgroundColor: '#fff',
            color: ["#2ec7c9", "#b6a2de", "#5ab1ef", "#ffb980", "#d87a80",
              "#8d98b3", "#FFEA01", "#B8D07C", "#fca4bb", "#dc69aa",
              "#07a2a4", "#9a7fd1", "#588dd5", "#f5994e", "#c05050",
              "#59678c", "#c9ab00", "#7eb00a", "#6f5553", "#c14089"
            ],
            tooltip: {
              trigger: 'item',
              formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            series: [{
              name: innerData.name,
              type: 'pie',
              radius: [0, '35%'],
              itemStyle: {
                normal: {
                  borderColor: '#fff',
                  borderWidth: 2
                }
              },
              label: {
                normal: {
                  position: 'inner',
                  show:false,
                }
              },
              labelLine: {
                normal: {
                  show: false
                }
              },
              data: innerData.data
            },
              {
                name: outData.name,
                type: 'pie',
                radius: ['45%', '55%'],
                data: outData.data,
                labelLine: {
                  normal: {
                    length: 20,
                    length2: 100,
                    lineStyle: {
                      color: '#e6e6e6'
                    }
                  }
                },
                label: {
                  normal: {
                    formatter: params => {
                      return (
                        '{icon|●}{name|' + params.name + '}{percent|' + params.percent.toFixed(1) + '%}'
                      );
                    },
                    padding: [0, -130, 25, -130],
                    rich: {
                      color: '#333',
                      icon: {
                        fontSize: 16
                      },
                      name: {
                        fontSize: 14,
                        padding: [0, 5, 0, 5],
                        color: '#666666'
                      },
                      percent: {
                        color: '#333',
                        padding: [0, 5, 0, 0],
                      },
                      value: {
                        fontSize: 16,
                        fontWeight: 'bold',
                        color: '#333333'
                      }
                    }
                  }
                },
              }
            ]
          }
        )
      }
    }
  }
</script>
