<template>
  <!--author Jack qq:774428957-->
  <div class="app-container">
     <reviewTable
      :list="supList"
      :listQuery="supListQuery"
      :tabletitle="supTableTitle"
      :total="supTotal"
      @handleReview="handleReview"
      @handleDetail="handleDetail"
      @handleFilter="handleFilter"
      @getList="getSupList"
    />
    <el-dialog :title="workorderName" :visible.sync="dialogFormVisible"  width="85%"  :close-on-click-modal='false'>
      <el-steps finish-status="success" simple style="margin-left: 10px; height: 30px;margin-top: 5px"
                :active="stepActive">
        <el-step v-for=" (step,index) in stepList" :title="step.role.cname" :key="index"
                 style="font-size: 10px;"></el-step>
      </el-steps>

      <el-alert
        style="height: 30px;margin-left: 10px;width: 98.5%;margin-top: 15px"
        title="申请人"
        type="info"
        :closable="false">
      </el-alert>
      <div style="margin-left: 20px;padding: 10px">
        <strong>申请人：</strong><span>{{creator.username}}</span><strong style="margin-left: 50px">中文名：</strong><span> {{creator.cname}}</span><strong
        style="margin-left: 50px">Email：</strong><span>{{creator.email}}</span>
      </div>

      <el-alert
        style="height: 30px;margin-left: 10px;width: 98.5%;margin-top: 5px"
        title="工单内容"
        type="info"
        :closable="false">
      </el-alert>
      <form-create ref="waitingForm" v-model="workorderFields" :rule="formRule" :option="option"
                   class="el-form el-form--label-left form-creat"
                   label-position="left" label-width="100px"
                   style="width: 80%; margin-left:25px;padding: 10px"></form-create>
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
        title="审批"
        type="info"
        :closable="false" v-show="dialogStatus!='detail'">
      </el-alert>
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="120px"
               style="width: 90%; margin-left:20px;margin-top: 10px" v-show="dialogStatus!='detail'">
        <el-form-item :label="$t('table.review')" prop="opinion">
          <el-select v-model="temp.opinion" filterable style="width: 83%!important; margin-left: 15px" @change="handleChange">
            <el-option v-for="item in reviewROptions" :key="item.key" :value="item.key"
                       :label="item.display_name"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item :label="$t('table.reviewRemark')" prop="remark">
          <el-input :autosize="{ minRows: 2, maxRows: 4}" v-model="temp.remark" type="textarea"
                    placeholder="input remark" style="width: 83%; margin-left: 15px"/>
        </el-form-item>
        <el-form-item :label="$t('table.nextreviewer')" prop="next_user" v-if="isShowNextUser&& isShow"  style="width: 85.5%!important;">
          <el-select v-model="temp.next_user" filterable style="width: 83%; margin-left: 15px">
            <el-option v-for="item in userOptions" :key="item.id" :value="item.id" :label="item.username"></el-option>
          </el-select>
        </el-form-item>
      </el-form>

      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false" size="mini">{{ $t('table.cancel') }}</el-button>
        <el-button v-show="dialogStatus!='detail'" type="primary"
                   @click="reviewData()" size="mini" :loading="reviewLoading">{{ $t('table.confirm')
          }}
        </el-button>
        <el-button v-show="isShowSql" type="primary"
                         @click="handleSyntax()" size="mini">{{ $t('mdb_sqljob.checkSyntax')}}
              </el-button>
      </div>
      <el-alert
        style="height: 30px;margin-left: 10px;width: 98.5%"
        title="审批历史"
        type="info"
        :closable="false">
      </el-alert>
      <div style="margin-left: 15px;width: 90%">
        <div v-for="auditrecord in auditrecordList" style="margin-top: 5px">
          [{{auditrecord.create_time}}]&nbsp;<span
          v-if="auditrecord.role_detail!=undefined&&auditrecord.role_detail!=null">{{auditrecord.role_detail.cname}}</span>:{{auditrecord.user_detail.username}}({{auditrecord.opinion|reviewFilter}})
          <div v-html="auditrecord.remark" style="margin-top:3px;margin-left:20px;font-size: smaller"/>
        </div>
      </div>
    </el-dialog>
  </div>
</template>

<script>
  import {Workorder, Workflow} from '@/api/workflow'
  import {DeployJob} from '@/api/mdb'
  import {Role} from '@/api/user'
  import waves from '@/directive/waves' // Waves directive
  import {parseTime, getNowFormatDate} from '@/utils'
  import Pagination from '@/components/Pagination' // Secondary package based on el-pagination
  import formCreate from 'form-create/element'
  import {maker} from 'form-create/element'
  import {
    workorderStatusOptions,
    workorderExecStatusOptions,
    reviewOptions,
    reviewLOptions,
    reviewAOptions,
    feedbackOptions,
    auditRecordOptions
  } from '@/utils/dict'
  import {handleReviewU,handleDetailU,handleSyntaxU,getAuditRecordListU,reviewDataU,handleChangeU,resetTempU,handleFilterU} from '@/utils/workflowutils'
import {reviewTable} from './components'
  const statusKeyValue = workorderStatusOptions.reduce((acc, cur) => {
    acc[cur.key] = cur.display_name
    return acc
  }, {})
  const execStatusKeyValue = workorderExecStatusOptions.reduce((acc, cur) => {
    acc[cur.key] = cur.display_name
    return acc
  }, {})
  export default {
    name: 'workorder_sup',
    components: {Pagination,reviewTable},
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
      const validateNextuser = (rule, value, callback) => {
        if (this.temp.status != 3 && (value == undefined || value == null || value == "")) {
          callback(new Error('next_user is required'))
        } else {
          callback()
        }
      }
      const validateRemark = (rule, value, callback) => {
        if (this.temp.opinion == 0 && (value == undefined || value == null || value == "")) {
          callback(new Error('remark is required'))
        } else {
          callback()
        }
      }
      return {
        isShow: true,
        workorderFields: {},
        userOptions: [],
        reviewOptions,
        reviewLOptions,
        reviewAOptions,
        reviewROptions: [],

        loading: true,

        supList: [],
        supListQuery: {
          page: 1,
          pagesize: 50,
          ordering: '-id',
          search: '',
          action: 'supervise',
        },
        supTableTitle:"督办工单",
        supTotal:0,

        temp: {
          next_user: undefined,
          remark: "",
          opinion: undefined,
          id: undefined,
          curstep: undefined,
          status: undefined,
        },
        dialogFormVisible: false,
        delVisible: false,
        dialogStatus: '',
        textMap: {
          update: 'Edit',
          create: 'Create',
          delete: 'Delete'
        },
        rules: {
          opinion: [{required: true, message: 'opinion is required', trigger: 'blur'}],
          remark: [{required: false, trigger: blur, validator: validateRemark}],
          next_user: [{required: true, trigger: blur, validator: validateNextuser}],
        },
        reviewLoading: false,
        formRule: [],
        option: {
          form: {
            //是否开启行内表单模式
            inline: false,
            //表单域标签的位置，可选值为 left、right、top
            labelPosition: 'left',
            //表单域标签的宽度，所有的 FormItem 都会继承 Form 组件的 label-width 的值
            labelWidth: "120px",
            //是否显示校验错误信息
            showMessage: true,
            //原生的 autocomplete 属性，可选值为 off 或 on
            autocomplete: 'off',
          },
          resetBtn: {
            show: false,
          },
          submitBtn: {
            show: false,
          },
        },
        stepList: [],
        workorderName: '',
        stepActive: 0,
        auditrecordList: [],
        workflowName: '',
        isShowNextUser: false,
        isShowBackNextUser: false,
        creator: {},
        curworkorder: {},
        isShowSql:false,
      }
    },
    created() {
      this.init()
    },
    methods: {
      init() {
        this.getSupList()
      },
      getSupList() {
        Workorder.list(this.supListQuery).then(response => {
          this.supList = response.results
          this.supTotal = response.count
        })
        setTimeout(() => {
          this.loading = false
        }, 1 * 1000)
      },
      handleFilter(search,action) {
        handleFilterU(this,search,action)
      },
      resetTemp() {
        resetTempU(this)
      },
      handleReview(row) {
        this.isShowSql=false
        handleReviewU(this,row,Workorder)
      },
      reviewData() {
        reviewDataU(this,Workorder,1)
      },
      handleChange(value) {
        handleChangeU(this,value)
      },
      getAuditRecordList(id) {
        getAuditRecordListU(this,Workorder,id)
      },
      handleDetail(row) {
        handleDetailU(this,row,Workorder)
      },
      handleSyntax() {
        handleSyntaxU(this,DeployJob,1)
      },
    }
  }
</script>
<style>
    .el-textarea.is-disabled .el-textarea__inner {
    background-color: #f5f7fa;
     border-color: #e4e7ed;
     color: #da0f1c;
    cursor: not-allowed;
}

  .el-input.is-disabled .el-input__inner {
    background-color: #f5f7fa;
    border-color: #e4e7ed;
     color: #da0f1c;
    cursor: not-allowed;
  }

  .el-radio__input.is-disabled + span.el-radio__label {
     color: #da0f1c;
    cursor: not-allowed;
  }
  .el-checkbox__input.is-disabled+span.el-checkbox__label {
    color: #da0f1c;
    cursor: not-allowed;
}
.el-checkbox__input.is-disabled.is-checked .el-checkbox__inner {
    background-color: #F2F6FC;
    /* border-color: #DCDFE6; */
}
  .el-tag--info, .el-tag--info .el-tag__close {
     color: #da0f1c;
}

</style>
