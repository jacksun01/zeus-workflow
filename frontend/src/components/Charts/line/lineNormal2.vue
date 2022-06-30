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
//      chartid: {
//        type: String,
//        default: 'lineonechartid',
//      },
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
        chartid:'chartid1234',
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
//    watch: {
//      chartData: {
//        deep: true,
//        handler(newValue, oldValue) {
//          this.chartData = newValue;
//          this.initChart()
//        }
//      }
//    },
    methods: {
      initChart() {
        this.chart = echarts.init(document.getElementById(this.chartid))
        var xData = this.chartData['xData']
        var yData = this.chartData['yData']
        var legendData = [yData[0]['name']]

        var series=[]
        for(var i=0;i<yData.length;i++){
          var serie={'name':yData[i]['name'],'type':'line','data':yData[i]['data'],smooth: true}
          series.push(serie)
          legendData.push(yData[i]['name'])
        }

        var titleColor='#999'
        if(this.settings.hasOwnProperty('titleColor')){
          titleColor=this.settings['titleColor']
        }
        this.chart.setOption(
          {
            backgroundColor: '#fff',
            title: {
              text: this.settings['title'],
              textStyle: {
                fontSize: 16,
                color: titleColor,
              },
              left: "2%"
            },
            color: ['#73A0FA', '#73DEB3', '#FFB761','#af408b','#7866FF','#658897'],
            tooltip: {
              trigger: 'axis',
              axisPointer: {
                type: 'cross',
                crossStyle: {
                  color: '#999'
                },
                lineStyle: {
                  type: 'dashed'
                }
              }
            },
            grid: {
              left: '25',
              right: '25',
              bottom: '24',
              top: '75',
              containLabel: true
            },
            legend: {
              data: legendData,
              orient: 'horizontal',
              icon: "rect",
              show: true,
              left: 150,
              top: 15,
            },
            xAxis: {
              type: 'category',
              data: xData,
              splitLine: {
                show: false
              },
              axisTick: {
                show: false
              },
              axisLine: {
                show: false
              },
            },
            yAxis: {
              type: 'value',
              axisLabel: {
                color: '#999',
                textStyle: {
                  fontSize: 12
                },
              },
              splitLine: {
                show: true,
                lineStyle: {
                  color: '#F3F4F4'
                }
              },
              axisTick: {
                show: false
              },
              axisLine: {
                show: false
              },
            },
            series: series,
          }
        )
      }
    }
  }
</script>
