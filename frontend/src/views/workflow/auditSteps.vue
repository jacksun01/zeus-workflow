<template>
  <!--author Jack qq:774428957-->
  <div class="app-container">
    <el-alert
        style="height: 40px;width: 98.5%;margin-bottom: 10px"
        :title="'工单名称 [ '+workflowname+' ]'"
        type="success"
        :closable="false">
      </el-alert>
    <div class="filter-container">
      <el-input v-model="listQuery.search" style="width: 200px;" class="filter-item"
                @keyup.enter.native="handleFilter"/>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">{{
        $t('table.search') }}
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit"
                 @click="handleCreate">{{ $t('table.add') }}
      </el-button>
    </div>
    <el-table
      v-loading="listLoading"
      :key="tableKey"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%">
      <el-table-column :label="$t('table.role')">
        <template slot-scope="scope">
          <span>{{ scope.row.role.name }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('table.cname')">
        <template slot-scope="scope">
          <span>{{ scope.row.role.cname }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('workflow_audit.role_type')">
        <template slot-scope="scope">
          <span>{{ scope.row.role_type|roleTypeFilter }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('workflow_formfields.dicurl')">
        <template slot-scope="scope">
          <span>{{ scope.row.url }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('table.create_time')">
        <template slot-scope="scope">
          <span>{{ scope.row.create_time | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('table.actions')" class-name="small-padding fixed-width" fixed="right"
                       label="操作"
                       width="235">
        <template slot-scope="scope">
          <el-button type="primary" size="mini" @click="handleUpdate(scope.row)">{{ $t('table.edit') }}</el-button>
          <el-button v-if="scope.row.status!='deleted'" size="mini" type="danger" @click="handleDelete(scope.row.id)">{{
            $t('table.delete') }}
          </el-button>
          <el-button size="mini" type='primary' @click.stop="moveUp(scope.$index, scope.row)">向上↑</el-button>
          <el-button size="mini" type='primary' @click.stop="moveDown(scope.$index, scope.row)">向下↓</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible" :close-on-click-modal='false'>
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left"
               label-width="100px"
               style="width: 80%; margin-left:30px;">
        <el-form-item :label="$t('workflow_audit.role_type')" prop="role_type">
          <el-select v-model="temp.role_type" filterable>
            <el-option v-for="item in roleTypesOptions" :key="item.key" :value="item.key"
                       :label="item.display_name"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item :label="$t('table.role')" prop="role">
          <el-select v-model="temp.role" filterable>
            <el-option v-for="item in roleOptions" :key="item.id" :value="item.id"
                       :label="item.cname"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item :label="$t('workflow_formfields.dicurl')" prop="url" >
          <el-input v-model="temp.url" placeholder="/api/v1/users/users/?special=project,code_type"/>
          <span style="color: #dcdfe6">
            注意:<br>
             &nbsp;&nbsp;1.接口返回格式json 必须包含id和cname字段 (例如：[{"id":"1","cname":"张三"}])<br>
             &nbsp;&nbsp;2.如果是第一级审核中 可以把工单中某些项的值传递给接口使用，例如 /api/abc/?special=project,code_type 其中special后边的就是 工单中的工单项值，
               假如工单中有一项叫 project，你填写的usercenter 调用接口的时候 /api/abc/?project=usercenter
          </span>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false" size="mini">{{ $t('table.cancel') }}</el-button>
        <el-button v-show="dialogStatus!='detail'" type="primary"
                   @click="dialogStatus==='create'?createData():updateData()" size="mini" v-no-more-click>{{
          $t('table.confirm') }}
        </el-button>
      </div>
    </el-dialog>
    <!-- 删除提示框 -->
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="delVisible" width="300px">
      <div class="del-dialog-cnt">删除不可恢复，是否确定删除？</div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="delVisible = false">取 消</el-button>
        <el-button type="primary" @click="deleteData()">确 定</el-button>
      </span>
    </el-dialog>

  </div>
</template>

<script>
  import {AuditSteps as masterApi, Workflow} from '@/api/workflow'
  import waves from '@/directive/waves' // Waves directive
  import {parseTime, getNowFormatDate} from '@/utils'
  import {Role} from '@/api/user'
  import {conver2KV} from '@/utils'
  import {roleTypesOptions} from '@/utils/dict'

  const roleTypeKeyValue = roleTypesOptions.reduce((acc, cur) => {
    acc[cur.key] = cur.display_name
    return acc
  }, {})
  export default {
    name: 'workflow_approval',
    directives: {waves},
    filters: {
      statusFilter(status) {
        const statusMap = {
          published: 'success',
          draft: 'info',
          deleted: 'danger'
        }
        return statusMap[status]
      },
      roleTypeFilter(value) {
        return roleTypeKeyValue[value]
      },
    },
    data() {
      const validateUrl = (rule, value, callback) => {
        if (this.temp.role_type=="dynamic"&&(value==""||value==null||value==undefined)) {
          callback(new Error('动态角色，必须填写获取接口'))
        } else {
          callback()
        }
      }
      return {
        workflowname: this.$route.query.workflowname,
        roleOptions: [],
        tableKey: 0,
        list: [],
        total: 0,
        workflowid: this.$route.query.workflowid,
        listLoading: true,
        listQuery: {
          page: 1,
          pagesize: 10,
          name: undefined,
          ordering: '-id',
          search: ''
        },
        temp: {
          role: "",
          workflow: "",
          role_type: "",
          url: "",
        },
        dialogFormVisible: false,
        delVisible: false,
        dialogStatus: '',
        textMap: {
          update: this.$t('dialog.update'),
          create: this.$t('dialog.create'),
          delete: this.$t('dialog.delete'),
          detail: this.$t('dialog.detail'),
        },
        rules: {
          workflow: [{required: true, message: 'workflow is required', trigger: 'blur'}],
          role: [{required: true, message: 'role is required', trigger: 'blur'}],
          url: [{required: false, trigger: 'blur', validator: validateUrl}],
        },
        downloadLoading: false,
        roleTypesOptions,
      }
    },
    created() {
      this.getList()
      this.getTableInfo("init")
    },
    methods: {
      getList() {
        Workflow.steps(this.workflowid).then(response => {
          this.list = response
        })
        setTimeout(() => {
          this.listLoading = false
        }, 1 * 1000)
      },

      getTableInfo(action) {
        this.roleOptions=[]
        masterApi.get_table_info().then(response => {
          var roleList = response.roles
          for (var i = 0; i < roleList.length; i++) {
            var isExist = 0
            for (var j = 0; j < this.list.length; j++) {
              if (this.list[j].role.id == roleList[i].id) {
                isExist = 1
                break
              }
            }
            if (isExist == 0) {
              this.roleOptions.push(roleList[i])
            }
          }
          if (action == "detail") {
            this.dialogFormVisible = true
          } else if (action == "create" || action == "update") {
            this.dialogFormVisible = true
            this.$nextTick(() => {
              this.$refs['dataForm'].clearValidate()
            })
          }
        })
      },
      handleFilter() {
        this.listQuery.page = 1
        this.getList()
      },
      resetTemp() {
        this.temp = {
          role: "",
          workflow: "",
          role_type: "",
          url: "",
        }
      },
      handleCreate() {
        this.getTableInfo("create")
        this.resetTemp()
        this.temp.role_type="static"
        this.dialogStatus = 'create'
      },
      createData() {
        this.$refs['dataForm'].validate((valid) => {
          if (valid) {
            this.temp.workflow = this.workflowid
            masterApi.create(this.temp).then(() => {
              this.dialogFormVisible = false
              this.getList()
              this.$notify({
                title: '成功',
                message: '创建成功',
                type: 'success',
                duration: 2000
              })
            })
          }
        })
      },
      handleDetail(row) {
        this.temp = Object.assign({}, row) // copy obj
        this.dialogStatus = 'detail'
        this.dialogFormVisible = true
        this.$nextTick(() => {
          this.$refs['dataForm'].clearValidate()
        })
      },
      handleUpdate(row) {
        this.getTableInfo("update")
        var params = Object.assign({}, row) // copy obj
        delete params.role
        this.temp = Object.assign({}, row)
        this.temp.role=row.role.id
        this.dialogStatus = 'update'
      },
      updateData() {
        this.$refs['dataForm'].validate((valid) => {
          if (valid) {
            const tempData = Object.assign({}, this.temp)
             if(tempData.hasOwnProperty("order_num")){
              delete tempData.order_num
            }
            masterApi.update(this.temp.id, tempData).then(() => {
              for (const v of this.list) {
                if (v.id === this.temp.id) {
                  const index = this.list.indexOf(v)
                  this.list.splice(index, 1, this.temp)
                  break
                }
              }
              this.dialogFormVisible = false
              this.getList()
              this.$notify({
                title: '成功',
                message: '更新成功',
                type: 'success',
                duration: 2000
              })
            })
          }
        })
      },
      handleDelete(id) {
        this.dialogStatus = 'delete'
        this.temp.id = id
        this.delVisible = true
      },
      deleteData() {
        this.delVisible = false
        masterApi.delete(this.temp.id).then(() => {
          this.getList()
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
        })
      },

      moveUp(index, row) {
        if (index > 0) {
          masterApi.up(row.id).then(response => {
            let item = this.list[index - 1];
            this.list.splice(index - 1, 1);
            this.list.splice(index, 0, item);
          })
        } else {
          this.$notify({
            message: '已经是第一条，不可上移',
            type: 'error',
            duration: 2000
          })
        }
      },
//向下移动
      moveDown(index, row) {
        if ((index + 1) === this.list.length) {
          this.$notify({
            message: '已经是最后一条，不可下移',
            type: 'error',
            duration: 2000
          })
        } else {
          masterApi.down(row.id).then(response => {
            let item = this.list[index + 1];
            this.list.splice(index + 1, 1);
            this.list.splice(index, 0, item);
          })
        }
      },
    }
  }
</script>
<style>
  .switchinner .el-switch__label {
    position: absolute;
    display: none;
    color: #fff;
  }

  /*打开时文字位置设置*/
  .switchinner .el-switch__label--right {
    z-index: 1;
    right: -3px;
  }

  /*关闭时文字位置设置*/
  .switchinner .el-switch__label--left {
    z-index: 1;
    left: 19px;
  }

  /*显示文字*/
  .switchinner .el-switch__label.is-active {
    display: block;
  }

  .switchinner.el-switch .el-switch__core,
  .el-switch .el-switch__label {
    width: 50px !important;
  }
</style>
