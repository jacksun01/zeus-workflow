<template>
  <div :class="className" :id="chartid" :style="{height:height,width:width}"/>
</template>

<script>
  import echarts from 'echarts'
  import {genUuid,COLORLIST,getDataWithUnitFiex} from '@/utils'

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
        var data = this.chartData['data']
        var title = "信息"
        if (this.settings.hasOwnProperty("title")) {
          title = this.settings['title']
        }
        var centerTitle = "信息"
        if (this.settings.hasOwnProperty("centerTitle")) {
          centerTitle = this.settings['centerTitle']
        }
        var centerSubTitle = ""
        if (this.settings.hasOwnProperty("subtitle")) {
          centerSubTitle = this.settings['subtitle']
        }
        var titleColor = '#999'
        if (this.settings.hasOwnProperty('titleColor')) {
          titleColor = this.settings['titleColor']
        }

        //单位
        var unit=""
        if (this.settings.hasOwnProperty('unit')) {
          unit = this.settings['unit']
        }

        var legendData=[]
        for(var i=0;i<data.length;i++){
          legendData.push(data["name"])
        }
        var colorData=[]
        var num=0
        for(var i=0;i<data.length;i++){
          if(num==COLORLIST.length){
            num=0
          }
          colorData.push(COLORLIST[num])
          num=num+1
        }

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
              text: centerTitle,
              subtext: centerSubTitle,
              x: 'center',
              y: 'center',
              textStyle: {
                fontWeight: 'normal',
                fontSize: 16
              }
            }],
            tooltip: {
              show: true,
              trigger: 'item',
              formatter: "{b}: {c} ({d}%)"
            },
            legend: {
              orient: 'horizontal',
              bottom: '0%',
              data: legendData,
            },
            series: [{
              type: 'pie',
              selectedMode: 'single',
              radius: ['25%', '58%'],
              color: colorData,

              label: {
                normal: {
                  position: 'inner',
                  formatter: '{d}%',
                  textStyle: {
                    color: '#fff',
                    fontWeight: 'bold',
                    fontSize: 14
                  }
                }
              },
              labelLine: {
                normal: {
                  show: false
                }
              },
              data: data
            }, {
              type: 'pie',
              radius: ['58%', '83%'],
              itemStyle: {
                normal: {
                  color: '#F2F2F2'
                },
                emphasis: {
                  color: '#ADADAD'
                }
              },
              label: {
                normal: {
                  position: 'inner',
                  // formatter: '{c}'+unit,
                  formatter: params => {
                      return (
                        params.name+""+getDataWithUnitFiex(params.value, 10000, ["","万", "亿"],1)
                      );
                    },

                  textStyle: {
                    color: '#777777',
                    fontWeight: 'bold',
                    fontSize: 10
                  }
                }
              },
              data: data
            }]
          }
        )
      }
    }
  }
</script>
