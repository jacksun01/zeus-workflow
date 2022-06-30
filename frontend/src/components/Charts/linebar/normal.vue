<template>
  <div :class="className" id="chartid" :style="{height:height,width:width}"/>
</template>

<script>
  import echarts from 'echarts'
  import resize from '@/components/Charts/mixins/resize'

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
        var xData = this.chartData['xData']
        var yLineData = []
        var yLineTitle = ''
        var yBarData = []
        var yBarTitle = ''
        var legendData = []
        for (var i = 0; i < this.chartData['yData'].length; i++) {
          if (this.chartData['yData'][i].type == 'line') {
            yLineData = this.chartData['yData'][i]['data']
            yLineTitle = this.chartData['yData'][i]['name']
            legendData.push(yLineTitle)
          }
          if (this.chartData['yData'][i].type == 'bar') {
            yBarData = this.chartData['yData'][i]['data']
            yBarTitle = this.chartData['yData'][i]['name']
            legendData.push(yBarTitle)
          }
        }

        var titleColor='#999'
        if(this.settings.hasOwnProperty('titleColor')){
          titleColor=this.settings['titleColor']
        }

        this.chart.setOption(
          {
            title: {
              text: this.settings['title'],
              textStyle: {
                fontSize: 16,
                color: titleColor,
              },
              left: "2%"
            },
            backgroundColor: 'rgba(255,255,255)',
            tooltip: {
              trigger: 'axis',
              backgroundColor: 'rgba(0,0,0,0.1)',
              axisPointer: {
                type: 'shadow',
                label: {
                  show: true,
                  backgroundColor: '#f1f4ff'
                }
              },
              textStyle: {
                color: '#000000',
                fontSize: 14,
                fontWeight: 'bold'
              },
            },
            legend: {
              data: legendData,
              textStyle: {
                color: '#ff861f'
              },
              top: '2%',
            },
            grid: {
              x: '12%',
              width: '82%',
              y: '12%',
            },
            xAxis: {
              data: xData,
              axisLine: {
                lineStyle: {
                  color: '#000000'
                }
              },
              axisTick: {
                show: false,
              },
            },
            yAxis: [{
              splitLine: {show: false},
              axisLine: {
                lineStyle: {
                  color: '#000000',
                }
              },
              axisLabel: {
                formatter: '{value} ',
              }
            },
              {

                splitLine: {show: false},
                axisLine: {
                  lineStyle: {
                    color: '#000000',
                  }
                },
                axisLabel: {
                  formatter: '{value} ',
                }
              }],

            series: [{
              name: yLineTitle,
              type: 'line',
              smooth: false,
              showAllSymbol: true,
              symbol: 'emptyCircle',
              symbolSize: 8,
              yAxisIndex: 1,
              itemStyle: {
                normal: {
                  color: '#ff5847'
                },
              },
              data: yLineData
            },
              {
                name: yBarTitle,
                type: 'bar',
                barWidth: 10,
                itemStyle: {
                  normal: {
                    barBorderRadius: 5,
                    color: new echarts.graphic.LinearGradient(
                      0, 0, 0, 1,
                      [
                        {offset: 0, color: '#956FD4'},
                        {offset: 1, color: '#3EACE5'}
                      ]
                    )
                  }
                },
                data: yBarData,
              }
            ]
          }
        )
      }
    }
  }
</script>
