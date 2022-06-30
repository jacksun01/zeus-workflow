<template>
  <div :class="className" :id="chartid" :style="{height:height,width:width}"/>
</template>

<script>
  import echarts from 'echarts'
  import {isRealObj, genUuid} from '@/utils'
  import 'echarts/map/js/china.js'

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
      id: {
        type: String,
        default: 'chart'
      },
      width: {
        type: String,
        default: '500px'
      },
      height: {
        type: String,
        default: '300px'
      },
    },
    data() {
      return {
        chart: null,
        chartid: 'chart1111'
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
        var myChart = echarts.init(document.getElementById(this.chartid))
        var dataList = [
          {name: "南海诸岛", value: 0},
          {name: '北京', value: 0},
          {name: '天津', value: 0},
          {name: '上海', value: 0},
          {name: '重庆', value: 0},
          {name: '河北', value: 0},
          {name: '河南', value: 0},
          {name: '云南', value: 0},
          {name: '辽宁', value: 0},
          {name: '黑龙江', value: 0},
          {name: '湖南', value: 0},
          {name: '安徽', value: 0},
          {name: '山东', value: 0},
          {name: '新疆', value: 0},
          {name: '江苏', value: 0},
          {name: '浙江', value: 0},
          {name: '江西', value: 0},
          {name: '湖北', value: 0},
          {name: '广西', value: 0},
          {name: '甘肃', value: 0},
          {name: '山西', value: 0},
          {name: '内蒙古', value: 0},
          {name: '陕西', value: 0},
          {name: '吉林', value: 0},
          {name: '福建', value: 0},
          {name: '贵州', value: 0},
          {name: '广东', value: 0},
          {name: '青海', value: 0},
          {name: '西藏', value: 0},
          {name: '四川', value: 0},
          {name: '宁夏', value: 0},
          {name: '海南', value: 0},
          {name: '台湾', value: 0},
          {name: '香港', value: 0},
          {name: '澳门', value: 0}
        ]

        var proData = this.chartData['proData']
        for (var i = 0; i < dataList.length; i++) {
          if (isRealObj(proData) && proData.hasOwnProperty(dataList[i]['name'])) {
            dataList[i]['value'] = proData[dataList[i]['name']]
          }
        }

        var titleTip = '信息'
        if (this.chartData.hasOwnProperty('title')) {
          titleTip = this.chartData['title']
        }
        var title = '地图例子'
        if (this.settings.hasOwnProperty('title')) {
          title = this.settings['title']
        }

        var titleColor = '#999'
        if (this.settings.hasOwnProperty('titleColor')) {
          titleColor = this.settings['titleColor']
        }

        var option = {
          title: {
            text: title,
            textStyle: {
              fontSize: 16,
              color: titleColor,
            },
            left: "2%"
          },
          tooltip: {
            formatter: function (params, ticket, callback) {
              return params.seriesName + '<br />' + params.name + '：' + params.value
            }//数据格式化
          },
          visualMap: {
            min: 0,
            max: 80,
            left: 'left',
            top: 'bottom',
            text: ['高', '低'],//取值范围的文字
            inRange: {
              color: ['#e0ffff', '#006edd']//取值范围的颜色
            },
            show: true//图注
          },
          geo: {
            map: 'china',
            roam: false,//不开启缩放和平移
            zoom: 1.23,//视角缩放比例
            label: {
              normal: {
                show: true,
                fontSize: '10',
                color: 'rgba(0,0,0,0.7)'
              }
            },
            itemStyle: {
              normal: {
                borderColor: 'rgba(0, 0, 0, 0.2)'
              },
              emphasis: {
                areaColor: '#F3B329',//鼠标选择区域颜色
                shadowOffsetX: 0,
                shadowOffsetY: 0,
                shadowBlur: 20,
                borderWidth: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          },
          series: [
            {
              name: titleTip,
              type: 'map',
              geoIndex: 0,
              data: dataList
            }
          ]
        }
        myChart.setOption(option);
      }
    }
  }
</script>
