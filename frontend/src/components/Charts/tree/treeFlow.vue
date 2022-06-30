<template>
  <div class="hello" id="chartflowid">
    <div id="tree-box">
      <div class="node" v-for="item in nodeList"
           :key="item.id"
           :style="{left: item.left, top: item.top}"
           :id="'node-'+ item.id">
        <strong style="color: red;font-size: 5px">{{ item.name }}</strong>
      </div>

    </div>
    <div>
      <div v-for="item in divList" :style="item.style">
        <AreaColorGradSimpleChart height="100%" width="100%" :chartData="linechartData" :settings="linesettings" :chartid="item.chartid"/>
      </div>
    </div>

  </div>
</template>

<script>
  import {jsPlumb} from "jsplumb";
  import * as D3 from "d3";
  import {AreaColorGradSimpleChart} from '@/components/Charts/line'
  import {isInArray} from '@/utils'

  export default {
    name: 'HelloWorld',
    components: {AreaColorGradSimpleChart},
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
        default: 500
      },
      height: {
        default: 500
      }
    },
    data() {
      return {
        linechartData: {
          'xData': ['10:30', '10:35', '10:40', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月','10:30', '10:35', '10:40', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
          'yData': [
            {
              'name': '幼儿园',
              'color': '#1a9bfc',
              'data': [13.7, 3.4, 13.5, 16.1, 7.4, 15.2, 5.2, 15, 45.2, 25, 12.2, 9.2,13.7, 3.4, 13.5, 16.1, 7.4, 15.2, 5.2, 15, 45.2, 25, 12.2, 9.2]
            },
          ]
        },
        linesettings: {'title': ''},

        jsPlumbInstance: "", // 画线实例
        // jsPlumb默认配置
        jsPlumbSetting: {
          Container: "relation-box",
          // 连线的样式 StateMachine、Flowchart
          Connector: ["Bezier", {curviness: 30}],
          // 鼠标不能拖动删除线
          ConnectionsDetachable: false,
          // 删除线的时候节点不删除
          DeleteEndpointsOnDetach: false,
          // 连线的端点
          Endpoint: ["Dot", {radius: 1}],
          PaintStyle: {stroke: "#c0c4ca", strokeWidth: 1},
          EndpointStyle: {
            stroke: "#888",
            fill: "#fff"
          }
        },
        jsPlumbConnectOptions: {
          isSource: true,
          isTarget: true,
          // 动态锚点、提供了4个方向 Continuous、AutoDefault
          anchor: "AutoDefault"
        },

        dataList: {
          id: 1,
          name: "中国",
          deep: 1,
          children: [
            {
              id: 2,
              name: "北京",
              deep: 2,
              children: [
                {
                  id: 6,
                  name: "海淀区",
                  deep: 3,
                },
                {
                  id: 7,
                  name: "高新区",
                  deep: 3,
                }
              ]
            },
            {
              id: 3,
              name: "贵州",
              deep: 2,
              children: [
                {
                  id: 4,
                  name: "贵阳",
                  deep: 3,
                },
                {
                  id: 5,
                  name: "黔西南",
                  deep: 3,
                },
                {
                  id: 8,
                  name: "黔东南",
                  deep: 3,
                }
              ]
            }
          ]
        },
        middleIdList: [2, 3],
        nodeList: [],
        lineList: [],
        divList: [],
      }
    },
    methods: {
      setNodeInfo(tree) {
        // 参考D3API
        const data = D3.hierarchy(tree);

        // 使用D3 Tree自动布局, nodeSize控制节点x方向和y方向上的距离
        const treeGenerator = D3.tree().nodeSize([90, 90]);
        const treeData = treeGenerator(data);

        // 获取自动布局后的节点信息
        const nodes = treeData.descendants();

        // 获取父子关系列表
        const links = treeData.links();


        console.log("------nodes--->",nodes)

        // 设置节点位置信息
        this.nodeList = nodes.map(item => {
          var node = {
            id: item.data.id,
            name: item.data.name,
            deep:item.data.deep,
            left: item.x + (this.width / 2.3) + "px", // 初始X方向起点位置，默认为屏幕一半
            top: item.y + 20 + "px"
          };
          return node;
        });



        console.log("------nodes--->",this.nodeList[0])

        //重新调整一下 节点位置
        var nodeListTmp=[]
        for(var i=0;i<this.nodeList.length;i++){
          if(i==0){
            continue
          }else{

          }
        }
        //如果 地一个节点和最后的叶子节点都 画在下边，中间节点画在旁边
        for (var i = 0; i < this.nodeList.length; i++) {
          var divtmp = {}
          var topOffset = 0
          var leftOffset = 0
          if (isInArray(this.middleIdList, this.nodeList[i]['id'])) {
            topOffset = 60
            leftOffset = 80
          } else {
            topOffset = 80
            leftOffset = -30
          }
          var top = parseInt(this.nodeList[i]['top'].replace(/px/, ''))
          var left = parseInt(this.nodeList[i]['left'].replace(/px/, ''))

          divtmp['style'] = 'position: absolute;top: ' + (top + topOffset) + 'px;width: 180px;height: 80px;left: ' + (left + leftOffset) + 'px;'
          divtmp['chartid'] = 'chartid' + i
          this.divList.push(divtmp)
        }
        this.lineList = links.map(item => {
          return {
            source: `node-${item.source.data.id}`,
            target: `node-${item.target.data.id}`,
            // overlays: [["Arrow", {width: 10, length: 10, location: 0.5}]]
          }
        })
      },
      drawLines() {
        this.$nextTick().then(() => {
          jsPlumb.ready(() => {
            this.jsPlumbInstance = jsPlumb.getInstance();

            this.jsPlumbInstance.importDefaults(this.jsPlumbSetting);

            this.lineList.forEach(item => {
              this.jsPlumbInstance.connect(item, this.jsPlumbConnectOptions);
            });

            this.jsPlumbInstance.repaintEverything(); // 重绘
          })
        })
      },
      handleAction(item, action) {
        this.$emit("handleAction", item, action)
      },
    },
    mounted() {
      this.setNodeInfo(this.chartData);
      this.drawLines();
      document.getElementById("chartflowid").oncontextmenu = () => {
        return false
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #tree-box {
    position: relative;
  }

  .node {
    position: absolute;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 20px 30px;
  }
</style>
