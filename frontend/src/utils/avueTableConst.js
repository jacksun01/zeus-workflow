/**
 * 获取form表结构常量参数
 */

export const DIC = {
  VAILD: [{
    label: '是',
    value: true
  }, {
    label: '否',
    value: false
  }],
}
//--- add search and menu
export const tableOpitonSearchMenuM = {
  addBtn: true,
  searchBtn: true,
  selection: true,
  border: true,
  page: true,
  viewBtn: true,
  align: 'center',
  menuAlign: 'center',
  menuWidth: 100,
  searchMenuSpan: 6,
  menuType: 'menu',
  searchShow: false,
  column: [
    {
      prop: 'u8',
      search: true
    },
  ]
}
export const tableOpitonSearchNoCRUDMenuM = {
  addBtn: false,
  editBtn: false,
  delBtn: false,
  searchBtn: true,
  selection: true,
  border: true,
  page: true,
  viewBtn: true,
  align: 'center',
  menuAlign: 'center',
  menuWidth: 100,
  searchMenuSpan: 6,
  menuType: 'menu',
  searchShow: false,
  column: [
    {
      prop: 'u8',
      search: true
    },
  ]
}
//--- add search and no menu
export const tableNoOptNoMenuSearchM = {
  addBtn: false,
  editBtn: false,
  delBtn: false,
  searchBtn: true,
  selection: true,
  border: true,
  page: true,
  align: 'center',
  searchMenuSpan: 6,
  menu: false,
  viewBtn: false,
  searchShow: false,
  column: [
    {
      prop: 'u8',
      search: true
    },
  ]
}

// add menu and no search
export const tableOpitonNoSearchMenuM = {
  addBtn: true,
  searchBtn: false,
  selection: true,
  border: true,
  page: true,
  align: 'center',
  viewBtn: true,
  column: [],
  menuAlign: 'center',
  menuWidth: 100,
  menuType: 'menu',
  searchShow: false,
}

//--- no search and no menu
export const tableOpitonNoSM = {
  addBtn: true,
  searchBtn: false,
  selection: false,
  border: true,
  page: true,
  align: 'center',
  viewBtn: false,
  column: [],
  menu: false,
  searchShow: false,
}
export const tableOpitonNoSMAdd = {
  addBtn: false,
  searchBtn: false,
  selection: false,
  border: true,
  page: true,
  align: 'center',
  viewBtn: false,
  column: [],
  menu: false,
  searchShow: false,
}

// base
export const tableOpitonSearchM = {
  addBtn: true,
  searchBtn: true,
  selection: true,
  border: true,
  page: true,
  align: 'center',
  menuAlign: 'center',
  menuWidth: 272,
  searchMenuSpan: 6,
  viewBtn: true,
  searchShow: false,
  column: [
    {
      prop: 'u8',
      search: true
    },
  ]
}

export const tableOptNoEditSearchM = {
  addBtn: false,
  editBtn: false,
  delBtn: false,
  viewBtn: true,
  searchBtn: true,
  selection: true,
  border: true,
  page: true,
  align: 'center',
  menuAlign: 'center',
  menuWidth: 100,
  searchMenuSpan: 6,
  searchShow: false,
  column: [
    {
      prop: 'u8',
      search: true
    },
  ]
}
export const tableNoOptAdExtMenuSearchM = {
  addBtn: false,
  editBtn: false,
  delBtn: false,
  searchBtn: true,
  selection: true,
  border: true,
  page: true,
  align: 'center',
  menuAlign: 'center',
  menuWidth: 180,
  searchMenuSpan: 6,
  viewBtn: false,
  searchShow: false,
  column: [
    {
      prop: 'u8',
      search: true
    },
  ]
}

export const tableOpitonM = {
  addBtn: true,
  searchBtn: false,
  selection: true,
  border: true,
  page: true,
  align: 'center',
  menuAlign: 'center',
  menuWidth: 272,
  searchMenuSpan: 6,
  viewBtn: true,
  searchShow: false,
  column: []
}

export const tableOptNoEditM = {
  addBtn: false,
  editBtn: false,
  delBtn: false,
  viewBtn: true,
  searchBtn: true,
  selection: true,
  border: true,
  page: true,
  align: 'center',
  menuAlign: 'center',
  menuWidth: 100,
  searchMenuSpan: 6,
  searchShow: false,
  column: []
}

export function getfilterMethod(objName) {
  return [
    {
      filterMethod: function (value, row, column) {
        return row[objName] === value;
      }
    }]
}

export const cRemoveListDef = ['id', "create_time", "update_time"]
export const uRemoveListDef = ['id', "create_time", "update_time"]
export const afterListDef = ['remark', "create_time", "update_time"]



