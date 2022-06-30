import {isRealObj} from "./index";

const requestsync = require('./requestSync')
const indexRed = require('./index')

export function handleAuditUserU(that) {
  for (var i = 0; i < that.userList.length; i++) {
    if (that.userList[i].id == that.createTemp.cur_user) {
      that.createTemp.cur_user_cname = that.userList[i].cname
      that.dialogRoleFormVisible = false
      break
    }
  }
}

//动态获取审批用户
export function handlerRoleUserU(that) {
  that.userList = []
  //静态
  if (that.cursetup.role_type == "dynamic") {
    var specialFiledList = []
    var queryParams = ""
    var url = that.cursetup.url
    if (that.cursetup.url.indexOf("?") > 0) {
      url = that.cursetup.url.substring(0, that.cursetup.url.indexOf("?"))
      var urlParams = that.cursetup.url.substring(that.cursetup.url.indexOf("?") + 1, that.cursetup.url.length)
      if (urlParams.indexOf("special=") >= 0) {
        var urlParamsArr = urlParams.split("&")
        for (var i = 0; i < urlParamsArr.length; i++) {
          const reg = /^special/
          if (reg.test(urlParamsArr[i])) {
            var strTmp = urlParamsArr[i].substring(urlParamsArr[i].indexOf("=") + 1, urlParamsArr[i].length)
            specialFiledList = strTmp.split(",")
          } else {
            if (queryParams == "") {
              queryParams = urlParamsArr[i]
            } else {
              queryParams = queryParams + "&" + urlParamsArr[i]
            }
          }
        }
        //特殊参数 拼接url
        if (specialFiledList.length > 0) {
          var params = that.workorderFields.formData()
          for (var i = 0; i < specialFiledList.length; i++) {
            if (params.hasOwnProperty(specialFiledList[i])) {
              if (params[specialFiledList[i]] != null && params[specialFiledList[i]] != "") {
                if (queryParams == "") {
                  queryParams = specialFiledList[i] + "=" + params[specialFiledList[i]]
                } else {
                  queryParams = queryParams + "&" + specialFiledList[i] + "=" + params[specialFiledList[i]]
                }
              }
            }
          }
        }
      }
    }
    if (queryParams != "") {
      url = url + "?" + queryParams
    }
    var ret = requestsync.requestSync.deal(url, {}, "GET");
    that.userList = ret
  } else {
    that.userList = that.cursetup.role.users
  }
  if (that.userList != null) {
    that.dialogRoleFormVisible = true
  }
}

//sql语法检查
export function handleSyntaxU(that, masterApi, flag) {
  var params = that.workorderFields.formData()
  if (flag == 0) {
    if (params.db == null || params.db.length == 0) {
      that.$notify({
        title: 'error',
        message: '请选择数据库',
        type: 'error',
        duration: 2000
      })
      return
    }
    if (params.sql == null || params.sql == "") {
      that.$notify({
        title: 'error',
        message: '请编写sql语句',
        type: 'error',
        duration: 2000
      })
      return
    }
    if (params.sql_type == null || params.sql_type == "") {
      that.$notify({
        title: 'error',
        message: '请选择sql类型语句',
        type: 'error',
        duration: 2000
      })
      return
    }
  }
  if (params.db instanceof Array) {
    params.db = params.db[2]
  }

  masterApi.sql_syntax_check(params).then(response => {
    that.isSyntax = 1
    that.$message({
      title: '成功',
      message: "影响行：" + response.affected_rows + " 通过",
      type: 'success',
      duration: 2000
    })
  })
}

export function handleReviewU(that, row,api) {
  that.resetTemp()
  that.isShowSql = false
  that.temp.id = row.id
  that.workorderName = row.cname + "工单"
  that.temp.status = row.status
  that.creator = row.creator_detail
  that.curworkorder = row
  api.get(row.id).then(response => {
    if (response.steps == null || response.steps == "") {
      that.stepList = []
    } else {
      var rowStepJson = JSON.parse(response.steps)
      that.stepList = rowStepJson
      var obj = {}
      obj.id = -1
      obj.cname = "申请人"
      var objtmp = {}
      objtmp.id = -1
      objtmp.role = obj
      var num = 0
      if (row.cur_step == null) {
        that.stepActive = that.stepList.length + 2
      } else {
        for (var j = 0; j < that.stepList.length; j++) {
          if (that.stepList[j].id == row.cur_step) {
            num = j
            break
          }
          that.stepActive++
        }
        that.stepActive++
      }
      if (that.stepList != null && that.stepList != undefined && that.stepList.length >= 1 && row.cur_step != that.stepList[that.stepList.length - 1].id) {

        that.isShowNextUser = true
        that.isShowBackNextUser = that.isShowNextUser
        that.reviewROptions = that.reviewOptions
        //动态
        console.log(that.stepList[num + 1])
        if (indexRed.isRealObj(that.stepList[num + 1]) && that.stepList[num + 1].hasOwnProperty("role_type") && indexRed.isRealObj(that.stepList[num + 1].role_type) && that.stepList[num + 1].role_type == "dynamic") {
          var ret = requestsync.requestSync.deal(that.stepList[num + 1].url, {}, "GET");
          that.userOptions = ret
        } else {
          if (that.stepList[num + 1].hasOwnProperty("role")) {
            that.userOptions = that.stepList[num + 1].role.users
          } else {
            that.userOptions = []
          }
        }

        that.userBackOptions = that.userOptions
      } else {
        if (row.has_script) {
          that.reviewROptions = that.reviewAOptions
        } else {
          that.reviewROptions = that.reviewLOptions
        }
      }
      that.stepList.push(objtmp)
      that.stepList.unshift(objtmp)
    }
    var data = JSON.parse(response.data)
    var formfields = JSON.parse(response.formfields)
    var file_info = JSON.parse(response.file_info)
     if (file_info == null){
      file_info = []
     }
    that.temp.curstep = row.cur_step
    for (var i = 0; i < formfields.length; i++) {
      var obj = formfields[i]
      if (obj.props == null || obj.props == undefined || obj.props == "") {
        obj.props = {"disabled": true}
      } else {
        obj.props.disabled = true
      }
    }
    that.formRule = formfields
    that.workorderFields = data
    that.file_info = file_info
    that.dialogStatus = 'update'
    that.getAuditRecordList(row.id)
    that.dialogFormVisible = true
    if (that.curworkorder != null && that.curworkorder.name.indexOf('dbsql_') >= 0) {
      that.isShowSql = true
    }
  })
}

export function handleDetailU(that, row,api) {
  that.resetTemp()
  that.temp.cur_step = row.cur_step
  that.workorderName = row.cname + "工单"
  that.dialogStatus = 'detail'
  that.creator = row.creator_detail
  that.curworkorder = row
  api.get(row.id).then(response => {
    var jsonData = JSON.parse(response.data)
    var jsonFormfields = JSON.parse(response.formfields)
    var jsonSteps = JSON.parse(response.steps)
    var file_info = JSON.parse(response.file_info)
    if (file_info == null ){
      file_info = []
     }
    that.curworkorder.exec_log=response.exec_log
    if (jsonSteps == null || jsonSteps == undefined || jsonSteps.length <= 0) {
      that.stepList = []
    } else {
      that.stepList = jsonSteps
      var obj = {}
      obj.id = -1
      obj.cname = "申请人"
      var objtmp = {}
      objtmp.id = -1
      objtmp.role = obj

      if (row.cur_step == null) {
        that.stepActive = that.stepList.length + 2
      } else {
        for (var j = 0; j < that.stepList.length; j++) {
          if (that.stepList[j].id == row.cur_step) {
            break
          }
          that.stepActive++
        }
        that.stepActive++
      }

      that.stepList.push(objtmp)
      that.stepList.unshift(objtmp)
    }
    that.formRule = jsonFormfields
    that.workorderFields = jsonData
    that.file_info = file_info
    that.getAuditRecordList(row.id)
    that.dialogFormVisible = true
  })
}

export function getAuditRecordListU(that, api, id) {
  api.auditrecord(id).then(response => {
    that.auditrecordList = []
    for (var i = 0; i < response.length; i++) {
      var obj = response[i]
      if (isRealObj(obj.remark)) {
        obj.remark = obj.remark.replace(/\n|\r\n/g, "<br/>")
      } else {
        obj.remark = ''
      }
      //最后一个人（同意，或者同意执行）
      if((that.stepList.length-2)==response.length && i==0 && obj['opinion']==1){
        obj['opinion']=50
      }
      that.auditrecordList.push(obj)
    }
  })
}


export function reviewDataU(that, api, flag) {
  that.$refs['dataForm'].validate((valid) => {
    if (valid) {
      var params = {}
      if (that.isShowNextUser && that.isShow) {
        params.next_user = that.temp.next_user
      }
      params.remark = that.temp.remark
      params.opinion = that.temp.opinion
      that.reviewLoading = true
      api.audit(that.temp.id, params).then(() => {
        if (flag == 0) {
          that.getWaitingList()
          that.getDoneList()
        } else {
          that.getSupList()
        }
        that.dialogFormVisible = false
        that.$notify({
          title: '成功',
          message: '更新成功',
          type: 'success',
          duration: 2000
        })
      })
      setTimeout(() => {
        that.reviewLoading = false
      }, 1 * 1000)
    }
  })
}

export function handleChangeU(that, value) {
  that.temp.next_user = ""
  if (value == 3) {
    for (var i = 1; i < that.stepList.length - 1; i++) {
      if (that.stepList[i].id == that.curworkorder.cur_step) {
        that.userOptions = that.stepList[i].role.users
        break
      }
    }
    that.isShow = true
    that.isShowNextUser = true
  } else if (value == 1) {
    that.isShow = true
    that.userOptions = that.userBackOptions
    that.isShowNextUser = that.isShowBackNextUser
  } else {
    that.isShow = false
    that.userOptions = that.userBackOptions
    that.isShowNextUser = that.isShowBackNextUser
  }
}

export function resetTempU(that) {
  that.temp = {
    next_user: undefined,
    remark: "",
    opinion: undefined,
    id: undefined,
    curstep: undefined,
    status: undefined,
  }
  that.stepActive = 0
  that.isShowNextUser = false
  that.isShowBackNextUser = that.isShowNextUser
  that.auditrecordList = []
  that.creator = {}
  that.reviewROptions = []
  that.curworkorder = {}
}

export function handleFilterU(that, search, action) {
  if (action == "waiting") {
    that.waitingListQuery.search = search
    that.waitingListQuery.page = 1
    that.getWaitingList()
  } else if (action == "done") {
    that.doneListQuery.search = search
    that.doneListQuery.page = 1
    that.getDoneList()
  } else if (action == "supervise") {
    that.supListQuery.page = 1
    that.supListQuery.search = search
    that.getSupList()
  } else {
    that.historyListQuery.page = 1
    that.historyListQuery.search = search
    that.getHisList()
  }
}
