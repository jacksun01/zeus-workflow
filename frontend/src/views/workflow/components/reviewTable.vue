<template>
  <!--author Jack qq:774428957-->
	<span>
	 <el-alert
     style="height: 30px;"
     :title="tabletitle"
     type="info"
     :closable="false">
    </el-alert>
    <div class="filter-container" style="margin-top: 5px">
      <el-input v-model="search" style="width: 200px;" class="filter-item"
                @keyup.enter.native="handleFilter"/>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">{{
        $t('table.search') }}
      </el-button>

       <el-checkbox v-model="mine" v-if="isShowMine" @change="handleChange" style="margin-left: 20px">Mine</el-checkbox>
    </div>
    <el-table
      v-loading="loading"
      :key="tableKey"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%;">
      <el-table-column :label="$t('table.id')" min-width="40%">
        <template slot-scope="scope">
          <span>{{ scope.row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('workflow.name')">
        <template slot-scope="scope">
          <span class="link-type" @click="handleDetail(scope.row)">{{ scope.row.cname }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('workorder.creator')">
        <template slot-scope="scope">
          <span>{{ scope.row.creator_detail.username}}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('workorder.cur_user_role')">
        <template slot-scope="scope">
          <span v-if="scope.row.cur_role_detail!=null&&scope.row.cur_user_detail!=null">{{ scope.row.cur_user_detail.username+"/"+scope.row.cur_role_detail.cname}}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('workorder.exec_status')">
        <template slot-scope="scope">
          <span>{{ scope.row.exec_status|execStatusFilter}}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('workorder.status')">
        <template slot-scope="scope">
          <span>{{ scope.row.status|woStatusFilter}}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('table.create_time')">
        <template slot-scope="scope">
          <span>{{ scope.row.create_time}}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('table.update_time')">
        <template slot-scope="scope">
          <span>{{ scope.row.update_time }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('table.actions')" class-name="small-padding"  v-if="listQuery.hasOwnProperty('action')&&listQuery.action!='done'">
        <template slot-scope="scope">
          <el-button type="primary" size="mini" @click="handleReview(scope.row)" >{{ $t('table.review') }}</el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.pagesize" @pagination="getList()" style="margin-left: 55%;margin-top: 5px"/>
	</span>
</template>

<script>
  import waves from '@/directive/waves'
  import Pagination from '@/components/Pagination'
  import {workorderStatusOptions, workorderExecStatusOptions, reviewOptions,auditRecordOptions} from '@/utils/dict'
  const statusKeyValue = workorderStatusOptions.reduce((acc, cur) => {
    acc[cur.key] = cur.display_name
    return acc
  }, {})
  const execStatusKeyValue = workorderExecStatusOptions.reduce((acc, cur) => {
    acc[cur.key] = cur.display_name
    return acc
  }, {})
  export default {
    name: 'reviewTable',
    directives: {waves},
    components: {Pagination},
    filters: {
      woStatusFilter(status) {
        return statusKeyValue[status]
      },

      execStatusFilter(status) {
        return execStatusKeyValue[status]
      },
      reviewFilter(opinion) {
        for (var i = 0; i < auditRecordOptions.length; i++) {
          if (opinion == auditRecordOptions[i].key) {
            return auditRecordOptions[i].display_name
          }
        }
      },
    },
    data() {
      return {
        search: '',
        loading: false,
        tableKey: 0,
        mine:true,
      }
    },
    props: {
      listQuery: {
        type: Object,
        required: true
      },
      tabletitle: {
        type: String,
        required: true
      },
      list: {
        type: Array,
        required: true
      },
      total: {
        type: Number,
        required: true
      },
      isShowMine: {
        type: Boolean,
        required: false,
        default:false,
      },

    },
   created() {
      this.getList()
    },
    methods: {
      getList() {
        this.$emit("getList",this.listQuery.action,this.mine)
      },
      handleFilter() {
        this.$emit("handleFilter", this.search, this.listQuery.action)
      },
      handleReview(row) {
        this.$emit("handleReview", row)
      },
      handleDetail(row){
        this.$emit("handleDetail", row)
      },
      handleChange(){
        this.getList()
      }
    },
  }
</script>
