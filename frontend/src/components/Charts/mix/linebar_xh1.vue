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

        var titleColor = '#999'
        if (this.settings.hasOwnProperty('titleColor')) {
          titleColor = this.settings['titleColor']
        }

        var y1Data = yData[0].data
        var y2Data = yData[1].data
        var y3Data = yData[2].data

        var max=10000
        for(var i=0;i<y1Data.length;i++){
          if(max<y1Data[i]){
            max=y1Data[i]
          }
        }
        for(var i=0;i<y2Data.length;i++){
          if(max<y2Data[i]){
            max=y2Data[i]
          }
        }

        var legendData=[]
        for(var i=0;i<yData.length;i++){
          legendData.push(yData[i]['name'])
        }

        this.chart.setOption(
          {
            grid: {
              left: '10%',
              right: '5%',
              top: '18%',
              bottom: '19%',
            },
            backgroundColor: '#fff',
            title: {
              text: this.settings['title'],
              textStyle: {
                fontSize: 16,
                color: titleColor,
              },
              left: "2%"
            },
            tooltip: {
              trigger: 'axis',
              axisPointer: {
                type: 'shadow'
              }
            },
            legend: {
              data: legendData,
              right: '3%',
              top: '10%',
              itemWidth: 11,
              itemHeight: 11,
              textStyle: {
                color: '#161616',
                fontSize: 13
              }
            },
            toolbox: {
              show: false,
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
                  fontSize: 12,
                  color: '#161616',
                  margin: 8,
                  interval: 0,
                  formatter: function (val) {
                    return val.split("").join("\n");
                  }
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
                splitNumber: 4,
                axisTick: {
                  show: false
                },
                splitLine: {
                  lineStyle: {
                    color: '#4e608b'
                  }
                },
                axisLabel: {
                  fontSize: 13,
                  color: '#999',
                  margin: 12,
                },
                // max: max,
                min: 0,
                boundaryGap: [0.2, 0.2]
              },
              {
                type: 'value',
                scale: true,
                axisLine: {
                  show: false
                },
                splitNumber: 3,
                axisTick: {
                  show: false
                },
                axisLabel: {
                  fontSize: 13,
                  color: '#000000',
                  margin: 12,
                },
                splitLine: {
                  lineStyle: {
                    color: '#6462d6'
                  }
                },
                name: '',
                // max: 30,
                // min: 0,
                boundaryGap: [0.2, 0.2]
              },

            ],
            series: [
              {
                name: yData[0]['name'],
                type: 'bar',
                label: {
                  normal: {
                    show: true,
                    position: 'top',
                    textStyle: {
                      color: '#ff431a'
                    }
                  }
                },
                itemStyle: {
                  normal: {
                    color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                      offset: 0,
                      color: "#fb925f" // 0% 处的颜色
                    }, {
                      offset: 1,
                      color: "#ff431a" // 100% 处的颜色
                    }], false)
                  }
                },
                barWidth: '40%',
                yAxisIndex: 0,
                data: y1Data
              },
              {
                name: yData[1]['name'],
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
                data: y2Data
              },
              {
                name: '增长比',
                yAxisIndex: 1,
                color: '#ffd300',
                label: {
                  normal: {
                    show: true,
                    position: 'top',
                    textStyle: {
                      color: '#ffd300'
                    }
                  }
                },
                lineStyle: {
                  color: '#ffd300'
                },
                type: 'line',
                data: y3Data
              }
            ]
          }
        )
      }
    }
  }
</script>
