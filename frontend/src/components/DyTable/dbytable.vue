<template>
  <div class="app-container">
    <strong style="margin-top: 5px;margin-bottom: 10px">{{tableTitle}}</strong>
    <el-table
      :data="tableData"
      :tableKey="tableKey"
      ref="dyTable"
      tooltip-effect="dark"
      style="width: 100%">
      <template v-for='(col) in localTableCols'>
        <el-table-column
          :prop="col.key"
          :label="col.value"
          :key="col.key"
        >
        </el-table-column>
      </template>
    </el-table>
  </div>
</template>
<script>
  import {isRealObj} from '@/utils'

  export default {
    props: {
      tableData: {
        type: Array,
        required: true
      },
      tableCols: {
        type: Array,
        required: true
      },
      tableKey: {
        type: Number,
        required: false,
        default: 0,
      },
      tableTitle:{
        type: String,
        required: false,
        default: '信息详情',
      }
    },
    created() {
      this.initTableCols()
    },
    methods: {
      initTableCols() {
        if (!isRealObj(this.tableCols) || this.tableCols.length < 1) {
          this.localTableCols = []
          for (var key in this.tableData[0]) {
            this.localTableCols.push({'key': key, 'value': key})
          }
        }else{
          this.localTableCols=this.tableCols
        }
      },
    }
  }
</script>
