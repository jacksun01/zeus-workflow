<template>
  <div id="chartid" :style="testyle"/>
</template>

<script>
  import echarts from 'echarts'
  import resize from '../mixins/resize'
  const color_list=['#1a9bfc', '#99da69', '#e32f46', '#7049f0', '#fa704d', '#01babc']
  export default {
    mixins: [resize],
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
        console.log(this.chartData)
        this.chart = echarts.init(document.getElementById("chartid"))

        var xData = this.chartData['xData']
        var yData = this.chartData['yData']

        var series = [];
        var legendData = []

        var colornum=0

        for (var i = 0; i < yData.length; i++) {
          legendData.push(yData[i]['name'])

          var color=''
          if(yData[i].hasOwnProperty('color')){
            color=yData[i]['color']
          }else{
            if(colornum>=color_list.length){
              colornum=0
            }
            color=color_list[colornum]
            colornum=colornum+1
          }
          series.push({
            name: yData[i]['name'],
            type: "line",
            symbolSize: 3,//标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示宽和高，例如 [20, 10] 表示标记宽为20，高为10[ default: 4 ]
            symbol: 'circle',//标记的图形。ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
            smooth: true, //是否平滑曲线显示
            showSymbol: false, //是否显示 symbol, 如果 false 则只有在 tooltip hover 的时候显示
            areaStyle: {
              normal: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                  offset: 0,
                  color: color
                }, {
                  offset: 0.8,
                  color: 'rgba(255,255,255,0)'
                }], false),
                // shadowColor: 'rgba(255,255,255, 0.1)',
                shadowBlur: 10,
                opacity: 0.3,
              }
            },
            itemStyle: {
              normal: {
                color: color,
                lineStyle: {
                  width: 1,
                  type: 'solid' //'dotted'虚线 'solid'实线
                },
                borderColor: color, //图形的描边颜色。支持的格式同 color
                borderWidth: 8,//描边线宽。为 0 时无描边。[ default: 0 ]
                barBorderRadius: 0,
                label: {
                  show: false,
                },
                opacity: 0.5,
              }
            },
            data: yData[i]['data'],
          })
        }

        this.chart.setOption(
          {
            backgroundColor: "#141f56",
            legend: {
              top: 20,
              itemGap: 5,
              itemWidth: 5,
              textStyle: {
                color: '#fff',
                fontSize: '10'
              },
              data: legendData
            },
            title: {
              text: this.settings['title'],
              textStyle: {
                color: '#fff',
                fontSize: '22',
                fontWeight: 'normal',
              },
              subtextStyle: {
                color: '#90979c',
                fontSize: '16',

              },
            },
            tooltip: {
              trigger: "axis",
              axisPointer: { // 坐标轴指示器，坐标轴触发有效
                type: 'line', // 默认为直线，可选为：'line' | 'shadow'
                lineStyle: {
                  color: '#57617B'
                }
              },
              formatter: '{b}<br />{a0}: {c0}%<br />{a1}: {c1}%<br />{a2}: {c2}%<br />{a3}: {c3}%<br />{a4}: {c4}%<br />{a5}: {c5}%',
              backgroundColor: 'rgba(0,0,0,0.7)', // 背景
              padding: [8, 10], //内边距
              extraCssText: 'box-shadow: 0 0 3px rgba(255, 255, 255, 0.4);', //添加阴影
            },
            grid: {
              borderWidth: 0,
              top: 110,
              bottom: 95,
              textStyle: {
                color: "#fff"
              }
            },
            xAxis: [{
              type: "category",
              axisLine: {
                lineStyle: {
                  color: '#32346c'
                }
              },
              splitLine: {
                show: true,
                lineStyle: {
                  color: '#32346c ',
                }
              },
              boundaryGap: false, //坐标轴两边留白策略，类目轴和非类目轴的设置和表现不一样
              axisTick: {
                show: false
              },
              splitArea: {
                show: false
              },
              axisLabel: {
                inside: false,
                textStyle: {
                  color: '#bac0c0',
                  fontWeight: 'normal',
                  fontSize: '12',
                },
              },
              data: xData,
            }],
            yAxis: {
              type: 'value',
              axisTick: {
                show: false
              },
              axisLine: {
                show: true,
                lineStyle: {
                  color: '#32346c',
                }
              },
              splitLine: {
                show: true,
                lineStyle: {
                  color: '#32346c ',
                }
              },
              axisLabel: {
                textStyle: {
                  color: '#bac0c0',
                  fontWeight: 'normal',
                  fontSize: '12',
                },
                formatter: '{value}%',
              },
            },
            series: series,
          }
        )
      }
    }
  }
</script>
