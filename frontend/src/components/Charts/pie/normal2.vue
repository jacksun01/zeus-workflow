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
        chartid:'chart'
      }
    },
    created(){
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
        var data = this.chartData['data']
        var title = this.settings['title']
        var titleColor = '#999'
        var total=0
        for(var i=0;i<data.length;i++){
          total=total+data[i].value
        }

        if (this.settings.hasOwnProperty('titleColor')) {
          titleColor = this.settings['titleColor']
        }
        var colorList = ['#afa3f5', '#00d488', '#3feed4', '#3bafff', '#f1bb4c', '#aff', "rgba(250,250,250,0.5)"];
        this.chart.setOption(
          {
            title: [
              {
                text: title,
                textStyle: {
                  fontSize: 16,
                  color: titleColor
                },
                left: "2%"
              },
              {
                subtext: '分布',
                x: 'center',
                y: '47%',
                textStyle: {
                  fontSize: 18,
                  fontWeight: 'normal',
                  color: ['#333']
                },
                subtextStyle: {
                  color: '#f1bb4c',
                  fontSize: 16
                },
              }],
            grid: {
              bottom: 150,
              left: 0,
              right: '10%'
            },
            legend: {
              show: false,
              orient: 'vertical',
              top: "middle",
              right: "5%",
              textStyle: {
                color: '#f2f2f2',
                fontSize: 25,

              },
              icon: 'roundRect'
            },
            series: [
              // 主要展示层的
              {
                radius: ['29%', '59%'],
                center: ['50%', '50%'],
                type: 'pie',
                itemStyle: {
                  normal: {
                    color: function (params) {
                      if (params.dataIndex < colorList.length) {
                        return colorList[params.dataIndex]
                      } else {
                        return colorList[params.dataIndex - colorList.length]
                      }
                    }
                  }
                },
                labelLine: {
                  normal: {
                    show: true,
                    length: 20,
                    length2: 80,
                    lineStyle: {
                      color: '#d3d3d3'
                    },
                    align: 'right'
                  },
                  color: "#000",
                  emphasis: {
                    show: true
                  }
                },
                label: {
                  normal: {
                    formatter: function (params) {
                      var perData=(params.value/total*100).toFixed(1)
                      return params.name + "[" + perData + '%' + "]";
                    },
                    padding: [0, -90],
                    height: 35,
                    rich: {
                      a: {
                        width: 38,
                        height: 38,
                        lineHeight: 1000,
                        align: 'left'
                      },
                      b: {
                        width: 29,
                        height: 45,
                        lineHeight: 50,
                        align: 'left'
                      },
                      c: {
                        width: 34,
                        height: 33,
                        lineHeight: 50,

                        align: 'left'
                      },
                      d: {
                        width: 34,
                        height: 44,
                        lineHeight: 50,
                        align: 'left'
                      },
                      e: {
                        width: 38,
                        height: 30,
                        lineHeight: 50,
                        align: 'left'
                      },
                      nameStyle: {
                        fontSize: 16,
                        color: "#555",
                        align: 'left'
                      },
                      rate: {
                        fontSize: 20,
                        color: "#1ab4b8",
                        align: 'left'
                      }
                    }
                  }
                },
                data: data,
              },
              // 边框的设置
              {
                radius: ['54%', '59%'],
                center: ['50%', '50%'],
                type: 'pie',
                label: {
                  normal: {
                    show: false
                  },
                  emphasis: {
                    show: false
                  }
                },
                labelLine: {
                  normal: {
                    show: false
                  },
                  emphasis: {
                    show: false
                  }
                },
                animation: false,
                tooltip: {
                  show: false
                },
                itemStyle: {
                  normal: {
                    color: 'rgba(250,250,250,0.5)'
                  }
                },
                data: [{
                  value: 1,
                }],
              }
            ]
          }
        )
      }
    }
  }
</script>
