<template>
  <div :id="chartid" :style="testyle"/>
</template>

<script>
  import echarts from 'echarts'
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
      },
      chartid: {
        type: String,
        default: 'chart1'
      },
      isShowY:{
        type:Boolean,
        default:true,
      }
    },
    data() {
      return {
        chart: null,
        testyle: '',
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
    },
    methods: {
      initChart() {
        this.chart = echarts.init(document.getElementById(this.chartid))
        var xData = this.chartData['xData']
        var yData = this.chartData['yData']
        var series = [];
        var legendData = []
        var colornum = 0
        for (var i = 0; i < yData.length; i++) {
          legendData.push(yData[i]['name'])
          series.push({
            type: 'line',
            areaStyle: {},
            data: yData[i]['data'],
          })
        }
        this.chart.setOption(
          {
            tooltip: {
              trigger: "axis",
              padding: [8, 10], //内边距
              extraCssText: 'box-shadow: 0 0 3px rgba(255, 255, 255, 0.4);', //添加阴影
            },
            xAxis: [{
              type: "category",
              boundaryGap: false,
              data: xData,
            }],
            yAxis: {
              show:this.isShowY,
              axisLabel: {
                textStyle: {
                  fontWeight: 'bolder',
                  fontSize: '9',
                },
              },
              splitArea:{show:false},
              axisLine: {show:false},
              axisTick: {show:false},
              splitLine:{show:false},
            },
            series: series,
          }
        )
      }
    }
  }
</script>
