<template>
  <div :id="chartid" :style="testyle"/>
</template>

<script>
  import echarts from 'echarts'
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
        this.chartid=this.chartid+''+new Date().getTime()
      }
    },
    methods: {
      initChart() {
        this.chart = echarts.init(document.getElementById(this.chartid))
        var xData = this.chartData['xData']
        var yData = this.chartData['yData']
        var titleColor = '#999'
        if (this.settings.hasOwnProperty('titleColor')) {
          titleColor = this.settings['titleColor']
        }
        var legendData = []
        var serie_list=[]
        var barColor='#563b80'
        if(this.settings.hasOwnProperty('barcolor')){
          barColor=this.settings['barcolor']
        }
        var xycolor='#5d5865'
        if(this.settings.hasOwnProperty('xycolor')){
          barColor=this.settings['xycolor']
        }
        for(var i=0;i<yData.length;i++){
          serie_list.push(yData[i])
        }
        this.chart.setOption( {
           title: {
              text: this.settings['title'],
              textStyle: {
                fontSize: 16,
                color: titleColor,
              },
              left: "2%"
            },
          tooltip: {},
          legend: {
            data: legendData,
            textStyle: {
              color: '#26bd30',
              align: 'left',
              fontSize: 12
            }
          },
          xAxis: {
            data: xData ,
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
          series: [{data: serie_list,type: "bar",itemStyle: {

                    normal: {
                        color: function(params) {


                            var colorList = [

                              '#C1232B','#B5C334','#FCCE10','#E87C25','#27727B',

                               '#FE8463','#9BCA63','#FAD860','#F3A43B','#60C0DD',

                               '#D7504B','#C6E579','#F4E001','#F0805A','#26C0C0',

                            ];
                          var index;
                            if (params.dataIndex >= colorList.length) {
                                       index = params.dataIndex - colorList.length;
                                       return colorList[index];
                                    }
                            return colorList[params.dataIndex]

                        },

                    }

                } }],
        })
      }
    }
  }
</script>
