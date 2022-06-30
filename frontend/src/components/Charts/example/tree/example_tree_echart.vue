<template>
  <div class="chart-container">
    <treeEChart :chartData="chartData" :settings="settings"/>
  </div>
</template>

<script>
  import {treeEChart} from '@/components/Charts/tree'

  export default {
    name: 'treeecharts',
    components: {treeEChart},
    data() {
      return {
        chartData: {
          name: 'root',
          children: [
            {
              name: 'node1',
              children: [
                {'name': 'leafnode1'},
                {'name': 'leafnode2'}
              ]
            },
            {name: 'node2'},
            {
              name: 'node3',
              collapsed: true,  //孩子节点是否不展开
              children: [
                {'name': 'leafnode1'},
                {'name': 'leafnode2'}
              ]
            },
          ]
        },
        //orient  LR 从左到右,RL 从右到左,BT 从上到下,TB 从下到上,RAD:雷达 圆形 ,默认LR   settings可以不写这个属性
        settings:{'orient':'LR'}
      }
    },
  }
</script>

<style scoped>
  .chart-container {
    position: relative;
    width: 100%;
    height: calc(100vh - 84px);
  }
</style>
