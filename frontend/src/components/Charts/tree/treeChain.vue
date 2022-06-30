<template>
  <div id="chartid" :style="stylestr"/>
</template>

<script>
  import echarts from 'echarts'

  //LR:left to right   ,RL:right to left , BT:up to down , TB:down to up , RAD:circular
  var orient_list = [
    {"name": "LR", "data": {"top": "2%", "left": "8%", "right": "20%", "bottom": "2%", "orient": "horizontal"}},
    {"name": "RL", "data": {"top": "2%", "left": "20%", "right": "8%", "bottom": "2%", "orient": "RL"}},
    {"name": "BT", "data": {"top": "20%", "left": "2%", "right": "2%", "bottom": "8%", "orient": "BT"}},
    {"name": "TB", "data": {"top": "8%", "left": "2%", "right": "2%", "bottom": "20%", "orient": "vertical"}},
    {"name": "RAD","data": {"top": "18%", "left": "0", "right": "0", "bottom": "14%", "orient": "vertical", "layout": "radial"}},
  ];

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
        stylestr: 'position: relative; overflow: hidden; padding: 0px; margin: 0px; border-width: 0px; cursor: default;',
      }
    },
    mounted() {
      document.getElementById("chartid").oncontextmenu = () => {
        return false
      }
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
      this.stylestr = this.stylestr+"height:" + this.height + ";" + "width:" + this.width + ";"
      console.log(this.stylestr)
    },
    methods: {
      initChart() {
        this.chart = echarts.init(document.getElementById("chartid"))
        echarts.util.each(this.chartData, function (datum, index) {
          index % 2 === 0 && (datum.collapsed = true);
        });
        var orient = orient_list[0]
        if (this.settings && this.settings.hasOwnProperty("orient")) {
          for (var i = 0; i < orient_list.length; i++) {
            if (this.settings["orient"] == orient_list[i]["name"]) {
              orient = orient_list[i]
              break
            }
          }
        }
        var serise = {
          type: 'tree',
          initialTreeDepth: 10,
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
              fontSize: 13,
              "color": "rgb(0,255,252)"
            }
          },
          itemStyle: {
            "normal": {
              "color": "rgb(0,255,252)",
              "borderWidth": 0
            }
          },
          "lineStyle": {
            "normal": {
              "color": "#F4A460",
              "curveness": 0.5
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
          delete serise.label
          delete serise.leaves
          serise['layout'] = 'radial'
        }
        var series = [serise]
        this.chart.setOption(
          {
            backgroundColor: 'rgb(43, 51, 59)',
            tooltip: {
              trigger: 'item',
              triggerOn: 'mousemove'
            },
            series: series,
          })
        this.chart.on('contextmenu', this.handleOpen);
      },
      handleOpen(params) {
        this.$emit("handleOpen", params)
      },
    }
  }
</script>
