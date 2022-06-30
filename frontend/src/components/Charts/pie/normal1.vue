<template>
  <div :class="className" :id="chartid" :style="{height:height,width:width}"/>
</template>

<script>
  import echarts from 'echarts'
  import {genUuid,isRealObj} from '@/utils'
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
      colorArr: {
        type: Array,
        default: () => [],
      },
    },
    data() {
      return {
        chart: null,
        chartid:'chart',
        colorList:[
          '#1b75ff',
          '#00acee',
          '#17e3ee',
          '#46d51e',
          '#22d58b',
          '#f1a621',
          '#e2f119',
          '#f18ab1',
          '#e260f1',
          '#a7e7ff',
          '#c8efff',
        ],
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

        if(isRealObj(this.colorArr)&&this.colorArr.length>0){
          this.colorList=this.colorArr
        }
        var colors = []
        var num = 0
        for (var i = 0; i < data.length; i++) {
          if (i < this.colorList.length) {
            colors.push(this.colorList[i])
          } else {
            num = num + 1
            colors.push(this.colorList[num])
          }
        }

        var title = this.settings['title']
        var titleColor = '#999'
        if (this.settings.hasOwnProperty('titleColor')) {
          titleColor = this.settings['titleColor']
        }
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
              trigger: 'item',
              formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            series: [{
              name: title,
              type: 'pie',
              radius: '68%',
              center: ['50%', '50%'],
              clockwise: false,
              data: data,
              label: {
                normal: {
                  textStyle: {
                    color: '#999',
                    fontSize: 14,
                  }
                }
              },
              labelLine: {
                normal: {
                  show: false
                }
              },
              itemStyle: {
                normal: {
                  borderWidth: 4,
                  borderColor: '#ffffff',
                },
                emphasis: {
                  borderWidth: 0,
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              }
            }],
            color: colors,
            backgroundColor: '#fff'
          }
        )
      }
    }
  }
</script>
