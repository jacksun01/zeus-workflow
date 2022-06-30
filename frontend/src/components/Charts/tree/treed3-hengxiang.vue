<template>
  <div style="overflow-x:scroll;">
    <div :id="id" class="tree-container" >
      <svg class="d3-tree">
        <g class="container">cccc</g>
      </svg>
    </div>
     <div>
      <div v-for="item in nodeDetailList" :style="item.style">
        <AreaColorGradSimpleChart height="100%" width="100%"
                                  :chartData="linechartData"
                                  :settings="linesettings"
                                  :chartid="item.chartid"
                                  :isShowY=false
        />
      </div>
    </div>
  </div>
</template>
<script>
  /**
   * 树状图
   */
//数据
  const dataset = {
    id:1,
    name: "中国",
    children: [
      {
        id:2,
        name: "浙江",
        children: [
          {
            id:3,
            name: "杭州", value: 100,
            children: [
              {
                id:4,
                name: "余杭区", value: 100,
                children: [
                  {
                    name: "三街道", value: 100,id:5,
                    children:[
                      {
                        name: "三1", value: 100,id:30,
                        children:[
                          {name: "三-2", value: 100,id:35}
                        ]
                      },
                      {name: "三3", value: 100,id:36}
                    ]
                  },
                  {name: "2街道", value: 100,id:6},
                  {name: "1街道", value: 100,id:7},
                ]
              },
              {name: "新区", value: 100,id:8},
              {name: "西湖区", value: 100,id:9},
            ]
          },
          {name: "宁波", value: 100,id:10},
          {name: "温州", value: 100,id:11},
          {name: "绍兴", value: 100,id:12}
        ]
      },
      {
        id:13,
        name: "新疆",
        children:
          [
            {name: "乌鲁木齐",id:14},
            {name: "克拉玛依",id:15},
            {name: "吐鲁番",id:16},
            {name: "哈密",id:17}
          ]
      },
      {
        id:18,
        name: "青海",
        children:
          [
            {name: "青海1",id:19},
            {name: '青海2',id:20},
            {name: "青海3",id:21},
            {name: "青海4",id:22}
          ]
      }
    ]
  }

  import * as d3 from 'd3'
  import {AreaColorGradSimpleChart} from '@/components/Charts/line'
import {isInArray} from '@/utils'

  export default {
    name: 'Scale',
    components: {AreaColorGradSimpleChart},
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
        middleIdList: [2, 3],
        lineList: [],

        id: '',
        zoom: null,
        index: 0,
        duration: 750,
        root: null,
        nodes: [],
        links: [],
        dTreeData: null,
        transform: null,
        margin: {top: 20, right: 90, bottom: 30, left: 90},
        nodeDetailList:[],

      }
    },
    methods: {
      uuid() {
        function s4() {
          return Math.floor((1 + Math.random()) * 0x10000)
            .toString(16)
            .substring(1)
        }

        return (
          s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4()
        )
      },
      /**
       * @description 获取构造根节点
       */
      getRoot() {
        let root = d3.hierarchy(dataset, d => {
          return d.children
        })
        root.x0 = this.height / 2
        root.y0 = 0
        return root
      },
      clickNode(d) {
        if (!d._children && !d.children)
          return
        if (d.children) {
          this.$set(d, '_children', d.children)
          d.children = null
        } else {
          this.$set(d, 'children', d._children)
          d._children = null
        }
        this.$nextTick(
          () => {
            this.update(d)
          }
        )
      },

      diagonal(s, d) {
        return `M ${s.y} ${s.x}
                    C ${(s.y + d.y) / 2} ${s.x},
                    ${(s.y + d.y) / 2} ${d.x},
                    ${d.y} ${d.x}`
      },

      /**
       * @description 获取构造的node数据和link数据
       */
      getNodesAndLinks() {
        // treemap generate new x、y coordinate according to root node,
        // so can‘t use computed propter of vue
        this.dTreeData = this.treemap(this.root)
        this.nodes = this.dTreeData.descendants()
        this.links = this.dTreeData.descendants().slice(1)
      },

      /**
       * @description 数据与Dom进行绑定
       */
      update(source) {
        console.log('===========update(source) ==', this.transform)
        this.getNodesAndLinks()
        this.nodes.forEach(d => {
          d.y = d.depth * 220
        })
        // *************************** Nodes section *************************** //
        // Update the nodes...
        const svg = d3.select(this.$el).select('svg.d3-tree')
        const container = svg.select('g.container')
        let node = container.selectAll('g.node')
          .data(this.nodes, d => {
            return d.id || (d.id = ++this.index)
          })
        // Enter any new sources at the parent's previous position.
        let nodeEnter = node.enter().append('g')
          .attr('class', 'node')
          .on('click', this.clickNode)
          .attr('transform', d => {
            return 'translate(' + source.y0 + ',' + source.x0 + ')'
          })
        nodeEnter.append("circle")
          .attr("r", 5)
          .style("fill", function (d) {
            return d.children || d._children ? "lightsteelblue" : "#fff";
          });

        //文字距离圈的位置 位置在文字在下方
        nodeEnter.append("text")
          .attr("font-size",11)
          .attr("font-weight",'bold')
          .attr("x", function (d) {
            return d.children || d._children ? 20 : -50;
          })
          .attr("y", function (d) {
            return 15
          })
          .attr("dy", ".35em")
          .attr("text-anchor", function (d) {
            return d.children || d._children ? "end" : "start";
          })
          .text(function (d) {
            return d.data.name
          })
          .style("fill-opacity", 1e-6);
        // Transition nodes to their new position.
        let nodeUpdate = nodeEnter.merge(node)
          .transition()
          .duration(this.duration)
          .attr("transform", function (d) {
            return "translate(" + d.y + "," + d.x + ")";
          });

        nodeUpdate.select("circle")
          .attr("r", 5)
          .attr("fill", "white")
          .attr("stroke", "blue")
          .attr("stroke-width", 1)
          .style("fill", function (d) {
            return d.children || d._children ? "lightsteelblue" : "#fff";
          });

        nodeUpdate.select("text")
          .style("fill-opacity", 1);

        // Transition exiting nodes to the parent's new position.
        let nodeExit = node.exit()
          .transition()
          .duration(this.duration)
          .attr("transform", function (d) {
            return "translate(" + source.y + "," + source.x + ")";
          })
          .remove();

        nodeExit.select("circle")
          .attr("r", 1e-6);

        nodeExit.select("text")
          .style("fill-opacity", 1e-6);

        // *************************** Links section *************************** //
        // Update the links…
        let link = container.selectAll('path.link')
          .data(this.links, d => {
            return d.id
          })

        // Enter any new links at the parent's previous position.
        let linkEnter = link.enter().insert("path", "g")
          .attr("class", "link")
          .attr("d", d => {
            let o = {x: source.x0, y: source.y0};
            return this.diagonal(o, o)
          })
          .attr("fill", 'none')
          .attr("stroke-width", 1)
          .attr('stroke', '#ccc')
        // Transition links to their new position.
        let linkUpdate = linkEnter.merge(link)
        linkUpdate.transition()
          .duration(this.duration)
          .attr('d', d => {
            return this.diagonal(d, d.parent)
          })

        // Transition exiting nodes to the parent's new position.
        link.exit().transition()
          .duration(this.duration)
          .attr("d", d => {
            let o = {x: source.x, y: source.y};
            return this.diagonal(o, o)
          })
          .remove();

        // Stash the old positions for transition.
        this.nodes.forEach(d => {
          d.x0 = d.x
          d.y0 = d.y
        })
        console.log("----->update---->", this.nodes)

        //如果 地一个节点和最后的叶子节点都 画在下边，中间节点画在旁边
        for (var i = 0; i < this.nodes.length; i++) {
          var divtmp = {}
          var topOffset = 0
          var leftOffset = 0
          var top = this.nodes[i]['x']
          var left = this.nodes[i]['y']
          if(this.nodes[i].data.children&&this.nodes[i].data.children.length>0){
            top=top-60
          }else{
            top=top-20
            left=left+90
          }

          divtmp['style'] = 'position: absolute;top: ' + (top + topOffset) + 'px;width: 180px;height: 80px;left: ' + (left + leftOffset) + 'px;'
          divtmp['chartid'] = 'chartid' + i
          this.nodeDetailList.push(divtmp)
        }
        console.log(this.nodeDetailList)
      },

      /**
       * @description control the canvas zoom to up or down
       */
      zoomed() {
        d3.select(this.$el).select('g.container').attr('transform', this.transform)
      }
    },
    created() {
      this.id = this.uuid()
    },
    mounted() {
      //创建svg画布
      this.width = document.getElementById(this.id).clientWidth
      this.height = document.getElementById(this.id).clientHeight
      const svg = d3.select(this.$el).select('svg.d3-tree')
        .attr('width', this.width)
        .attr('height', this.height)
      this.transform = d3.zoomIdentity.translate(this.margin.left, this.margin.top).scale(1)
      console.log("================>", this.transform)
      const container = svg.select('g.container')
      // init zoom behavior, which is both an object and function
      this.zoom = d3.zoom()
        .scaleExtent([1 / 2, 8])
        .on('zoom', this.zoomed)
      container.transition().duration(this.duration).call(this.zoom.transform, this.transform)
      svg.call(this.zoom)
      this.root = this.getRoot()
      this.update(this.root)
    },
    computed: {
      treemap() {
        return d3.tree().size([this.height, this.width])
      }
    }
  }
</script>
<style lang='scss' scoped>
  .tree-container {
    width: 100%;
    height: 1000px;
  }

  .d3-tree {
    .node {
      cursor: pointer;
    }

    .node circle {
      fill: #fff;
      stroke: steelblue;
      stroke-width: 1.5px;
    }

    .node text {
      font: 18px sans-serif;
    }

    .link {
      fill: none;
      stroke: #ccc;
      stroke-width: 1.5px;
    }
  }
</style>
