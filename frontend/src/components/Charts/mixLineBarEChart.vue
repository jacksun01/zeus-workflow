<template>
  <div :class="className" id="chartid" :style="{height:height,width:width}"/>
</template>

<script>
  import echarts from 'echarts'
  import resize from './mixins/resize'
  import {basecolors} from '@/utils'

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
        colorbar:['rgba(255,144,128,1)','rgba(153,82,48,1)','rgba(63,159,79,1)','rgba(0,204,204,1)'],
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
        //init ydata
        var ydata_list = []
        var legend=[]
        var colorlinenum = 0
        var colorbarnum = 0
        for (var i = 0; i < this.chartData['yData'].length; i++) {
          var name = this.chartData['yData'][i]['name']
          legend.push(name)
          var type = this.chartData['yData'][i].hasOwnProperty('type') ? this.chartData['yData'][i]['type'] : 'bar'

          var color = ''

          if(type=='bar'){
            if (colorbarnum < this.colorbar.length) {
             color=this.colorbar[colorbarnum]
            }else{
              colorbarnum=0
              color=this.colorbar[colorbarnum]
            }
            colorbarnum=colorbarnum+1
          }

           if(type=='line'){
            if (colorlinenum < basecolors.length) {
             color=basecolors[colorlinenum]
            }else{
              colorlinenum=0
              color=basecolors[colorlinenum]
            }
            colorlinenum=colorlinenum+1
          }
          var position = 'insideTop'
          var data = this.chartData['yData'][i]['data']
          var ydata = {
            name: name,
            type: type,
            stack: 'total',
            barMaxWidth: 35,
            barGap: '10%',
            itemStyle: {
              normal: {
                color: color,
                label: {
                  show: true,
                  textStyle: {
                    color: '#fff'
                  },
                  position: position,
                  formatter(p) {
                    return p.value > 0 ? p.value : ''
                  }
                }
              }
            },
            data: data
          }
          ydata_list.push(ydata)
        }
        this.chart.setOption({
          backgroundColor: '#344b58',
          title: {
            text: this.settings['title'],
            x: '20',
            top: '20',
            textStyle: {
              color: '#fff',
              fontSize: '22'
            },
            subtextStyle: {
              color: '#90979c',
              fontSize: '16'
            }
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              textStyle: {
                color: '#fff'
              }
            }
          },
          grid: {
            left: '5%',
            right: '5%',
            borderWidth: 0,
            top: 150,
            bottom: 95,
            textStyle: {
              color: '#fff'
            }
          },
          legend: {
            x: '5%',
            top: '10%',
            textStyle: {
              color: '#90979c'
            },
            data: legend
          },
          calculable: true,
          xAxis: [{
            type: 'category',
            axisLine: {
              lineStyle: {
                color: '#90979c'
              }
            },
            splitLine: {
              show: false
            },
            axisTick: {
              show: false
            },
            splitArea: {
              show: false
            },
            axisLabel: {
              interval: 0

            },
            data: this.chartData['xData']
          }],
          yAxis: [{
            type: 'value',
            splitLine: {
              show: false
            },
            axisLine: {
              lineStyle: {
                color: '#90979c'
              }
            },
            axisTick: {
              show: false
            },
            axisLabel: {
              interval: 0
            },
            splitArea: {
              show: false
            }
          }],
          dataZoom: [
            {
              show: true,
              height: 30,
              xAxisIndex: [
                0
              ],
              bottom: 30,
              start: 10,
              end: 80,
              handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
              handleSize: '110%',
              handleStyle: {
                color: '#d3dee5'

              },
              textStyle: {
                color: '#fff'
              },
              borderColor: '#90979c'
            },
            {
              type: 'inside',
              show: true,
              height: 15,
              start: 1,
              end: 35
            }
          ],
          series: ydata_list,
        })
      }
    }
  }
</script>
