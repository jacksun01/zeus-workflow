/*
  对象操作基础js，基本操作都在此处完成，初始化，crud，刷新等 by  sunming
 */
import {isRealObj} from "./index";

const crud = require('./crud')
const index = require('./index')
const tableinfo = require('./avueCreateTable')

//crud
export function getListB(that) {
  var params = Object.assign({}, that.listQuery) // copy obj
  params.page = that.page.currentPage
  params.pagesize = that.page.pageSize
  that.masterApi.list(that.masterUri, params).then(response => {
    that.tableData = response.results
    that.page.total = response.count
  })
}

export function getTableInfoB(that) {
  tableinfo.getTableInfoB(that)
}

export function handleFilterB(that, search, num) {
  if (num == 1) {
    that.listQuery.search = search
  }
  that.listQuery.page = num
  that.page.currentPage = num
  that.getList()
}


export function deleteB(that) {
  crud.deleteData(that, that.masterApi)
}

export function updateB(that, form, index, done, loading) {
  crud.updateData(that, that.masterApi, form, done, loading)
}

export function insertB(that, form, done, loading) {
  crud.createData(that, that.masterApi, form, done, loading)
}


// other opt
export function searchChangeB(that, params) {
  for (var key in that.listQuery) {
    if (key.indexOf("__in") >= 0) {
      var param = key.substring(0, key.indexOf("__in"))
      if (params.hasOwnProperty(param)) {
        if (isRealObj(params[param])) {
          if (params[param] instanceof Array) {
            var tmpstr = ""
            for (var k = 0; k < params[param].length; k++) {
              if (k == 0) {
                tmpstr = params[param][k]
              } else {
                tmpstr = tmpstr + "," + params[param][k]
              }
            }
            that.listQuery[key] = tmpstr
          } else {
            that.listQuery[key] = params[param]
          }

        } else {
          that.listQuery[key] = undefined
        }
      }
    } else {
      if (params.hasOwnProperty(key)) {
        if(!isRealObj(params[key])){
          that.listQuery[key] = undefined
        }else {
          that.listQuery[key] = params[key]
        }
      }
    }
  }
  that.handleFilter(that.listQuery.search, 1)
}

export function refreshB(that) {
  that.getList()
}

export function sizeChangeB(that, val) {
  that.page.currentPage = 1
  that.page.pageSize = val
  that.getList()
}

export function currentChangeB(that, val) {
  that.page.currentPage = val
  that.getList()
}

export function sortChangeB(that, val) {
  var str = "-"
  if (val.order == "ascending") {
    str = "+"
  }
  that.listQuery.ordering = str + val.prop
  that.page.currentPage = 1
  that.getList()
}

export function searchResetB(that) {
  for (var p in that.listQuery) {
    if (!index.isInArray(["ordering", "search"], p)) {
      that.listQuery[p] = undefined
    }
  }
  that.init()
}


