<template>
  <!--author Jack qq:774428957-->
  <div class="expandwo">
    <div id="workflowleft">
      <div class="app-container">
        <el-alert
          style="height: 30px;"
          :title="$t('workorder.wotype')"
          type="info"
          :closable="false">
        </el-alert>
        <div v-for="group in workflowgroupList">
          <div style="margin-top: 3%;">
            <el-dropdown @command="handleCommand" v-for="(workflowgroup,index)  in group" :key="index">
              <el-button type="success"  class="el-btn">
                {{workflowgroup.cname}}<i class="el-icon-arrow-down el-icon--right"></i>
              </el-button>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item v-for="(item,index1) in workflowgroup.workflow" :command="item" :key="index1">
                  {{item.cname}}
                </el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </div>
        </div>
        <el-alert
          style="height: 30px; margin-top: 20px"
          :title="$t('workorder.mine')"
          type="info"
          :closable="false">
        </el-alert>
        <div style="margin-top: 10px;margin-left: 10px">
          <div class="filter-container">
            <el-input v-model="listQuery.search" style="width: 200px;" class="filter-item"
                      @keyup.enter.native="handleFilter"/>
            <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">{{
              $t('table.search') }}
            </el-button>
          </div>
          <el-table
            v-loading="listLoading"
            :key="tableKey"
            :data="orderList"
            border
            fit
            highlight-current-row
            style="width: 100%;font-size: 10px">
            <el-table-column :label="$t('table.id')" min-width="30%">
              <template slot-scope="scope">
                <span>{{ scope.row.id }}</span>
              </template>
            </el-table-column>
            <el-table-column :label="$t('workflow.name')">
              <template slot-scope="scope">
                <span class="link-type" @click="handleDetail(scope.row)">{{ scope.row.cname }}</span>
              </template>
            </el-table-column>
            <el-table-column :label="$t('workorder.cur_user_role')">
              <template slot-scope="scope">
                <span v-if="scope.row.cur_role_detail!=null&&scope.row.cur_user_detail!=null">{{ scope.row.cur_user_detail.username+"/"+scope.row.cur_role_detail.cname}}</span>
              </template>
            </el-table-column>
            <el-table-column :label="$t('workorder.exec_status')" min-width="50%">
              <template slot-scope="scope">
                <span>{{ scope.row.exec_status|execStatusFilter}}</span>
              </template>
            </el-table-column>
            <el-table-column :label="$t('workorder.status')" min-width="50%">
              <template slot-scope="scope">
                <span>{{ scope.row.status|woStatusFilter}}</span>
              </template>
            </el-table-column>
            <el-table-column :label="$t('table.create_time')">
              <template slot-scope="scope">
                <span>{{ scope.row.create_time  }}</span>
              </template>
            </el-table-column>
            <el-table-column :label="$t('table.update_time')">
              <template slot-scope="scope">
                <span>{{ scope.row.update_time }}</span>
              </template>
            </el-table-column>
            <el-table-column :label="$t('table.actions')" class-name="small-padding"
                             label="操作"
                             min-width="80%">
              <template slot-scope="scope">
                <!--<el-button type="primary" size="mini" @click="handleFeedBack(scope.row)" v-if="scope.row.status==4"-->
                           <!--v-no-more-click>{{ $t('workorder.feedback') }}-->
                <!--</el-button>-->
                <el-button type="primary" size="mini" @click="handleRevoke(scope.row)" v-if="scope.row.status==2 ||scope.row.status==3">撤回</el-button>
                <el-button type="primary" size="mini" @click="handleFeedBack(scope.row)" v-if="scope.row.status==4">反馈</el-button>
              </template>
            </el-table-column>
          </el-table>

          <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.pagesize"
                      @pagination="getOrderList"/>

          <el-dialog :title="workorderName" :visible.sync="dialogFormVisible" customClass="customWidthwo"
                     :close-on-click-modal='false' width="85%">
            <el-steps finish-status="success" simple style="margin-left: 10px; height: 30px;"
                      :active="stepActive" v-if="stepList!=undefined&&stepList!=null&&stepList.length>0">
              <el-step v-for=" (step,index) in stepList" :title="step.role.cname" :key="index"
                       style="font-size: 10px;"></el-step>
            </el-steps>
            <el-alert
              style="height: 30px;margin-left: 10px;width: 98.5%;margin-top: 5px"
              title="工单"
              type="info"
              :closable="false">
            </el-alert>
            <form-create ref="waitingForm" v-model="workorderFields" :rule="formRule" :option="option"
                         class="el-form el-form--label-left form-creat"
                         label-position="left" label-width="100px"
                         style="width: 81%; margin-left:20px;padding: 10px"
                         @dbenv-change="handleDbEnv"
            ></form-create>
            <el-form label-position="left"
                     label-width="220px"  style="width: 90%; margin-left:30px;margin-top: 10px" v-if="uploadfile">
               <el-form-item label="附件上传(单个大小为20M):">
                 <el-upload
                      class="upload-demo"
                      action="/api/v1/workflow/workorders/upload_file/"
                      multiple
                      :limit="3"
                      :on-success="onsuccess"
                      :file-list="fileList">
                  <el-button size="small" type="primary">文件上传</el-button>
                </el-upload>
               </el-form-item>
           </el-form>
            <el-form  v-if="downloadfile" label-position="left"
                     label-width="120px"  style="width: 90%; margin-left:30px;margin-top: 10px" prop="file_info">
              <el-form-item  label="附件下载"
                             v-model="file_info" v-if="file_info.length != 0 && file_info !=undefined && file_info != null">
                   <span class="link-type"><a v-for="item in file_info" :href="item.url" >{{item.name}}<br/></a></span>
              </el-form-item>
            </el-form>

            <el-alert
              style="height: 30px;margin-left: 10px;width: 98.5%"
              title="执行日志"
              type="info"
              :closable="false" v-if="curworkorder!=undefined&&curworkorder.exec_status!=0">
            </el-alert>
            <el-form ref="execDataForm" label-position="left"
                     label-width="120px"
                     style="width: 90%; margin-left:20px;margin-top: 10px"
                     v-if="curworkorder!=undefined&&curworkorder.exec_status!=0">
              <el-form-item :label="$t('workorder.exec_log')" prop="execlog">
                <el-input :autosize="{ minRows: 2, maxRows: 10}" v-model="curworkorder.exec_log" type="textarea"
                          style="width: 83%; margin-left: 15px"/>
              </el-form-item>
            </el-form>
            <el-alert
              style="height: 30px;margin-left: 10px;width: 98.5%"
              title="审批人"
              type="info"
              :closable="false" v-if="isShowNextUser">
            </el-alert>
            <el-form ref="createDataForm" :rules="createRules" :model="createTemp" label-position="left"
                     label-width="120px"
                     style="width: 80%; margin-left:20px;margin-top: 10px" v-if="isShowNextUser">
              <el-form-item :label="$t('table.nextreviewer')" prop="cur_user">
                <span>{{createTemp.cur_user_cname}}</span><span style="margin-left: 10px">
                <el-button @click="handlerRoleUser" size="mini" type="success">选择审批人</el-button></span>
              </el-form-item>
            </el-form>


            <el-alert
              style="height: 30px;margin-left: 10px;width: 98.5%"
              title="反馈"
              type="info"
              :closable="false" v-if="dialogStatus=='feedback'">
            </el-alert>
            <el-form ref="feedbackDataForm" :rules="feedbackRules" :model="feedbackTemp" label-position="left"
                     label-width="100px"
                     style="width: 90%; margin-left:20px;margin-top: 10px" v-if="dialogStatus=='feedback'">
              <el-form-item :label="$t('workorder.feedback')" prop="opinion">
                <el-select v-model="feedbackTemp.opinion" filterable style="width: 83%!important; margin-left: 15px">
                  <el-option v-for="item in feedbackOptions" :key="item.key" :value="item.key"
                             :label="item.display_name"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item :label="$t('table.reviewRemark')" prop="remark">
                <el-input :autosize="{ minRows: 2, maxRows: 4}" v-model="feedbackTemp.remark" type="textarea"
                          placeholder="input remark" style="width: 83%; margin-left: 15px"/>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogFormVisible = false" size="mini">{{ $t('table.cancel') }}</el-button>
              <el-button v-show="dialogStatus!='detail'" type="primary"
                         @click="handleData(dialogStatus)" size="mini" :loading="chickLoading">{{ $t('table.confirm')}}
              </el-button>

              <el-button v-show="isShowSql" type="primary"
                         @click="handleSyntax()" size="mini">{{ $t('mdb_sqljob.checkSyntax')}}
              </el-button>
              <a href="http://help.zeus.com/xxxxxn.html" target="_blank"
                 class="button-type">
                <el-button v-show="isShowSql" type="primary"
                           size="mini">{{ $t('mdb_sqljob.sqlgrammar')}}
                </el-button>
              </a>
            </div>
            <el-alert
              style="height: 30px;margin-left: 10px;width: 98.5%"
              title="审批历史"
              type="info"
              :closable="false" v-if="isShowHistory">
            </el-alert>
            <div style="margin-left: 15px;width: 90%" v-if="isShowHistory">
              <div v-for="auditrecord in auditrecordList" style="margin-top: 5px">
                [{{auditrecord.create_time}}]&nbsp;<span
                v-if="auditrecord.role_detail!=undefined&&auditrecord.role_detail!=null">{{auditrecord.role_detail.cname}}</span>:{{auditrecord.user_detail.username}}({{auditrecord.opinion|reviewFilter}})
                <div v-html="auditrecord.remark" style="margin-top:3px;margin-left:20px;font-size: smaller"/>
              </div>
            </div>
          </el-dialog>
        </div>
      </div>
    </div>
    <div id="workflowright">
      <el-alert
        style="height: 30px; margin-top: 20px;margin-left: 5px;width: 90%"
        :title="$t('workorder.hotwo')"
        type="info"
        :closable="false">
      </el-alert>
      <ul>
        <li v-for="item in hotWorkFlowList">
          <a @click="handleCommand(item)" target="_blank" class="link-type">{{item.group_cname}}->{{item.cname}}</a>&nbsp;&nbsp;&nbsp;&nbsp;
          {{item.num}}{{$t('table.per')}}
        </li>
      </ul>
    </div>

    <!-- 撤销工单提示 -->
    <el-dialog title="撤销工单提示" :visible.sync="revokeDeployVisible" width="300px">
      <div class="del-dialog-cnt">
        <span style="color:red">"是否确认撤回工单"</span>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="revokeDeployVisible = false">取消</el-button>
        <el-button type="primary" @click="Revoke">确认</el-button>
      </span>
    </el-dialog>

    <el-dialog :visible.sync="dialogRoleFormVisible" ref="dataFormDialog">
      <el-form ref="dataForm" :rules="createRules" :model="createTemp" label-position="left" label-width="100px"
               style="width: 80%; margin-left:50px;">
        <el-form-item :label="$t('table.nextreviewer')" prop="cur_user">
          <el-select v-model="createTemp.cur_user" filterable>
            <el-option v-for="item in userList" :key="item.id" :value="item.id"
                       :label="item.cname"></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogRoleFormVisible = false" size="mini">{{ $t('table.cancel') }}</el-button>
        <el-button type="primary" @click="handleAuditUser" size="mini">{{ $t('table.confirm') }}
        </el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
  import {Workflow, Workflowgroup, Workorder} from '@/api/workflow'
  import {Role} from '@/api/user'
  import waves from '@/directive/waves' // Waves directive
  import {parseTime, getNowFormatDate, isInArray, isRealObj, isRealArr} from '@/utils'
  import Pagination from '@/components/Pagination' // Secondary package based on el-pagination
  import formCreate from 'form-create/element'
  import {maker} from 'form-create/element'
  import {
    workorderStatusOptions,
    workorderExecStatusOptions,
    reviewOptions,
    feedbackOptions,
    auditRecordOptions
  } from '@/utils/dict'
  import {Db, DbInstance, DeployJob} from '@/api/mdb'
  import {requestSync} from '@/utils/requestSync'
  import vue from 'vue'

  import {handlerRoleUserU, handleSyntaxU, handleAuditUserU} from '@/utils/workflowutils'

  const statusKeyValue = workorderStatusOptions.reduce((acc, cur) => {
    acc[cur.key] = cur.display_name
    return acc
  }, {})
  const execStatusKeyValue = workorderExecStatusOptions.reduce((acc, cur) => {
    acc[cur.key] = cur.display_name
    return acc
  }, {})
  export default {
    name: 'workflow',
    components: {Pagination},
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
        emitNameList: ['dbenv'],
        uploadfile: true,
        downloadfile: false,
        file_info: [],
        fileList:[],
        approvalUserOptions: [{key: 1, display_name: '张三'}, {key: 2, display_name: '李四'}],
        total: 0,
        workorderId: '',
        currWorkflow: null,
        tableData: [],
        tableHeader: [],
        tableKey: 0,
        list: null,
        listQuery: {
          action: 'sent',
          page: 1,
          pagesize: 10,
          ordering: '-id',
          search: '',
        },
        listLoading: true,
        isShowAdvanced: false,
        feedbackTemp: {
          id: undefined,
          opinion: undefined,
          remark: undefined,
        },
        feedbackRules: {
          opinion: [{required: true, message: 'opinion is required', trigger: 'blur'}],
        },
        createTemp: {
          cur_user: undefined,
          cur_step: 1,
          cur_user_cname: ""
        },
        createRules: {
          cur_user: [{required: true, message: 'user is required', trigger: 'blur'}],
        },
        dialogFormVisible: false,
        dialogStatus: '',
        orderList: null,
        workflowgroupList: null,
        row: 4,
        workorderFields: {},
        formRule: [],
        option: {
          resetBtn: {
            show: false,
          },
          submitBtn: {
            show: false,
          },
        },
        stepList: [],
        hotWorkFlowList: null,
        userOptions: [],
        isShowNextUser: false,
        isShowHistory: false,
        workorderName: '',
        auditrecordList: [],
        feedbackOptions,
        stepActive: 1,
        curworkorder: undefined,
        isSyntax: 0,
        chickLoading: false,
        revokeDeployVisible: false,
        revokeId:'',

        isShowSql: false,
        cursetup: {},
        userList: [],
        dialogRoleFormVisible: false,
        createRules: {
          cur_user: [{required: true, message: 'user is required', trigger: 'blur'}],
        },
        mulselect: [],
      }
    },
    created() {
      this.init()
    },
    methods: {
      init() {
        this.getOrderList()
        this.getTableInfo()
      },
      getTableInfo() {
        Workorder.get_table_info().then(response => {
          if (response.hasOwnProperty("workflowgroups") && response.workflowgroups.length > 0) {
            this.dealGroup(response.workflowgroups)
          }
          if (response.hasOwnProperty("workflows") && response.workflows.length > 0) {
            this.hotWorkFlowList = response.workflows
          }
        })
      },
      dealGroup(wfgList) {
        var groupList = []
        var workflowgroupList = []
        for (var i = 0; i < wfgList.length; i++) {
          if (i != 0 && i % 4 == 0) {
            groupList.push(workflowgroupList)
            workflowgroupList = []
          }
          workflowgroupList.push(wfgList[i])
          if (i + 1 == wfgList.length) {
            groupList.push(workflowgroupList)
            workflowgroupList = []
          }
        }
        this.workflowgroupList = groupList
      },
      getOrderList() {
        Workorder.list(this.listQuery).then(response => {
          this.orderList = response.results
          this.total = response.count
        })
        setTimeout(() => {
          this.listLoading = false
        }, 1 * 1000)
      },
      handleFilter() {
        this.listQuery.page = 1
        this.getOrderList()
      },

      resetfileTemp() {
        this.file_info = []
      },
      resetTemp() {
        this.createTemp = {
          cur_user: undefined,
          cur_step: 1,
        }
        this.isShowNextUser = false
        this.feedbackTemp = {
          id: undefined,
          feedback: undefined,
          remark: undefined,
        }
        this.curworkorder = undefined
        this.isShowHistory = false
        this.isSyntax = 0
      },

      retFormAfterConfirm() {
        this.formRule = []
        this.stepList = []
      },

      handleCommand(item) {
        this.isShowSql = false
        this.resetTemp()
        this.resetfileTemp()
        this.isShowSql = false
        this.dialogStatus = "create"
        this.currWorkflow = item
        this.isShowNextUser = false
        this.uploadfile = true
        this.downloadfile = false
        this.userOptions = []
        this.stepActive = 1
        this.mulselect = []
        Workflow.formfields(item.id).then(response => {
          this.formRule = []
          for (var i = 0; i < response.length; i++) {
            var obj = response[i]
            if (obj.hasOwnProperty("is_active") && obj["is_active"]) {
              if (obj.props != undefined && obj.props != null && obj.props != "") {
                try {
                  obj.props = JSON.parse(obj.props)
                } catch (e) {
                  obj.props = null
                }
              } else {
                obj.props = null
              }
              if (obj.validate != undefined && obj.validate != null && obj.validate != "") {
                try {
                  obj.validate = JSON.parse(obj.validate)
                } catch (e) {
                  obj.validate = null
                }
              } else {
                obj.validate = null
              }
              if (obj.options != undefined && obj.options != null && obj.options != "") {
                try {
                  obj.options = JSON.parse(obj.options)
                } catch (e) {
                  obj.options = null
                }
              } else {
                obj.options = null
              }

              if (isInArray(this.emitNameList, obj.field)) {
                obj.emit = ['change']
              }

              if (obj.type == "select" && obj.dicurl != null && obj.dicurl != "") {
                var ret = requestSync.deal(obj.dicurl, {}, "GET", 5000);
                if (ret != null) {
                  obj.options = ret
                }
              } else if (obj.type == "cascader" && obj.dicurl != null && obj.dicurl != "") {
                var ret = requestSync.deal(obj.dicurl, {}, "GET", 5000);
                if (ret != null) {
                  obj.props = {}
                  obj.props["options"] = ret
                }
              }
              this.formRule.push(obj)
            }
          }

          this.dialogFormVisible = true
          // for (var h = 0; h < this.mulselect.length; h++) {
          //   this.$refs.waitingForm.searchForm[this.mulselect[h]] = []
          // }

        })
        Workflow.steps(item.id).then(response => {
          if (response == null || response == undefined || response.length <= 0) {
            this.stepList = []
          } else {
            this.stepList = response
            var obj = {}
            obj.id = -1
            obj.cname = "申请人"
            var objtmp = {}
            objtmp.id = -1
            objtmp.role = obj
            this.stepList.push(objtmp)
            this.stepList.unshift(objtmp)
            this.userOptions = response[1].role.users
            this.cursetup = response[1]
            this.isShowNextUser = true
          }
        })
        this.workorderName = item.cname + "工单"

        if (this.currWorkflow != null && this.currWorkflow.name.indexOf('dbsql_') >= 0) {
          this.isShowSql = true
        }
      },
      handleData(type) {
        if (type == "create") {
          this.createData()
        } else {
          this.feedbackData()
        }
      },
      createData() {
        this.workorderFields.validate(() => {
          if (!this.checkCumRules()) {
            return
          }
          var params = {}
          params.workflow = this.currWorkflow.id
          params.data = JSON.stringify(this.workorderFields.formData())
          console.log("------>",params.data)
          console.log("-3333----->",params.data)
          params.cur_user = this.createTemp.cur_user
          params.file_info = JSON.stringify(this.file_info)
          var formruls = this.formRule
          var data = this.workorderFields.formData()
          for (var i = 0; i < formruls.length; i++) {
            if (formruls[i].type == 'select') {
              var options = []
              for (var j = 0; j < formruls[i].options.length; j++) {
                if (formruls[i].options[j].value == data[formruls[i].field]) {
                  options.push(formruls[i].options[j])
                  break
                }
              }
              if (options.length != 0) {
                formruls[i].options = options
              }
            }
          }
          params.formfields = JSON.stringify(this.formRule)
          this.chickLoading = true
          Workorder.create(params).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.chickLoading = false
            this.getOrderList()
            this.retFormAfterConfirm()
          })
          setTimeout(() => {
            this.chickLoading = false
          }, 3000)
        })
      },

      checkCumRules() {
        if ((this.cursetup.role_type == "dynamic" || isRealArr(this.stepList)) && !isRealObj(this.createTemp.cur_user)) {
          this.$notify({
            title: '失败',
            message: '请选择下一个审批人!',
            type: 'error',
            duration: 2000
          })
          return false
        }

        if (this.currWorkflow.name.indexOf("dbsql_") >= 0) {
          if (this.isSyntax == 0) {
            this.$notify({
              title: '失败',
              message: '请检查sql语法!',
              type: 'error',
              duration: 2000
            })
            return false
          }
        }
        return true
      },

      feedbackData() {
        this.$refs['feedbackDataForm'].validate((valid) => {
          if (valid) {
            const tempData = Object.assign({}, this.feedbackTemp)
            this.chickLoading = true
            Workorder.feedback(tempData.id, tempData).then(() => {
              this.dialogFormVisible = false
              this.$notify({
                title: '成功',
                message: '更新成功',
                type: 'success',
                duration: 2000
              })
              this.chickLoading = false
              this.getOrderList()
            })
            setTimeout(() => {
              this.chickLoading = false
            }, 2 * 1000)
          }
        })
      },
      handleDetail(row) {
        this.isShowSql = false
        this.resetTemp()
        this.isShowHistory = true
        this.createTemp.cur_step = row.cur_step
        this.curworkorder = row
        this.workorderName = row.cname + "工单"
        this.dialogStatus = 'detail'
        this.stepActive=0
        Workorder.get(row.id).then(response => {
          var jsonData = JSON.parse(response.data)
          this.file_info = JSON.parse(response.file_info)
          if (this.file_info == null){
             this.file_info = []
           }
          var jsonFormfields = JSON.parse(response.formfields)
          var jsonSteps = JSON.parse(response.steps)
          if (jsonSteps == null || jsonSteps == undefined || jsonSteps.length <= 0) {
            this.stepList = []
          } else {
            this.stepList = jsonSteps
            var obj = {}
            obj.id = -1
            obj.cname = "申请人"
            var objtmp = {}
            objtmp.id = -1
            objtmp.role = obj

            if (row.cur_step == null) {
              this.stepActive = this.stepList.length + 2
            } else {
              for (var j = 0; j < this.stepList.length; j++) {
                if (this.stepList[j].id == row.cur_step) {
                  break
                }
                this.stepActive++
              }
              this.stepActive++
            }

            this.stepList.push(objtmp)
            this.stepList.unshift(objtmp)
          }
          for (var i = 0; i < jsonFormfields.length; i++) {
            var obj = jsonFormfields[i]
            if (obj.props == null || obj.props == undefined || obj.props == "") {
              obj.props = {"disabled": true}
            } else {
              obj.props.disabled = true
            }
          }
          this.formRule = jsonFormfields
          this.workorderFields = jsonData
          this.curworkorder = response
        })
        this.getAuditRecordList(row.id)
        this.uploadfile = false
        this.downloadfile = true
        this.dialogFormVisible = true
      },

      getAuditRecordList(id) {
        Workorder.auditrecord(id).then(response => {
          this.auditrecordList = []
          for (var i = 0; i < response.length; i++) {
            var obj = response[i]
            if (isRealObj(obj.remark))
              obj.remark = obj.remark.replace(/\n|\r\n/g, "<br/>")
            else {
              obj.remark = ''
            }
            this.auditrecordList.push(obj)
          }
        })
      },

      handleFeedBack(row) {
        if (row['status'] == 5){
          this.$message({
            title: 'error',
            message: '工单状态已结束,无法执行撤回操作',
            type: 'error',
            duration: 3000
          })
          return
        }
        this.resetTemp()
        this.createTemp.cur_step = row.cur_step
        this.workorderName = row.cname + "工单"
        this.dialogStatus = 'feedback'
        this.feedbackTemp.id = row.id
        this.isShowHistory = true
        this.curworkorder = row

        Workorder.get(row.id).then(response => {
          var jsonData = JSON.parse(response.data)
          var jsonFormfields = JSON.parse(response.formfields)
          var jsonSteps = JSON.parse(response.steps)
          if (jsonSteps == null || jsonSteps == undefined || jsonSteps.length <= 0) {
            this.stepList = []
          } else {
            this.stepList = jsonSteps
            var obj = {}
            obj.id = -1
            obj.cname = "申请人"
            var objtmp = {}
            objtmp.id = -1
            objtmp.role = obj
            if (row.cur_step == null) {
              this.stepActive = this.stepList.length + 2
            } else {
              for (var j = 0; j < this.stepList.length; j++) {
                if (this.stepList[j].id == row.cur_step) {
                  num = j
                  break
                }
                this.stepActive++
              }
              this.stepActive++
            }
            this.stepList.push(objtmp)
            this.stepList.unshift(objtmp)
          }
          for (var i = 0; i < jsonFormfields.length; i++) {
            var obj = jsonFormfields[i]
            if (obj.props == null || obj.props == undefined || obj.props == "") {
              obj.props = {"disabled": true}
            } else {
              obj.props.disabled = true
            }
          }
          this.formRule = jsonFormfields
          this.workorderFields = jsonData
        })
        this.getAuditRecordList(row.id)
        this.dialogFormVisible = true
      },

      handleRevoke(row) {
        this.revokeDeployVisible = true
        this.revokeId = row.id
      },

      Revoke() {
        var params = {}
        params.id = this.revokeId
        params.opinion = 10
        Workorder.revoke(params.id,params).then(response => {
          this.revokeDeployVisible = false
          if (response['opinion'] == 1){
              this.$notify({
              title: '失败',
              message: '当前工单状态无法撤回',
              type: 'error',
              duration: 2000
            })
          }else{
              this.$notify({
              title: '成功',
              message: '撤回成功',
              type: 'success',
              duration: 2000
            })
          }

          this.getOrderList()
        })
        setTimeout(() => {
          this.chickLoading = false
        }, 2 * 1000)
      },

      handleDbEnv(checked) {
        var params = {}
        params.env = checked
        DbInstance.list(params).then(response => {
          var list = response.results
          for (var i = 0; i < this.formRule.length; i++) {
            for (var key in this.formRule[i]) {
              if (this.formRule[i][key] == "dbinstances") {
                var optionList = []
                for (var k = 0; k < list.length; k++) {
                  var option = {}
                  option.value = list[k].id
                  option.label = list[k].host + ":" + list[k].port + "-" + list[k].name
                  option.disabled = false
                  optionList.push(option)
                }
                this.formRule[i].options = optionList
              }
            }
          }
        })
      },

      handleSyntax() {
        handleSyntaxU(this, DeployJob, 0)
      },

      handleAuditUser() {
        handleAuditUserU(this)
      },
      //动态获取审批用户
      handlerRoleUser() {
        this.userList = []
        handlerRoleUserU(this)
      },

      onsuccess(res) {
        console.log(res);
        this.file_info.push(res);
      },

    },
  }
</script>
<style scoped>
  .el-dropdown {
    vertical-align: top;
    margin-left: 10px
  }

  .el-dropdown + .el-dropdown {
    margin-left: 5%
  }

  .el-icon-arrow-down {
    font-size: 12px;
  }

  .el-btn {
    width: 130px;
    height: 35px
  }
</style>
<style scoped>
  .el-dialog__body {
    padding: 10px 20px;
    color: #606266;
    font-size: 14px;
  }

  .warn-content a {
    color: #42b983;
    font-weight: 600
  }

  .expandwo {
    width: 100%;
    height: 100%;
    overflow: hidden;
  }

  .expandwo > div {
    height: 100%;
    width: 100%;
    overflow-y: auto;
  }

  .expandwo > div::-webkit-scrollbar-track {
    box-shadow: inset 0 0 6px rgba(0, 0, 0, .3);
    border-radius: 5px;
  }

  .expandwo > div::-webkit-scrollbar-thumb {
    background-color: rgba(50, 65, 87, 0.5);
    outline: 1px solid slategrey;
    border-radius: 5px;
  }

  .expandwo > div::-webkit-scrollbar {
    width: 10px;
  }

  #workflowleft {
    width: 70%;
    float: left;
    margin-top: 5px;
    border-right: 1px solid #eeefff;
  }

  #workflowright {
    width: 30%;
    margin-top: 5px;
    margin-left: 10px;
    height: 100%
  }

  .el-step.is-simple .el-step__title {
    font-size: 14px;
    line-height: 20px;
  }

  .customWidthwo {
    width: 60%;
  }
</style>
