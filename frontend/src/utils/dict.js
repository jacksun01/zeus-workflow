export const methodOptions = [
  {key: 'ALL', display_name: 'ALL'},
  {key: 'GET', display_name: 'GET'},
  {key: 'POST', display_name: 'POST'},
  {key: 'PUT', display_name: 'PUT'},
  {key: 'PATCH', display_name: 'PATCH'},
  {key: 'DELETE', display_name: 'DELETE'},
]
export const userTypeOptions = [
  {key: 'customuser', display_name: '自定义用户'},
  {key: 'anonymous', display_name: '匿名用户'},
  {key: 'authenticated', display_name: '已认证用户'},
]

export const isActiveOptions = [
  {key: true, display_name: '是'},
  {key: false, display_name: '否'},
]

export const MountOptions = [
  {key: 'unmount', display_name: '未挂载'},
  {key: 'mount', display_name: '已挂载'},
]

export const ActionOptions = [
  {key: 1, display_name: '添加'},
  {key: 2, display_name: '修改'},
  {key: 3, display_name: '删除'},
]

export const isExpiredOptions = [
  {key: 0, display_name: '过保'},
  {key: 1, display_name: '未过保'},
]

export const dbEnvOptions = [
  {key: 'online', display_name: '生产'},
  {key: 'sim', display_name: 'sim预发'},
  {key: 'qa', display_name: 'qa测试'},
  {key: 'dev', display_name: '开发'},
]

export const dbTypeOptions = [
  {key: 'master', display_name: '主库'},
  {key: 'slave', display_name: '从库'},
]
export const dbSlaveTypeOptions = [
  {key: 'instance', display_name: '实例级从库'},
  {key: 'db', display_name: '多源从库'},
]

export const sqlTypeOptions = [
  {key: 'DML', display_name: 'DML:操作表数据'},
  {key: 'DDL', display_name: 'DDL:操作表结构'},
]
export const sqlJobStatusOptions = [
  {key: -1, display_name: "待执行"},
  {key: -2, display_name: "执行中"},
  {key: 0, display_name: "执行成功"},
  {key: 1, display_name: "执行成功"},
  {key: 2, display_name: "执行失败"},
  {key: 3, display_name: "已定时"},
  {key: 4, display_name: "已放弃"},
  {key: 7, display_name: "回滚中"},
  {key: 8, display_name: "回滚失败"},
  {key: 9, display_name: "回滚成功"},
]


export const fieldTypeOptions = [
  {key: "input", display_name: "输入框"},
  {key: "InputNumber", display_name: "数字输入框"},
  {key: "DatePicker", display_name: "日期"},
  {key: "TimePicker", display_name: "时间"},
  {key: "switch", display_name: "开关"},
  {key: "radio", display_name: "单选框"},
  {key: "checkbox", display_name: "多选框"},
  {key: "select", display_name: "下拉框"},
  {key: "textarea", display_name: "文本域"},
  {key: "cascader", display_name: "级联选择器"},
  {key: "upload", display_name: "上传"},
  {key: "hidden", display_name: "隐藏域"}
]


export const workorderStatusOptions = [
  {key: 0, display_name: '已驳回'},
  {key: 1, display_name: '新建中'},
  {key: 2, display_name: '已提交'},
  {key: 3, display_name: '等待审批'},
  {key: 4, display_name: '已处理'},
  {key: 5, display_name: '已结束'}
]

export const workorderExecStatusOptions = [
  {key: 0, display_name: '未执行完'},
  {key: 1, display_name: '执行成功'},
  {key: 2, display_name: '执行失败'},
]

export const reviewOptions = [
  {key: 1, display_name: '同意'},
  {key: 0, display_name: '驳回'},
  {key: 3, display_name: '移交工单'},
]

export const reviewAOptions = [
  {key: 1, display_name: '同意,自动执行'},
  {key: 2, display_name: '同意，已手动执行完成'},
  {key: 0, display_name: '驳回'},
  {key: 3, display_name: '移交工单'},
]

export const reviewLOptions = [
  {key: 2, display_name: '同意，已手动执行完成'},
  {key: 0, display_name: '驳回'},
  {key: 3, display_name: '移交工单'},
]


export const limitOptions = [
  {key: 100, display_name: 100},
  {key: 500, display_name: 500},
  {key: 1000, display_name: 1000},
]


export const sqlQueryOptions = [
  {key: "sql", display_name: "SQL"},
  {key: "limit", display_name: "行限制"},
  {key: "effect_row", display_name: "影响行"},
  {key: "query_cost_time", display_name: "查询耗时"},
  {key: "masking_cost_time", display_name: "脱敏耗时"},
  {key: "cost_time", display_name: "总耗时"},
  {key: "creator", display_name: "查询人"},
  {key: "create_time", display_name: "查询时间"},
]

export const sqlQueryPermTypeOptions = [
  {key: "TABLE", display_name: "表"},
  {key: "DATABASE", display_name: "整库"},
]


export const selectOptions = [
  {key: 1, display_name: "选择规则"},
  {key: 0, display_name: "编写规则"},
]
export const feedbackOptions = [
  {key: 10, display_name: '已解决'},
  {key: 11, display_name: '未解决'},
]

export const auditRecordOptions = [
  {key: 1, display_name: '同意'},
  {key: 2, display_name: '同意，已手动执行完成'},
  {key: 0, display_name: '驳回'},
  {key: 3, display_name: '移交工单'},
  {key: 10, display_name: '已解决'},
  {key: 11, display_name: '未解决'},
  {key: 50, display_name: '同意,自动执行'},
]

export const roleTypesOptions = [
  {key: "static", display_name: '静态角色'},
  {key: "dynamic", display_name: '动态角色'},
]
export const permOptions = [
  {key: "SELECT", display_name: "SELECT"},
  {key: "UPDATE", display_name: "UPDATE"},
  {key: "DELETE", display_name: "DELETE"},
  {key: "INSERT", display_name: "INSERT"},
  {key: "ALL", display_name: "ALL"},
  {key: "ALTER", display_name: "ALTER"},
  {key: "CREATE", display_name: "CREATE"},
  {key: "DROP", display_name: "DROP"},
  {key: "SHOW", display_name: "SHOW"},
  {key: "GRANT", display_name: "GRANT"},
  {key: "EVENT", display_name: "EVENT"},
  {key: "EXECUTE", display_name: "EXECUTE"},
  {key: "FILE", display_name: "FILE"},
  {key: "INDEX", display_name: "INDEX"},
  {key: "LOCK", display_name: "LOCK"},
  {key: "PROCESS", display_name: "PROCESS"},
  {key: "PROXY", display_name: "PROXY"},
  {key: "REFERENCES", display_name: "REFERENCES"},
  {key: "RELOAD", display_name: "RELOAD"},
  {key: "REPLICATION", display_name: "REPLICATION"},
  {key: "SHUTDOWN", display_name: "SHUTDOWN"},
  {key: "SUPER", display_name: "SUPER"},
  {key: "TRIGGER", display_name: "TRIGGER"},
  {key: "USAGE", display_name: "USAGE"}
]

export const requiredOptions = [
  {key: '1', display_name: '必填'},
  {key: '0', display_name: '非必填'},
]

export const colorOptions = [
  {key: '1', display_name: '255, 0, 0'},
  {key: '0', display_name: '255, 165, 0'},
]

export const eurekaStatusOptions = [
  {key: 'OUT_OF_SERVICE', display_name: '停止注册'},
  {key: 'UP', display_name: '启动注册'},
]

export const LtypeOptions = [
  {key: '5xx', display_name: '日志错误',showtype:2},
  {key: 'tcpnum', display_name: 'TCP链接',showtype:1},
  {key: 'srtx', display_name: '进出流量',showtype:1},
  {key: 'cpu', display_name: 'mem',showtype:1},
  {key: 'io', display_name: 'io',showtype:1},
  {key: 'load', display_name: 'load',showtype:1},
]

export const cicdStepsMap = {
  'stop_service':'停止服务',
  'service_offline':'平滑下线',
  'push_code':'推送代码',
  'unzip_package':'解压代码',
  'start_service':'服务启动',
  'health_check':'健康检测',
}
