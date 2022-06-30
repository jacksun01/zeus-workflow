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
        var yData = this.chartData['yData']
        var xData = this.chartData['xData']
        var title=''
        if(this.settings.hasOwnProperty('title')){
          title=this.settings['title']
        }
        this.chart.setOption(
          {
            backgroundColor: '#081534',
            grid: {
              left: '5%',
              right: '2%',
              top: '1%',
              bottom: '1%',
              containLabel: true
            },
            title: {
              text: title,
              show: true,
              textStyle: {
                color: '#ffffff',
                fontSize: 18,
                fontWeight: "500"
              }
            },
            tooltip: {
              trigger: 'axis',
              formatter: function (c) {
                let d;
                for (let i = 0; i < c.length; i++) {
                  if (c[i].axisIndex === 0) {
                    d = c[i].axisValue + ' : ' + c[i].data + 'ms';
                  }
                }
                return d;
              },
            },
            xAxis: {
              show: false
            },
            yAxis: [{
              show: true,
              data: yData,
              inverse: true,
              max: 4,
              axisLabel: {
                textStyle: {
                  fontSize: 12,
                  color: '#fff'
                }
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
            }, {
              show: true,
              inverse: true,
              data: xData,
              max: 4,
              axisLabel: {
                textStyle: {
                  fontSize: 12,
                  color: '#fff'
                }
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
            series: [
              {
                type: 'pictorialBar',
                yAxisIndex: 0,
                barWidth: 10,
                symbol: 'path://d="M70 90 L130 100 L130 80 Z"',
                itemStyle: {
                  emphasis: {
                    opacity: 1
                  }
                },
                data: xData
              },
              {
                symbol: 'circle',
                symbolSize: 16,
                symbolOffset: ['50%', 0],
                symbolPosition: 'end',
                type: "pictorialBar",
                yAxisIndex: 1,
                data: xData
              }
            ]
          }
        )
      }
    }
  }
</script>
<style>
  .chartDiv{
  width: 100%;
  height: 100%;
  margin: 0 auto;
}
</style>
