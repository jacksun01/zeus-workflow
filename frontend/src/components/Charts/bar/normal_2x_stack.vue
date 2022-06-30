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


        var yData1 = yData[0]['data']
        var yData2 = yData[1]['data']
        var yData3 = yData[2]['data']
        var legend = [yData[0]['name'], yData[1]['name'], yData[2]['name']]
        var colorArr = [
          "#0ee569",
          "#8686f1",
          "#f7c54c",];
        let series = [];

        [yData1, yData2, yData3].forEach((item, index) => {
          var obj = {
            name: legend[index],
            type: "bar",
            data: item,
            stack: "1",
            barGap: 0,
            barWidth: "50%",
            itemStyle: {
              normal: {
                color: colorArr[index]
              }
            },
            label: {
              show: true,
              formatter: function (params, i) {
                return (params.value * 100).toFixed(0) + "%"
              },
              position: "inside"
            },
            xAxisIndex: 0,
            yAxisIndex: 0
          };


          if (index == yData1.length - 1) {
            obj['barCategoryGap'] = 0
          }

          series.push(obj);
        });


        for (var i = 0; i < xper.length; i++) {
          var item = {
            data: [{
              name: xper[i].name,
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
            barWidth: xper[i].per,
            itemStyle: {
              normal: {
                color: xper[i].color
              }
            },
            xAxisIndex: 1,
            yAxisIndex: 1
          }

          if (i == xper.length - 1) {
            item['barCategoryGap'] = 0
          }

          series.push(item)
        }

        var title = ''
        if (this.settings.hasOwnProperty('title')) {
          title = this.settings.title
        }
        var titleColor = '#999'
        if (this.settings.hasOwnProperty('titleColor')) {
          titleColor = this.settings['titleColor']
        }
        /**
         双X轴标签对应，伪实现思路：
         底部的标签也是柱状图，对应包含的区域为上方X轴条数占总数的比例，设为宽度即可
         */
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
            tooltip: {
              trigger: 'axis',
              axisPointer: {
                type: 'shadow'
              }
            },
            grid: [
              {
                left: '10%',
                right: '5%',
                top: 100,
                bottom: 101,
              },
              {
                left: '10%',
                right: '5%',
                height: 60,
                bottom: 40
              }
            ],
            legend: {
              show: true,
              x: 'center',
              top: '20',
              textStyle: {
                color: '#000000'
              },
              data: legend
            },
            xAxis: [
              {
                show: false,
                type: 'category',
                data: xData,
                gridIndex: 0,
                axisLabel: {
                  color: '#333',
                  rotate: 40,
                  fontSize: '10',
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
            series: series,
          }
        )
      }
    }
  }
</script>
