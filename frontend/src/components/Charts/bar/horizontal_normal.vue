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
        var legendData=[]
        var selecteData={}
        var selectedSetting='all'
        if(this.settings.hasOwnProperty('selected')){
          selectedSetting=this.settings['selected']
        }
        for(var i=0;i<yData.length;i++){
          legendData.push(yData[i].name)
          yData[i]['type']='bar'
          if(selectedSetting=='all'){
            selecteData[yData[i]['name']]=true
          }else if(selectedSetting=='one'){
            if(i==0){
              selecteData[yData[i]['name']]=true
            }else{
              selecteData[yData[i]['name']]=false
            }
          }

        }

        this.chart.setOption(
          {
            title: {
              text: this.settings['title'],
            },
            tooltip: {
              trigger: 'axis',
              axisPointer: {
                type: 'shadow'
              }
            },
            legend: {
              data: legendData,
              selected: selecteData,
            },
            grid: {
              left: '3%',
              right: '4%',
              bottom: '3%',
              containLabel: true
            },
            xAxis: {
              type: 'value',
              boundaryGap: [0, 0.01]
            },
            yAxis: {
              type: 'category',
              data: xData,
            },
            series: yData,
          }
        )
      }
    }
  }
</script>
<style>
  .chartDiv {
    width: 100%;
    height: 100%;
    margin: 0 auto;
  }
</style>
