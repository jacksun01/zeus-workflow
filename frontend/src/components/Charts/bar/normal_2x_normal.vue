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
        var xper = this.chartData['xper']

        var series=[{
              data: yData,
              type: 'bar',
              label: {
                show: true,
                position: 'top',
                textStyle: {
                  color: '#555'
                }
              },
              itemStyle: {
                normal: {
                  color: (params) => {
                    let colors = ['#4150d8', '#28bf7e', '#ed7c2f', '#f2a93b', '#f9cf36', '#4a5bdc', '#4cd698', '#f4914e', '#fcb75b', '#ffe180', '#b6c2ff', '#96edc1']
                    return colors[params.dataIndex]
                  }
                }
              },
              xAxisIndex: 0,
              yAxisIndex: 0
            }]


        for(var i=0;i<xper.length;i++){
          var item={
              data: [{
                name: xper.name,
                value: 1
              }],
              label: {
                show: true,
                position: 'inside',
                formatter: '{b}',
                offset: [0, 10],
                textStyle: {
                  color: '#777'
                }
              },
              type: 'bar',
              barGap: 0,
              barWidth: xper.per,
              itemStyle: {
                normal: {
                  color: xper.color
                }
              },
              xAxisIndex: 1,
              yAxisIndex: 1
            }
          series.push(item)
        }
        var title = ''
        if (this.settings.hasOwnProperty('title')) {
          title = this.settings.title
        }
        /**
         双X轴标签对应，伪实现思路：
         底部的标签也是柱状图，对应包含的区域为上方X轴条数占总数的比例，设为宽度即可
         */
        this.chart.setOption(
          {
            tooltip: {
              trigger: 'axis',
              axisPointer: {
                type: 'shadow'
              }
            },
            grid: [
              {
                top: 100,
                bottom: 101
              },
              {
                height: 60,
                bottom: 40
              }
            ],
            xAxis: [{
              type: 'category',
              data: xData,
              gridIndex: 0,
              axisLabel: {
                color: '#333'
              },
              axisLine: {
                lineStyle: {
                  color: '#e7e7e7'
                }
              },
              axisTick: {
                lineStyle: {
                  color: '#e7e7e7'
                }
              },
              zlevel: 2
            }, {
              type: 'category',
              gridIndex: 1,
              axisLine: {
                show: false
              },
              zlevel: 1
            }],
            yAxis: [{
              type: 'value',
              gridIndex: 0,
              axisLabel: {
                color: '#333'
              },
              splitLine: {
                lineStyle: {
                  type: 'dashed'
                }
              },
              axisLine: {
                lineStyle: {
                  color: '#ccc'
                }
              },
              axisTick: {
                lineStyle: {
                  color: '#ccc'
                }
              }
            }, {
              type: 'value',
              gridIndex: 1,
              axisLabel: {
                show: false
              },
              axisLine: {
                show: false
              },
              splitLine: {
                show: false
              },
              axisTick: {
                show: false
              }
            }],
            series:
              [
              {
              data: yData,
              type: 'bar',
              label: {
                show: true,
                position: 'top',
                textStyle: {
                  color: '#555'
                }
              },
              itemStyle: {
                normal: {
                  color: (params) => {
                    let colors = ['#4150d8', '#28bf7e', '#ed7c2f', '#f2a93b', '#f9cf36', '#4a5bdc', '#4cd698', '#f4914e', '#fcb75b', '#ffe180', '#b6c2ff', '#96edc1']
                    return colors[params.dataIndex]
                  }
                }
              },
              xAxisIndex: 0,
              yAxisIndex: 0
            }, {
              data: [{
                name: '贵阳市',
                value: 1
              }],
              label: {
                show: true,
                position: 'inside',
                formatter: '{b}',
                offset: [0, 10],
                textStyle: {
                  color: '#777'
                }
              },
              type: 'bar',
              barGap: 0,
              barWidth: '27.2727%',
              itemStyle: {
                normal: {
                  color: 'rgba(134,176,237, .5)'
                }
              },
              xAxisIndex: 1,
              yAxisIndex: 1
            }, {
              data: [{
                name: '六盘水市',
                value: 1
              }],
              label: {
                show: true,
                position: 'inside',
                formatter: '{b}',
                offset: [0, 10],
                textStyle: {
                  color: '#777'
                }
              },
              type: 'bar',
              barGap: 0,
              barWidth: '18.1818%',
              itemStyle: {
                normal: {
                  color: 'rgba(40,191,126, .5)'
                }
              },
              xAxisIndex: 1,
              yAxisIndex: 1
            }, {
              data: [{
                name: '遵义市',
                value: 1
              }],
              label: {
                show: true,
                position: 'inside',
                formatter: '{b}',
                offset: [0, 10],
                textStyle: {
                  color: '#777'
                }
              },
              type: 'bar',
              barGap: 0,
              barWidth: '27.2727%',
              itemStyle: {
                normal: {
                  color: 'rgba(237,124,47, .5)'
                }
              },
              xAxisIndex: 1,
              yAxisIndex: 1
            }, {
              data: [{
                name: '安顺市',
                value: 1
              }],
              label: {
                show: true,
                position: 'inside',
                formatter: '{b}',
                offset: [0, 10],
                textStyle: {
                  color: '#777'
                }
              },
              type: 'bar',
              barGap: 0,
              barWidth: '18.1818%',
              itemStyle: {
                normal: {
                  color: 'rgba(242,169,59, .5)'
                }
              },
              xAxisIndex: 1,
              yAxisIndex: 1
            }, {
              data: [{
                name: '铜仁市',
                value: 1
              }],
              label: {
                show: true,
                position: 'inside',
                formatter: '{b}',
                offset: [0, 10],
                textStyle: {
                  color: '#777'
                }
              },
              type: 'bar',
              barCategoryGap: 0,
              barGap: 0,
              barWidth: '9.0909%',
              itemStyle: {
                normal: {
                  color: 'rgba(249,207,54, .5)'
                }
              },
              xAxisIndex: 1,
              yAxisIndex: 1
            }]
          }
        )
      }
    }
  }
</script>
