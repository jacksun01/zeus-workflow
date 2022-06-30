<template>
  <div id="chartid" :style="testyle"/>
</template>

<script>
  import echarts from 'echarts'
  import resize from '../mixins/resize'

  //LR:left to right   ,RL:right to left , BT:up to down , TB:down to up , RAD:circular
  var orient_list = [
    {"name": "LR", "data": {"top": "2%", "left": "8%", "right": "20%", "bottom": "2%", "orient": "horizontal"}},
    {"name": "RL", "data": {"top": "2%", "left": "20%", "right": "8%", "bottom": "2%", "orient": "RL"}},
    {"name": "BT", "data": {"top": "20%", "left": "2%", "right": "2%", "bottom": "8%", "orient": "BT"}},
    {"name": "TB", "data": {"top": "8%", "left": "2%", "right": "2%", "bottom": "20%", "orient": "vertical"}},
    {"name": "RAD","data": {"top": "18%", "left": "0", "right": "0", "bottom": "14%", "orient": "vertical", "layout": "radial"}},
  ];

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
      console.log(this.testyle)
    },
    methods: {
      initChart() {
        this.chart = echarts.init(document.getElementById("chartid"))

        var orient = orient_list[0]
        if (this.settings && this.settings.hasOwnProperty("orient")) {
          for (var i = 0; i < orient_list.length; i++) {
            if (this.settings["orient"] == orient_list[i]["name"]) {
              orient = orient_list[i]
              break
            }
          }
        }

        var serie = {
          type: 'tree',
          data: [this.chartData],
          top: orient['data']['top'],
          left: orient['data']['left'],
          bottom: orient['data']['bottom'],
          right: orient['data']['right'],
          orient: orient['data']['orient'],
          symbolSize: 7,
          label: {
            normal: {
              position: 'left',
              verticalAlign: 'middle',
              align: 'right',
              fontSize: 9
            }
          },
          leaves: {
            label: {
              normal: {
                position: 'right',
                verticalAlign: 'middle',
                align: 'left'
              }
            }
          },

          expandAndCollapse: true,
          animationDuration: 550,
          animationDurationUpdate: 750
        }
        if (orient['name'] == 'RAD') {
          delete serie.label
          delete serie.leaves
          serie['layout'] = 'radial'
        }
        var series = [serie]

        this.chart.setOption(
          {
            tooltip: {
              trigger: 'item',
              triggerOn: 'mousemove'
            },
            series: series
          })
        console.log(this.chart)
      }
    }
  }
</script>
