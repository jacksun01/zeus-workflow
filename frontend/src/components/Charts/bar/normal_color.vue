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
            backgroundColor: '#fff',
            "title": {
                "text": "DB工单使用次数统计",
                x: "center",
                y:"4%",
                textStyle: {
                    color: '#00265f',
                    fontSize: '16'
                },
                subtextStyle: {
                    color: '##00265f',
                    fontSize: '16',

                },
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            grid: {
                top: '15%',
                right: '3%',
                left: '5%',
                bottom: '12%'
            },
            xAxis: [{
                type: 'category',
//                data: ['制造业', '建筑业', '农林牧渔', '房地产', '金融业', '居民服务及其他'],
                data: xData,
                axisLine: {
                    lineStyle: {
                        color: '#00265f'
                    }
                },
                axisLabel: {
                    margin: 10,
                    color: '#00265f',
                    interval:0,
                    rotate:10,
                    textStyle: {
                        fontSize: 14
                    },
                },
            }],
            yAxis: [{
                name: '单位：次',
                axisLabel: {
                    formatter: '{value}',
                    color: '#00265f',
                },
                axisLine: {
                    show: false,
                    lineStyle: {
                        color: '#00265f'
                    }
                },
                splitLine: {
                    lineStyle: {
                        color: '#00265f'
                    }
                }
            }],
            series: [{
                type: 'bar',
//                data: [5000, 2600, 1300, 1300, 1250, 1500],
                data: yData,
                barWidth: '20px',
                itemStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(0,244,255,1)' // 0% 处的颜色
                        }, {
                            offset: 1,
                            color: 'rgba(0,77,167,1)' // 100% 处的颜色
                        }], false),
                        barBorderRadius: [30, 30, 30, 30],
                        shadowColor: '#00265f',
                        shadowBlur: 4,
                    }
                },
                label: {
                    normal: {
                        show: true,
                        lineHeight: 30,
                        width: 80,
                        height: 30,
                        backgroundColor: '#00265f',
                        borderRadius: 200,
                        position: ['-8', '-60'],
                        distance: 1,
                        formatter: [
                            '    {d|●}',
                            ' {a|{c}}     \n',
                            '    {b|}'
                        ].join(','),
                        rich: {
                            d: {
                                color: '#3CDDCF',
                            },
                            a: {
                                color: '#fff',
                                align: 'center',
                            },
                            b: {
                                width: 1,
                                height: 30,
                                borderWidth: 1,
                                borderColor: '#234e6c',
                                align: 'left'
                            },
                        }
                    }
                }
            }]
          }
        )
      }
    }
  }
</script>
