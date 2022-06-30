<template>
  <div :id="chartid" :style="testyle"/>
</template>

<script>
  import echarts from 'echarts'
    import {genUuid} from '@/utils'
  // import resize from '../mixins/resize'
  export default {
    // mixins: [resize],
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
        chartid:'chartid'
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
      if(this.settings.hasOwnProperty('chartid')){
        this.chartid=this.chartid+this.settings['chartid']
      }else{
        this.chartid = this.chartid + '' + genUuid()
      }
    },
    methods: {
      initChart() {
        this.chart = echarts.init(document.getElementById(this.chartid))
        var xData = this.chartData['xData']
        var yData = this.chartData['yData']
        var legendData = []
        var serie_list=[]
        var barColor='#563b80'
        if(this.settings.hasOwnProperty('barcolor')){
          barColor=this.settings['barcolor']
        }
        var xycolor='#e1ffff'
        if(this.settings.hasOwnProperty('xycolor')){
          barColor=this.settings['xycolor']
        }
        for(var i=0;i<yData.length;i++){
          legendData.push(yData[i]['name'])
          serie_list.push(
          {
              name: yData[i]['name'],
              type: "bar",
              data: yData[i]['data'],
              textStyle: {
                color: '#e1ffff',
                align: 'left',
                fontSize: 12
              },
              itemStyle: {
                normal: {
                  color: barColor,
                  label: {
                    show: true,
                    position: 'top',
                    textStyle: {
                      fontSize: '14',
                      fontWeight: 'bold',
                      color: 'skyblue'
                    }
                  },
                }
              },
            })
        }
        this.chart.setOption( {
          title: {},
          tooltip: {},
          legend: {
            data: legendData,
            textStyle: {
              color: '#5fe9ff',
              align: 'left',
              fontSize: 12
            }
          },
          xAxis: {
            data: xData,
            "axisLabel": {
              "textStyle": {
                "color": xycolor
              }
            },
            "axisLine": {
              "lineStyle": {
                "color": xycolor
              }
            }
          },
          yAxis: {
            "axisLine": {
              "lineStyle": {
                "color": xycolor
              }
            },
            "axisLabel": {
              "textStyle": {
                "color": xycolor,
                fontSize:10,
              },
            },
          },
          series: serie_list,
        })
      }
    }
  }
</script>
