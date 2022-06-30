<template>
  <!--author Jack qq:774428957-->
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.search" style="width: 200px;" class="filter-item"
                @keyup.enter.native="handleFilter"/>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">{{
        $t('table.search') }}
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit"
                 @click="handleCreate">{{ $t('table.add') }}
      </el-button>
      <router-link :to="{ path:'/workflow/workflowgroup/'}">
        <el-button class="filter-item" style="margin-left: 10px;" type="primary">{{$t('workflow.addgroup') }}
        </el-button>
      </router-link>
    </div>
    <el-table
      v-loading="listLoading"
      :key="tableKey"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%">
      <el-table-column :label="$t('table.name')" min-width="40%">
        <template slot-scope="scope">
          <span class="link-type" @click="handleDetail(scope.row)">{{ scope.row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('table.cname')" min-width="50%">
        <template slot-scope="scope">
          <span>{{ scope.row.cname }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('workflow.steps')">
        <template slot-scope="scope">
          <span>{{ scope.row.steps }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('workflow.type')" min-width="50%">
        <template slot-scope="scope">
          <span>{{ scope.row.wftype }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('workflow.group_cname')">
        <template slot-scope="scope">
          <span>{{ scope.row.group_cname }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('table.is_active')" min-width="50%">
        <template slot-scope="scope">
          <span>{{ scope.row.is_active_name }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('table.remark')" min-width="50%">
        <template slot-scope="scope">
          <span>{{ scope.row.remark }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('table.create_time')" min-width="60%">
        <template slot-scope="scope">
          <span>{{ scope.row.create_time | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('table.actions')" class-name="small-padding fixed-width" fixed="right"
                       label="操作"
                       width="280">
        <template slot-scope="scope">
          <router-link
            :to="{ path:'/workflow/formfields/', query: { workflowid: scope.row.id,workflowname:scope.row.name}}">
            <el-button type="primary" size="mini" style="width: 70px">{{
              $t('workflow.addfields') }}
            </el-button>
          </router-link>
          <router-link
            :to="{ path:'/workflow/auditsteps/', query: { workflowid: scope.row.id,workflowname:scope.row.name}}">
            <el-button type="primary" size="mini" style="width: 70px">{{
              $t('workflow.addauditflow') }}
            </el-button>
          </router-link>
          <el-button v-if="scope.row.name!='demo'" type="primary" size="mini" @click="handleUpdate(scope.row)">{{ $t('table.edit') }}</el-button>
          <el-button v-if="scope.row.name!='demo'" size="mini" type="danger" @click="handleDelete(scope.row.id)">{{
            $t('table.delete') }}
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.pagesize"
                @pagination="getList"/>

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible" :close-on-click-modal='false'>
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="100px"
               enctype="multipart/form-data"
               style="width: 80%; margin-left:50px;">
        <el-form-item :label="$t('table.name')" prop="name">
          <el-input v-model="temp.name"/>
        </el-form-item>
        <el-form-item :label="$t('table.cname')" prop="cname">
          <el-input v-model="temp.cname"/>
        </el-form-item>
        <el-form-item :label="$t('workflow.group_cname')" prop="group">
          <el-select v-model="temp.group" filterable>
            <el-option v-for="item in workflowgroups" :key="item.id" :value="item.id" :label="item.cname"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item :label="$t('workflow.script')" prop="script">
          <input type="file" @change="getFile($event)" ref="pathClear" name="file" id="file"
                 v-if="temp.script==''||temp.script==null||typeof temp.script != 'string'"/>
          <a class="link-type" href="/media/workflow/scripts/default.py" download="default.py"
             v-if="temp.script==''||temp.script==null||typeof temp.script != 'string'">下载脚本模板</a>
          <span v-if=" typeof temp.script == 'string' && temp.script!=''&&temp.script!=null">{{temp.script|scriptFilter}}</span>&nbsp;&nbsp;
          <span v-if="typeof temp.script == 'string' && temp.script!=''&&temp.script!=null" class="el-icon-close"
                @click="handleDeleteScript"></span>
        </el-form-item>
 <el-form-item :label="$t('table.is_active')" prop="public">
          <el-switch
            v-model="temp.is_active"
            class="switchinner"
            active-color="#00A854"
            active-text="ON"
            inactive-color="#F04134"
            inactive-text="OFF"
          />
        </el-form-item>
        <el-form-item :label="$t('table.remark')" prop="remark">
          <el-input :autosize="{ minRows: 3, maxRows: 5}" v-model="temp.remark" type="textarea"
                    placeholder="input remark"/>
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
    <!-- 删除提示框 -->
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="delScriptVisible" width="300px">
      <div class="del-dialog-cnt">删除不可恢复，是否确定删除？</div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="delScriptVisible = false">取 消</el-button>
        <el-button type="primary" @click="deleteScript()">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  import {Workflow, Workflowgroup} from '@/api/workflow'
  import waves from '@/directive/waves' // Waves directive
  import {parseTime, getNowFormatDate,isRealObj} from '@/utils'
  import {isvalidEnName,validateURL} from '@/utils/validate'
  import Pagination from '@/components/Pagination' // Secondary package based on el-pagination
  import draggable from 'vuedraggable'
  import {fieldTypeOptions} from '@/utils/dict'
  import request from '@/utils/request'
  import data2blob from '../../components/ImageCropper/utils/data2blob.js'

  export default {
    name: 'workflow_workflow',
    components: {Pagination, draggable},
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
      scriptFilter(script) {
        if (script != null && script != undefined && script != "") {
          var arr = script.split("/")
          return arr[arr.length - 1]
        } else {
          return ""
        }
      },
    },
    data() {
      const validateScript = (rule, script, callback) => {
        if (this.temp.script != null && this.temp.script.size > 1048576) {
          callback(new Error('Please script is less than 1M'))
        } else {
          callback()
        }
      }
      const validateEnName = (rule, value, callback) => {
        if (!isvalidEnName(value)) {
          callback(new Error('Please name should contain only A-Za-z or _'))
        } else {
          callback()
        }
      }
      return {
        workflowgroups: [],
        fieldTypeOptions,
        tableKey: 0,
        list: null,
        total: 0,
        listLoading: true,
        listQuery: {
          page: 1,
          pagesize: 10,
          name: undefined,
          ordering: '-id',
          search: ''
        },
        temp: {
          name: '',
          cname: '',
          remark: '',
          group: '',
          script: '',
          is_active:true,
        },
        dialogFormVisible: false,
        fieldsFormVisible: false,
        delVisible: false,
        delScriptVisible: false,
        dialogStatus: '',
        textMap: {
          update: 'Edit',
          create: 'Create',
          delete: 'Delete'
        },
        rules: {
          name: [{required: true, trigger: 'blur', validator: validateEnName}],
          cname: [{required: true, message: 'cname is required', trigger: 'blur'}],
          group: [{required: true, message: 'group is required', trigger: 'blur'}],
          script: [{required: false, trigger: 'blur', validator: validateScript}],
        },
        downloadLoading: false,
        isUpdateScript: false,
      }
    },
    created() {
      this.init()
    },
    methods: {
      init() {
        this.getList()
      },
      getList() {
        Workflow.list(this.listQuery).then(response => {
          this.list = []
          for(var i=0;i<response.results.length;i++){
            var obj=response.results[i]
            if(isRealObj(obj["script"])){
              obj["wftype"]=  this.$t('workflow.automation')
            }else{
              obj["wftype"]=this.$t('workflow.manual')
            }
            if(obj["is_active"]){
              obj["is_active_name"]="是"
            }else{
              obj["is_active_name"]="否"
            }
            this.list.push(obj)
          }
          this.total = response.count
        })
        setTimeout(() => {
          this.listLoading = false
        }, 1 * 1000)
      },
      handleFilter() {
        this.listQuery.page = 1
        this.getList()
      },
      resetTemp() {
        this.temp = {
          name: '',
          cname: '',
          remark: '',
          script: '',
          is_active:true,
        }
      },
      handleCreate() {
        this.resetTemp()
        this.dialogStatus = 'create'
        this.dialogFormVisible = true
        this.$nextTick(() => {
          this.$refs['dataForm'].clearValidate()
        })
        this.getWorkflowGroupList()
      },
      getWorkflowGroupList() {
        var params={"page":1,"pagesize":500}
        Workflowgroup.list(params).then(response => {
          this.workflowgroups = response.results
        })
      },
      createData() {
        this.$refs['dataForm'].validate((valid) => {
          if (valid) {
            this.upload(1)
          }
        })
      },
      upload(flag) {
        let fmData = new FormData()
        var methodTmp = "post"
        var url = "/workflow/workflows/"
        if (flag == 1) {
          fmData.append("name", this.temp.name)
          fmData.append("cname", this.temp.cname)
          fmData.append("group", this.temp.group)
          fmData.append("remark", this.temp.remark)
        } else {
          fmData.append("name", this.temp.name)
          fmData.append("cname", this.temp.cname)
          fmData.append("group", this.temp.group)
          fmData.append("remark", this.temp.remark)
          fmData.append("id", this.temp.id)
          methodTmp = "put"
          url = url + this.temp.id + "/"
        }

        if (this.temp.script != null && this.temp.script != undefined && this.temp.script != ""&&!validateURL(this.temp.script)) {
          fmData.append("script", this.temp.script)
        }
        // 上传文件
        request({
          url,
          method: methodTmp,
          data: fmData,
        }).then(resData => {
          this.$message({
            title: '成功',
            message: '更新成功',
            type: 'success',
            duration: 2000
          })
          this.dialogFormVisible = false
          this.getList()
        }).catch(err => {
        })
      },
      handleDetail(row) {
        this.temp = Object.assign({}, row) // copy obj
        this.dialogStatus = 'detail'
        this.getWorkflowGroupList()
        this.dialogFormVisible = true
        this.$nextTick(() => {
          this.$refs['dataForm'].clearValidate()
        })
      },


      handleUpdate(row) {
        this.temp = Object.assign({}, row) // copy obj
        this.dialogStatus = 'update'
        this.dialogFormVisible = true
        this.$nextTick(() => {
          this.$refs['dataForm'].clearValidate()
        })
        this.getWorkflowGroupList()
      },
      updateData() {
        this.$refs['dataForm'].validate((valid) => {
          if (valid) {
            if (this.isUpdateScript == 1 && this.temp.script != "" && this.temp.script != undefined && this.temp.script != null&&!validateURL(this.temp.script)) {
              this.upload(0)
            } else {
              const tempData = Object.assign({}, this.temp)
              if(tempData.hasOwnProperty("script")){
                delete tempData.script
              }

              Workflow.update(this.temp.id, tempData).then(() => {
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
          }
        })
      },
      handleDelete(id) {
        this.dialogStatus = 'delete'
        this.temp.id = id
        this.delVisible = true
      },

      handleDeleteScript() {
        this.dialogStatus = 'delete'
        this.delScriptVisible = true
      },

      deleteScript() {
        this.delScriptVisible = false
        this.temp.script = ""
        var params = {}
        params.script = null
        params.id = this.temp.id
        Workflow.update(this.temp.id, params).then(() => {
          for (var i = 0; i < this.list.length; i++) {
            if (this.list[i].id == this.temp.id) {
              this.list[i].script = null
            }
          }
          this.temp.script = null
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.isUpdateScript = 1
        })
      },

      deleteData() {
        this.delVisible = false
        Workflow.delete(this.temp.id).then(() => {
          this.getList()
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
        })
      },

      getFile(event) {
        if (event.target.files.length < 1) {
          this.temp.script = undefined
        } else {
          var file = event.target.files[0];
          if (file.size > 1048576) {
            this.$notify({
              title: '成功',
              message: '脚本文件不能大于1M',
              type: 'error',
              duration: 2000
            })
            this.temp.script = undefined
          } else {
            this.isUpdateScript = 1
            this.temp.script = file
          }
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
