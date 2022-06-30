<template>
    <AvueTable :tableOpiton="tableOpiton" :masterApi="masterApi" :masterUri="masterUri" :listQueryExtra="listQueryExtra"/>
</template>

<script>
  import {ApiBase} from '@/api/apibase'
  import {tableNoOptNoMenuSearchM} from '@/utils/avueTableConst'
  import AvueTable from '@/components/AvueTable'

  export default {
    name: 'commonavueAdSearch',
    components: {AvueTable},
    data() {
      return {
        masterApi: ApiBase,
        masterUri:this.$route.path,
        //开关规则字段
        radioCols: [],
        //自定义规则
        rulesCols: [],
        tableOpiton:tableNoOptNoMenuSearchM,
        //配合上边一起搜索使用
        listQueryExtra: []
      }
    },
  }
</script>
