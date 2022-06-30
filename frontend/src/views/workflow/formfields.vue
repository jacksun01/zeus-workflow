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

      <el-table-column type="expand">
        <template slot-scope="scope">
          <el-form label-position="left" inline class="demo-table-expand">
            <el-form-item :label="$t('workflow_formfields.title')">
              <span>{{ scope.row.title }}</span>
            </el-form-item>
            <el-form-item :label="$t('workflow_formfields.type')">
              <span>{{ scope.row.type|fieldTypeFilter }}</span>
            </el-form-item>
            <el-form-item :label="$t('workflow_formfields.field')">
              <span>{{ scope.row.field}}</span>
            </el-form-item>
            <el-form-item :label="$t('workflow_formfields.value')">
              <span>{{ scope.row.value }}</span>
            </el-form-item>
            <el-form-item :label="$t('workflow_formfields.dicurl')">
              <span>{{ scope.row.dicurl }}</span>
            </el-form-item>
            <el-form-item :label="$t('workflow_formfields.props')">
              <span>{{ scope.row.props }}</span>
            </el-form-item>
            <el-form-item :label="$t('workflow_formfields.validate')">
              <span>{{scope.row.validate|isValidateRequiredFilter }}</span>
            </el-form-item>
            <el-form-item :label="$t('workflow_formfields.options')">
              <span>{{ scope.row.options }}</span>
            </el-form-item>
            <el-form-item :label="$t('table.is_active')">
              <span>{{ scope.row.is_active|isActiveFilter }}</span>
            </el-form-item>
          </el-form>
        </template>
      </el-table-column>

      <el-table-column :label="$t('workflow_formfields.title')">
        <template slot-scope="scope">
          <span class="link-type" @click="handleDetail(scope.row)">{{ scope.row.title }}</span>
        </template>
      </el-table-column>

      <el-table-column :label="$t('workflow_formfields.type')">
        <template slot-scope="scope">
          <span>{{ scope.row.type|fieldTypeFilter }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('workflow_formfields.field')">
        <template slot-scope="scope">
          <span>{{ scope.row.field }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('workflow_formfields.props')">
        <template slot-scope="scope">
          <span>{{ scope.row.props }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('workflow_formfields.validate')">
        <template slot-scope="scope">
          <span>{{ scope.row.validate|isValidateRequiredFilter }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('workflow_formfields.options')">
        <template slot-scope="scope">
          <span>{{ scope.row.options }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('table.is_active')">
        <template slot-scope="scope">
          <span>{{ scope.row.is_active|isActiveFilter }}</span>
        </template>
      </el-table-column>
      <el-table-column :label="$t('table.actions')" class-name="small-padding fixed-width" fixed="right"
                       label="操作"
                       width="240">
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
        <el-form-item :label="$t('workflow_formfields.demo')" prop="demoid">
          <el-select v-model="demoid" filterable clearable @change="handleDemoSelect">
            <el-option v-for="item in demoOptions" :key="item.id" :value="item.id"
                       :label="'name:'+item.title+' type:'+item.type"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item :label="$t('table.title')" prop="title">
          <el-input v-model="temp.title"/>
        </el-form-item>
        <el-form-item :label="$t('workflow_formfields.type')" prop="type">
          <el-select v-model="temp.type" filterable>
            <el-option v-for="item in fieldTypeOptions" :key="item.key" :value="item.key"
                       :label="item.display_name"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item :label="$t('workflow_formfields.field')" prop="field">
          <el-input v-model="temp.field"/>
        </el-form-item>
        <el-form-item :label="$t('workflow_formfields.value')" prop="value">
          <el-input v-model="temp.value"/>
        </el-form-item>
        <el-form-item :label="$t('workflow_formfields.props')" prop="props">
          <el-input :autosize="{ minRows: 3, maxRows: 5}" v-model="temp.props" type="textarea"
                    placeholder='input props  for example: {"type": "text"}'/>
          <a href="http://www.form-create.com/components/element/input.html" target="_blank" class="link-type">规则文档</a>
        </el-form-item>

        <el-form-item :label="$t('workflow_formfields.validate_required')" prop="validate_required">
          <el-switch
            v-model="temp.validate_required"
            class="switchinner"
            active-color="#00A854"
            active-text="ON"
            inactive-color="#F04134"
            inactive-text="OFF"
          />
        </el-form-item>

        <el-form-item :label="$t('workflow_formfields.dicurl')" prop="dicurl">
          <el-input v-model="temp.dicurl"/>
        </el-form-item>

        <el-form-item :label="$t('workflow_formfields.options')" prop="options">
          <el-input :autosize="{ minRows: 3, maxRows: 5}" v-model="temp.options" type="textarea"
                    placeholder='input options  for example: [{"value": "104", "label": "生态蔬菜", "disabled": false}]'/>
        </el-form-item>
        <el-form-item :label="$t('table.is_active')" prop="is_active">
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

  </div>
</template>

<script>
  import {Workflow, Formfields as masterApi} from '@/api/workflow'
  import waves from '@/directive/waves' // Waves directive
  import {parseTime, getNowFormatDate, isRealObj} from '@/utils'
  import {isvalidEnName} from '@/utils/validate'
  import {fieldTypeOptions, isActiveOptions, selectOptions,requiredOptions} from '@/utils/dict'

  const fieldTypeKeyValue = fieldTypeOptions.reduce((acc, cur) => {
    acc[cur.key] = cur.display_name
    return acc
  }, {})

  const isActiveKeyVale = isActiveOptions.reduce((acc, cur) => {
    acc[cur.key] = cur.display_name
    return acc
  }, {})


  export default {
    name: 'workflow_formfields',
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
      fieldTypeFilter(type) {
        return fieldTypeKeyValue[type]
      },
      isActiveFilter(type) {
        return isActiveKeyVale[type]
      },
      isValidateRequiredFilter(value) {
        if (value != null && value != undefined && value != "" && value.indexOf("trigger") >= 0) {
          return "必填"
        } else {
          return "非必填"
        }
      },

    },
    data() {
      const validateEnName = (rule, value, callback) => {
        if (!isvalidEnName(value)) {
          callback(new Error('Please name should contain only A-Za-z or _'))
        } else {
          callback()
        }
      }
      return {
        demoOptions: [],
        demoid: undefined,
        fieldTypeOptions,
        selectOptions,
        isActiveKeyVale,
        requiredOptions,
        tableKey: 0,
        list: null,
        total: 0,
        listLoading: true,
        workflowname: this.$route.query.workflowname,
        workflowid: this.$route.query.workflowid,
        listQuery: {
          page: 1,
          pagesize: 10,
          name: undefined,
          ordering: '-id',
          search: ''
        },
        temp: {
          remark: undefined,
          type: undefined,
          field: undefined,
          title: undefined,
          value: undefined,
          props: undefined,
          validate: undefined,
          validate_required: false,
          dicurl: undefined,
          options: undefined,
          is_active: undefined,
          workflow: undefined,
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
          type: [{required: true, message: 'type is required', trigger: 'blur'}],
          field: [{required: true, trigger: 'blur', validator: validateEnName}],
          title: [{required: true, message: 'title is required', trigger: 'blur'}],
        },
        downloadLoading: false,
        isShowCustom: true,
        formfieldid: undefined,
      }
    },
    created() {
      this.getList()
    },
    methods: {
      getList() {
        Workflow.formfields(this.workflowid).then(response => {
          var data_list=[]
          for(var i=0;i<response.length;i++){
            var obj=response[i]
            if(obj.hasOwnProperty("validate")&&isRealObj(obj["validate"])){
              obj["validate_required"]=true
            }else{
              obj["validate_required"]=false
            }
            data_list.push(obj)
          }
          this.list = data_list
        })
        setTimeout(() => {
          this.listLoading = false
        }, 1 * 1000)
      },
      handleFilter() {
        this.listQuery.page = 1
        this.getList()
      },
      handleDemoSelect() {
        this.resetTemp()
        for (var i = 0; i < this.demoOptions.length; i++) {
          if (this.demoOptions[i].id == this.demoid) {
            this.temp = Object.assign({}, this.demoOptions[i])
            break
          }
        }
      },
      getDemoformfields() {
        Workflow.getDemoformfields().then(response => {
          var data_list=[]
          for(var i=0;i<response.length;i++){
            var obj=response[i]
            if(obj.hasOwnProperty("validate")&&isRealObj(obj["validate"])){
              obj["validate_required"]=true
            }else{
              obj["validate_required"]=false
            }
            data_list.push(obj)
          }
          this.demoOptions = data_list
        })
      },
      resetTemp() {
        this.temp = {
          remark: undefined,
          type: undefined,
          field: undefined,
          title: undefined,
          value: undefined,
          props: undefined,
          validate: undefined,
          validate_required: false,
          dicurl: undefined,
          options: undefined,
          is_active: true,
          workflow: undefined,
        }
      },
      handleCreate() {
        this.demoid = undefined
        this.demoOptions = []
        this.resetTemp()
        this.getDemoformfields()
        this.dialogStatus = 'create'
        this.dialogFormVisible = true
        this.$nextTick(() => {
          this.$refs['dataForm'].clearValidate()
        })
      },
      createData() {
        this.$refs['dataForm'].validate((valid) => {
          if (valid) {
            this.temp.workflow = this.workflowid
            if (!this.chechJson(this.temp.props, "属性规则") || !this.chechJson(this.temp.options, "选项数据")) {
              return false
            }
            if (this.temp.props == "" || this.temp.props == undefined || this.temp.props == null) {
              this.temp.props = undefined
            }
            if (this.temp.validate == "" || this.temp.validate == undefined || this.temp.validate == null) {
              this.temp.validate = undefined
            }
            if (this.temp.options == "") {
              this.temp.options = undefined
            }

            if (this.temp.validate_required) {
              this.temp.validate = JSON.stringify([{
                "required": true,
                "message": this.temp.title + " is required!",
                "trigger": true
              }])
            } else {
              this.temp.validate = undefined
            }

            if (!this.checkType(this.temp)) {
              return
            }

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

      checkType(obj) {
        if (obj.type == "radio" || obj.type == "checkbox") {
          if (obj.options == undefined) {
            this.$notify({
              title: '失败',
              message: '选项数据必填',
              type: 'error',
              duration: 2000
            })
            return false
          }
        } else if (obj.type == "select") {
          if (!isRealObj(this.temp.dicurl) && !isRealObj(obj.options)) {
            this.$notify({
              title: '失败',
              message: '选项数据/接口 选其一 必填',
              type: 'error',
              duration: 2000
            })
            return false
          }
        }

        return true
      },

      chechJson(obj, str) {
        if (obj != "" && obj != undefined && obj != null) {
          try {
            var objJson = JSON.parse(obj)
          } catch (e) {
            this.$notify({
              title: '失败',
              message: str + '必须是json字符串',
              type: 'error',
              duration: 2000
            })
            return false
          }
        }
        return true
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
        this.resetTemp()
        this.demoid = undefined
        this.formfieldid = row.id
        this.temp = Object.assign({}, row) // copy obj
        this.getDemoformfields()
        this.dialogStatus = 'update'
        this.dialogFormVisible = true
        this.$nextTick(() => {
          this.$refs['dataForm'].clearValidate()
        })

      },
      updateData() {
        this.$refs['dataForm'].validate((valid) => {
          if (valid) {
            this.temp.workflow = this.workflowid
            if (!this.chechJson(this.temp.props, "属性规则") || !this.chechJson(this.temp.options, "选项数据")) {
              return false
            }
            var validate = undefined
            if (this.temp.validate_required) {
              this.temp.validate = JSON.stringify([{
                "required": true,
                "message": this.temp.title + " is required!",
                "trigger": true
              }])
            } else {
              this.temp.validate = ''
            }

            const tempData = Object.assign({}, this.temp)

            if (!this.checkType(this.temp)) {
              return
            }
            if (tempData.hasOwnProperty("order_num")) {
              delete tempData.order_num
            }
            masterApi.update(this.formfieldid, tempData).then(() => {
              for (const v of this.list) {
                if (v.id === this.temp.id) {
                  const index = this.list.indexOf(v)
                  this.list.splice(index, 1, this.temp)
                  break
                }
              }
              this.dialogFormVisible = false
              this.$notify({
                title: '成功',
                message: '更新成功',
                type: 'success',
                duration: 2000
              })
              this.getList()
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
<style>
  .demo-table-expand {
    font-size: 0;
  }

  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }

  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>
