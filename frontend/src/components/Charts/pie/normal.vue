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
        chartid: 'chart',
        colorList:[
          "#8d7fec",
          "#5085f2",
          "#e75fc3",
          "#f87be2",
          "#f2719a",
          "#fca4bb",
          "#f59a8f",
          "#fdb301",
          "#37ecac",
          "#cf9ef1",
          "#57e7ec",
          "#cf9ef1"],
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

        if(isRealObj(this.colorArr)&&this.colorArr.length>0){
          this.colorList=this.colorArr
        }
        var data = this.chartData['data']
        var m2R2Data = []
        var total=0
        for (var i = 0; i < data.length; i++) {
          var item = data[i]
          if (i < this.colorList.length) {
            item['itemStyle'] = {color: this.colorList[i]}
          } else {
            item['itemStyle'] = {color: this.colorList[Math.ceil(Math.random() * this.colorList.length)]}
          }
          m2R2Data.push(item)
          total=total+item['value']
        }
        var title = this.settings['title']

        var titleColor = '#999'
        if (this.settings.hasOwnProperty('titleColor')) {
          titleColor = this.settings['titleColor']
        }
        var totalStr = ''
        if (this.settings.hasOwnProperty('totalStr')) {
          totalStr = this.settings['totalStr']
        }else{
          totalStr=total.toFixed(1)
        }
        var isshowtotal=true
        if (this.settings.hasOwnProperty('showtotal')) {
          isshowtotal = showtotal
        }
        this.chart.setOption(
          {
            title: [
              {
                text: title,
                textStyle: {
                  fontSize: 14,
                  color: titleColor
                },
                left: "3%",
                top:"8%"
              },
              {
                show:isshowtotal,
                text: '总数',
                subtext: totalStr,
                textStyle: {
                  fontSize: 20,
                  color: "black"
                },
                subtextStyle: {
                  fontSize: 20,
                  color: 'black'
                },
                textAlign: "center",
                x: '30%',
                y: '42%',
              }],
            tooltip: {
              trigger: 'item',
              formatter: function (parms) {
                var str = parms.seriesName + "</br>" +
                  parms.marker + "" + parms.data.legendname + "</br>" +
                  "数量：" + parms.data.value + "</br>" +
                  "占比：" + parms.percent + "%";
                return str;
              }
            },
            legend: {
              type: "scroll",
              orient: 'vertical',
              left: '63%',
              align: 'left',
              top: 'middle',
              textStyle: {
                color: '#8C8C8C'
              },
              height: 250
            },
            series: [
              {
                name: title,
                type: 'pie',
                center: ['30%', '50%'],
                radius: ['30%', '50%'],
                clockwise: false, //饼图的扇区是否是顺时针排布
                avoidLabelOverlap: false,
                label: {
                  normal: {
                    show: true,
                    position: 'outter',
                    formatter: function (parms) {
                      return parms.percent + "%"
                    }
                  }
                },
                labelLine: {
                  normal: {
                    length: 5,
                    length2: 3,
                    smooth: true,
                  }
                },
                data: m2R2Data
              }
            ]
          }
        )
      }
    }
  }
</script>
