export default {
  route: {
    usercenter: "用户中心",
    usermgt: "用户管理",
    groupmgt: "部门管理",

    cca:'成本中心',
    cca_index:'首页',
    cca_departappress:'部门项目配置',
    cca_publicconfs:'云授权配置',
    cca_conf:'公用配置',
    cca_rescalrules:'产品分摊规则',
    jobcenter: '任务中心',
    scriptjob: '作业管理',
    crontask: "计划任务",
    txcvm: "cvm服务器",
    txclb: "负载均衡",
    dns: "域名解析",
    httpdns: "httpdns",
    domain: "域名配置",
    region: "地区配置",
    r2d: "地区策略",
    user: '用户系统',
    userList: '用户列表',
    userInfo: '个人信息',
    userResetPwd: '重置密码',
    userChangePwd: '修改密码',
    userChangeAvatar: '用户头像',
    roleList: '角色列表',
    urlList: 'Url权限列表',
    modellog: '操作日志系统',
    logSentryList: '用户操作记录',
    stree: '服务树',
    streeList: '服务树',
    cmdb: '资产系统',

    mdb: '数据库系统',
    dbconsole:'控制台',
    mdb_mange:'服务管理',
    dbClusterList: '集群管理',
    dbinstancesList: '实例管理',
    dbList: '库管理',
    maskingrule: '脱敏规则',
    maskingcolumn: '脱敏字段',
    dbtrxs:"在线事务",
    dbtrxcounts:"事务并发执行数",
    slowqueryreviewhistorys:"SQL慢查询",
    slowqueryreviewhistoryadds:"当天新增慢查询",
    slowqueryreviewperdays:"每天新增慢查询",
    tableinfos:"mysql表信息",
    tablesizecrements:"表行数增长信息统计",
    dbcheckperdays: "DB每日巡检",
    fullTableScan: "全表扫描及慢查询",

    sqlOptimize: 'SQL优化',
    sqlQuery: 'SQL查詢',
    sqlJob: 'SQL上线',
    queryPerm: '查询权限管理',
    dbuserList: '数据库用户管理',

    inception: 'Inception配置',
    hostList: '主机管理',
    lbList: '负载均衡管理',
    networkDeviceList: '网络设备管理',
    projectList: '项目列表',
    workflow: '工单系统',
    workflowList: '工作流管理',
    workorderList: '工单需求',
    workflowgroupList: '工作流组列表',
    formfieldsList: '工单项',
    auditStepsList: '审批流',
    workordernew: '新建工单',
    woswaitingList: '审批工单',
    wosuperviseList: '督办工单',
    wohistoryList: '历史工单',

    cicd: '发布系统',
    modList: '模块管理',
    pub: '发布代码',
    pubprod: '发布生产',
    pubtest: '发布测试',
    pubdev: '发布开发',
    jobList: '发布历史',
    jobRuleList: '发布规则',
    jobLog: '发布任务日志',
    cicd_project: '应用管理',
    cicd_deploy:'发布代码',
    cicd_deployhistory: '发布历史',
    cicd_packageedition: '发布jar包',
    cicd_workorder:'发布申请',
    cicd_workorderverify:'发布审核',
    cicd_workorderconfirm:'QA验收',
    cicd_workorderpub:'发布入口',
    deploy_manage: '发布管理',
    vm_deploy: '线上kvm发布',
    vm_deploy_history: '线上kvm发布历史',
    k8s_deploy: '线上k8s发布',
    k8s_testdeploy: '线下k8s发布',

    mlog: '业务日志',
    eslogTail: 'ES业务日志',
    logType: "日志类型管理",
    logConf: '业务配置管理',
    alilog:'阿里业务日志',

    mcloud: '混合云系统',
    aliyun: '阿里云',
    tencent: '腾讯云',
    conf: '通用配置',
    operaterecordsList: '混合云日志',
    cloudstack: 'CloudStack',
    redisList: 'redis管理',
    rhostList: '宿主机管理',

    publicconfList: '公有云授权配置',
    publicregionList: '可用区域管理',
    privateconfList: '私有云授权配置',

    redisclassList: 'redis类型',
    hosttypeList: '主机类型',
    hosttemplateList: '模板类型',

    mfalcon: 'Flcon监控',
    mfalconindex: '监控集合页',

    //m Supervisong Center
    msc:'监控中心',
    user_perform_dashboard: '服务性能感知系统',
    user_trend: '服务性能数据趋势',
    servicePreform:'服务性能中心',
    msc_trenddata:'核心业务趋势',
    alarm_config: '告警配置',
    monitor_alarm: "监控告警",
    alarm_dashboard: "告警大屏",
    monitor_dashboard: "监控大屏",
    alarm_level: "告警等级",
    alarm_temp: "告警模板",
    alarm_group_subscribe: "群组订阅",
    alarm_personal_subscribe: "个人订阅",
    msc_decisionopt:'紧急操作台',
    msc_conf:'通用配置',
    user_trendgroup: "用户性能配置",
    msc_trendgroup:'核心业务配置',

    msc_service_monitor:'业务监控平台',

    decisionopt:'控制台',

    mk8s: 'K8S',
    mk8s_harbor:'項目镜像',
    mk8s_harborproject: '项目組',
    mk8s_harborlog: '日志',
    mk8s_harbor_repo: '镜像',
    mk8s_harbor_repo_tag: '镜像详情',
    mk8s_harbor_manifest: '构建历史',

    mk8s_conf_clusters: '集群认证',
    mk8s_pub_deployments: '部署配置',
    mk8s_pub_deployrecords: '发布历史',
    mk8s_conf_labels: '标签',
    mk8s_conf_resources: '资源',
    mk8s_conf_volumes: '挂载卷',
    mk8s_pub:'发布',
    mk8s_conf:'通用配置',
    mk8s_conf_affinitys:'亲和策略',
    mk8s_conf_checkhealths:'健康检查策略',

    mk8s_cluster: "集群管理",
    mk8s_pod: "应用实例",
    mk8s_deployment: "服务控制",
    mk8s_service: "服务负载",
    mk8s_event: "集群事件",
    mk8s_node: "集群节点",
    mk8s_hpa: "弹性扩容",
    network_policy: "网络策略",

    iapetus:"问题定问系统",
    chains:"业务链",
    chainnodes:'定位图',

    hera:'全链路跟踪',
    hera_index:'首页',
    hera_publicconfs:'通用配置',
    hera_sampleddata:'超时数据',

    dashboard: '首页',
    introduction: '简述',
    documentation: '文档',
    guide: '引导页',
    permission: '权限测试页',
    pagePermission: '页面权限',
    directivePermission: '指令权限',
    icons: '图标',
    components: '组件',
    componentIndex: '介绍',
    tinymce: '富文本编辑器',
    markdown: 'Markdown',
    jsonEditor: 'JSON编辑器',
    dndList: '列表拖拽',
    splitPane: 'Splitpane',
    avatarUpload: '头像上传',
    dropzone: 'Dropzone',
    sticky: 'Sticky',
    countTo: 'CountTo',
    componentMixin: '小组件',
    backToTop: '返回顶部',
    dragDialog: '拖拽 Dialog',
    dragSelect: '拖拽 Select',
    dragKanban: '可拖拽看板',
    charts: '图表',
    keyboardChart: '键盘图表',
    lineChart: '折线图',
    mixChart: '混合图表',
    example: '综合实例',
    nested: '路由嵌套',
    menu1: '菜单1',
    'menu1-1': '菜单1-1',
    'menu1-2': '菜单1-2',
    'menu1-2-1': '菜单1-2-1',
    'menu1-2-2': '菜单1-2-2',
    'menu1-3': '菜单1-3',
    menu2: '菜单2',
    Table: 'Table',
    dynamicTable: '动态Table',
    dragTable: '拖拽Table',
    inlineEditTable: 'Table内编辑',
    complexTable: '综合Table',
    treeTable: '树形表格',
    customTreeTable: '自定义树表',
    tab: 'Tab',
    form: '表单',
    createArticle: '创建文章',
    editArticle: '编辑文章',
    articleList: '文章列表',
    errorPages: '错误页面',
    page401: '401',
    page404: '404',
    errorLog: '错误日志',
    excel: 'Excel',
    exportExcel: 'Export Excel',
    selectExcel: 'Export Selected',
    uploadExcel: 'Upload Excel',
    zip: 'Zip',
    exportZip: 'Export Zip',
    theme: '换肤',
    clipboardDemo: 'Clipboard',
    i18n: '国际化',
    externalLink: '外链',

  },

  common: {
    changeavatar: '更换头像',
  },
  navbar: {
    logOut: '退出登录',
    resetPwd: '重置密码',
    changePwd: '修改密码',
    userinfo: '个人信息',
    dashboard: '首页',
    github: '项目地址',
    screenfull: '全屏',
    theme: '换肤',
    size: '布局大小',
    help: '帮助文档'
  },

  guide: {
    description: '引导页对于一些第一次进入项目的人很有用，你可以简单介绍下项目的功能。本 Demo 是基于',
    button: '打开引导'
  },
  components: {
    documentation: '文档',
    tinymceTips: '富文本是管理后台一个核心的功能，但同时又是一个有很多坑的地方。在选择富文本的过程中我也走了不少的弯路，市面上常见的富文本都基本用过了，最终权衡了一下选择了Tinymce。更详细的富文本比较和介绍见',
    dropzoneTips: '由于我司业务有特殊需求，而且要传七牛 所以没用第三方，选择了自己封装。代码非常的简单，具体代码你可以在这里看到 @/components/Dropzone',
    stickyTips: '当页面滚动到预设的位置会吸附在顶部',
    backToTopTips1: '页面滚动到指定位置会在右下角出现返回顶部按钮',
    backToTopTips2: '可自定义按钮的样式、show/hide、出现的高度、返回的位置 如需文字提示，可在外部使用Element的el-tooltip元素',
    imageUploadTips: '由于我在使用时它只有vue@1版本，而且和mockjs不兼容，所以自己改造了一下，如果大家要使用的话，优先还是使用官方版本。'
  },
  notice: {
    delete: '删除不可恢复，是否确定删除？',
    createsuccess: '创建成功！',
    updatesuccess: '更新成功!',
    delsuccess: '删除成功！',
    syncsuccess: '同步成功！',
    linksuccess: '连接成功！',
    linkfail: '连接失败！',
    lastNodeName: '最后一个节点名字为环境，环境必须以-online/-dev/-qa/-sim/-res结尾！',
    hostempty: '主机为空，无法查看监控性能!',
    node_no_del:'节点下有子节点，不允许删除!',
    dealsuccess:'处理成功！',
  },
  table: {
    dynamicTips1: '固定表头, 按照表头顺序排序',
    dynamicTips2: '不固定表头, 按照点击顺序排序',
    dragTips1: '默认顺序',
    dragTips2: '拖拽后顺序',
    title: '标题',
    importance: '重要性',
    type: '类型',

    search: '搜索',
    add: '增加',
    export: '导出',
    exportall: '导出全部',
    upload: '导入',
    reviewer: '审核人',
    id: '序号',
    date: '时间',
    author: '作者',
    readings: '阅读数',
    status: '状态',
    actions: '操作',
    edit: '编辑',
    review: '审批',
    nextreviewer: '下一个审核人',
    reviewRemark: '审批意见',
    publish: '发布',
    draft: '草稿',
    delete: '删除',
    cancel: '取 消',
    confirm: '确 定',
    name: '名称',
    remark: '备注',
    cname: '中文名称',
    phone: '手机号',
    create_time: '创建时间',
    update_time: '更新时间',
    end_time: '截止时间',
    email: '邮箱',
    username: '用户名',
    description: '描述',
    showadvance: '高级搜索',
    save: '保存',
    is_active: '是否启用',
    role: '角色',
    copy: '复制',
    detail: "查看",
    env: '环境',
    goback: '返回',
    password: '密码',
    perm: '权限',
    perm_type: '权限类型',
    table: '表',
    getpwd: '获取密码',
    stree_id: '树节点',
    sync: '同步',
    developers: '开发者',
    testers: '测试者',
    per: '次',
    arch: '架构',
    os: '操作系统',
    os_version: '操作系统版本',
    docker_version: 'Docker版本',

    reboot:'重启',
    restore:'恢复',
    shutdown:'关闭',
    pause:'暂停',
    refresh:'刷新',
    refreshPod:'刷新Pod',
    ip:'ip地址',
    country:'中国',
    city:'市',
    province:'省',
    creator:'创建人',
    company:'公司',
    department:'部门',
    entry_excel:'Execl录入',
    publicconfs:'通用配置',
  },
  login: {
    title: '系统登录',
    getsmscode: '获取短信验证码',
    loginpwdtitle: '密码登录',
    loginphonetitle: '手机登录',
    logIn: '登录',
    username: '账号',
    password: '密码',
    phone: '手机号',
    any: '随便填',
    register: '注册',
    resetPwd: '重置密码',
    thirdpartyTips: '提示：到用户中心绑定第三方后，才可以使用对应的第三方登录'
  },
  register: {
    title: '系统注册',
    regisTer: '注册',
    username: '账号',
    password: '密码',
    email: '邮箱',
    smscode: '验证码',
    phone: '手机号'
  },
  resetpwd: {
    title: '重置密码',
    password: '新密码',
    confirmPassword: '确认密码',
    resetpwd: '重置密码',
  },
  documentation: {
    documentation: '文档',
    github: 'Github 地址'
  },
  permission: {
    roles: '你的权限',
    switchRoles: '切换权限'
  },
  userconf: {
    isvoice: '语音',
    issms: '短信',
    isemail: '邮件',
  },
  userrole: {
    expired_time: '过期时间',
  },

  role: {
    name: '角色',
    detail: '角色描述',
    users: '用户列表',
  },
  idc: {
    name: '名称',
    cname: '中文名称',
    remark: '备注',
    address: '机房地址',
    contact: '联系人',
    phone: '联系电话',
    cabinet: '机柜信息',
    bandwidth: '机房带宽(M)',
    network: '网段',
    operator: '运营商'
  },
  networkdevice: {
    hostname: "名称",
    device_type: "设备类型",
    model: "型号",
    cabinet: "机柜",
    position: "U位",
    sn: "SN编号",
    use_status: "使用状态",
    manage_ip: "管理IP",
    asset_no: "资产编号",
    vendor: "供应商",
    up_time: "上架时间",
    expired_time: "过保时间",
    remark: "备注",
    idc: "机房"
  },

  host: {
    hostname: '主机名',
    ip: 'ip地址',
    host_type: '主机类型',
    cabinet: '机柜',
    position: 'U位',
    up_time: '上架时间',
    expired_time: '过保时间',
    asset_no: '资产编号',
    vendor: '供应商',
    use_status: '使用状态',
    public_ip: '公网IP',
    manage_ip: '管理IP',
    other_ip: '其他IP',
    port: 'SSH端口号',
    model: '型号',
    sn: 'SN编号',
    os: '操作系统',
    cpu_memory_disk: 'CPU/内存/磁盘',
    baseinfo: '负载/CPU/内存/IO',
    cpu: 'CPU',
    memory: '内存',
    disk: '硬盘',
    run_status: '运行状态',
    salt_status: 'Salt状态',
    remark: '备注',
    idc: '机房',
    trees: '挂载树节点'
  },
  publish_code: {
    'pub': '发布代码',
  },

  stree: {
    trees: '挂载树节点',
    adddbs: '添加DB',
    showperform: '性能图',
    pub_code: '发布代码',
    pub_k8s_code: '发布k8s代码',
    wiki: 'wiki地址',
    prod_domain: "生产域名",
    test_domain: "测试域名",
    dev_domain: "开发域名",
    applog_es_index:'ES日志索引',
    applog_es_ip:'ES日志地址',
    git: 'git地址',
    code_type: '代码类型',
    description: '业务描述',
    archaddr: '架构图地址',
    puser:'项目负责人',
    opuser:'运维负责人',
    gitid:'GitId',
    treenode_filter: '树节点过滤 , 回车搜索',
    mount_host: '所在机器',
    mount_pod: '所在Pods',
    mounted_host: '已挂在机器',
    mountable_host: '可挂在机器',
    project_detail: '业务详情',
    demand: '需求周期',
    mount_db: '关联DB',
    db_conn_user:'连接用户',
    charge_person: '报警负责人',
    rolelist: '权限列表',
    roleop: '具有查看、新建和编辑树节点权限',
    roleop_admin: '具有查看、新建、编辑和拖拽树节点权限，同时还有审批OP权限',
    rolerd: '具有查看树节点权限',
    rolerd_admin: '具有查看树节点权限，同时还有审批RD权限',

    falconlist: 'Falcon监控模板列表',
    falcon_model_name: '模板名字',
    falcon_band_user: '绑定人',
    node_name: '节点名字必须是字母开头 数字和字母 - 组合！并且不能命名为host-pool/主机资源池',
    node_no_del: '此节点有子级，不可删除！',

    demandlist: '服务生命周期表(需求表)',
    demand_title: '需求标题',
    demand_content: '需求内容',
    toolbox: '工具箱',
    adjustrecord:'变更记录',
    detail:'变更详情',
    sla:'sla承诺'
  },
  stree_mk8s:{
    hostname:'Pod名',
    ip:'Pod-IP',
    phase:'运行状态',
    creat_time:'创建时间',
    restart_count:'重启次数',
  },


  mdb: {
    env: '环境',
    showconf: '查看配置',
    showprocesslist: '查看慢查询',
    showdbs: '查看所有库',
    showmonitor: '实例监控',
    showhostmonitor: '所在机器监控',
    createdb: '创建库',
    createuser: '用户授权',

    sqlconsole: 'SQL控制台',
    sqlresult: '查询结果',
    tablenotice: '显示表结构',
    querysqlhistory: '查询历史记录',
    table: '表',
    tablename: '表名',

    currdbnotice: '当前数据库:',
    syntaxok: '语法检查通过！',

    inceconsole: 'Inception控制台',
    inceparams: '参数列表',
  },

  mdb_dbcluster: {
    env: '环境',
    dbinstances: '实例',
    dbs: '库',
  },

  mdb_dbinstance: {
    host: 'IP地址',
    port: '端口',
    type: '类型',
    user: '用户名',
    passwd: '密码',
    name: '名称',
    cname: '中文名',
    check_conn: '测试连接',
    dbcluster: '集群',
    slave_type: '从类型',
    syncslave: '导入从实例',
  },
  mdb_db: {
    name: '数据库名',
    cname: '中文名',
    charset: '字符集',
    dbcluster_name: '集群',
    read_host: '读域名',
    write_host: '写域名',
    notice_create: '注意:\n' +
    '          选择数据库名：\n' +
    '            1. 如果选择以下已有的数据库名，为把已经存在的数据库导入系统，\n' +
    '            2. 如果输入没有的数据库名，那么为新建数据库，会操作主实例，\n' +
    '              在实例中新建数据库!\n' +
    '          读写域名说明：\n' +
    '            3. 读域名填写以后 在以下SQL查询，优化中才能查到\n' +
    '            4. 写域名填写以后 在以下SQL执行中才能使用\n'
  },
  mdb_dbuser: {
    grant: '用户授权',
    privileges: '权限',
    table: '表名',
    ip: 'IP或IP段',
  },
  mdb_sqladvisor: {
    sql: 'SQL语句',
    database: '数据库',
    table: '表',
    type: '优化器',
    advisor: 'SQL建议',
    syntax: 'SQL语法',
    format: 'SQL美化',
    clear: '清空SQL',
    query: 'SQL查詢',
    limit: "查询行",
  },

  mdb_sqlquery: {
    sql: 'SQL',
    limit: '行数限制',
    effect_row: '影响行',
    query_cost_time: '查询耗时',
    masking_cost_time: '脱敏',
    cost_time: '总耗时',
    creator: '查询人',
    db: '查询库',
  },

  mdb_sqljob: {
    task_id: '工单ID',
    db: '数据库',
    sql: 'SQL语句',
    sql_type: 'SQL类型',
    creator: '提交人',
    status: '状态',
    errormessage: '错误信息',
    affectedrows: '影响行数',
    executetime: '执行时间',
    executecosttime: '执行耗时',
    executeresult: '执行结果',
    rollbackable: '可回滚',
    rollbacktime: '回滚时间',
    rollbackcosttime: '回滚耗时',
    rollbackresult: '回滚结果',
    rollback: "回滚",
    rollbacksql: '回滚SQL',
    execresult: '执行结果',
    checkSyntax: 'SQL语法检查',
    sqlgrammar: 'SQL语法规范',
    order_id: '工单号'
  },
  mdb_inceptionconf: {
    remark: "备注",
    param: "可选参数",
    default: "默认值",
    value: "当前值",
    description: "功能说明",
    host: '域名',
    port: '端口',
    username: '用户名',
    ddl_limit: 'DDL语句限制',
    dml_limit: 'DML语句限制',
  },
  mdb_querypermissions: {
    username: "用户名",
    perm_type: "权限类型",
    tables: "表",
    expired_time: "过期时间",
    db: '数据库',

  },
  workflow: {
    steps: "审批流程",
    group_cname: "工单组",
    is_common: '普通工单',
    name: '工单名',
    approvers: '审批人',
    addfields: '工单项',
    addauditflow: '审批流',
    script: '脚本',
    type: '类型',
    addgroup: '添加工单组',
    automation: '自动',
    manual: '手工'
  },

  workorder: {
    flow: "审批流程",
    data: "表单数据",
    status: "状态",
    exec_status: "执行状态",
    exec_log: "执行日志",
    workflow: "工单",
    creator: "申请人",
    cur_user_role: "当前处理人/角色",
    title: '标题',
    contact: '抄送人',
    audit_user: '审批人/处理人',
    feedback: '反馈',
    hotwo: '热门工单',
    wotype: '工单分类',
    mine: '我的工单',
    per: '次',
  },

  workflow_formfields: {
    name: "名称",
    cname: "中文名称",
    remark: "备注",
    type: "组件类型",
    field: "字段名",
    title: "标题",
    value: "默认值",
    props: "属性规则",
    validate_select: '校验选择',
    validate: "高级校验规则",
    validate_required: '是否必填',
    validate_message: '校验提示内容',
    dicurl: '数据获取接口',
    options: "选项数据",
    order_num: "排序",
    is_active: "是否启用",
    workflow: "工作流",
    demo: "参考模板",
  },
  workflow_audit: {
    role_type: "角色类型",
  },

  cicd: {
    project: '项目名',
    action: '操作指令',
    hostList: '主机列表',
    gittag: 'Git分支或tag',
    jira_id:'JiraId',
    notify_user: '通知用户',
    deploy_type: '发布类型',
    rollbackType: '回滚类型',
    //2
    tag: '版本',
    ip: 'ip地址',
    version: '当前版本',
    pubtime: '发布时间',
    parallelper:'并发比例',
    pubdesc: '发布内容',
    pubstatus: '发布状态',
    pubisher: '发布人',
    comment: '发布内容',
    ctag: '构建生成Tag',
    repub: '重新发布',
    checklog: '查看日志',
    refreshlog: '刷新日志',
    appname:'备注',
    branch:'分支名',
    email: '邮箱',
    tester:'测试人员',

    processtitle:'发布应用',
    jiadetail:'需求详情',
    pub_priority:'上线顺序',
    revokedeploy:'停止发布',
  },
  cicd_pc:{
    key:'Jira编号',
    summary:'需求标题',
    url:'url',
    reporter:'报告人',
    creator:'创建人',
    status:'状态',
    createDate:'创建时间',
    changeDate:'修改时间',
    priority:'优先级',
    pf:'计划完成时间',
    af:'实际完成时间',
  },

  cicd_mod: {
    mod_type: "模块类型",
    deploy_dir: "部署路径",
    deploy_sec_dir: "tomcat二级路径",
    tomcat_version: "tomcat版本",
    server_port_prod: "端口",
    compile: "编译参数",
    jdk_version: "jdk版本",
    health_check_file: "健康检查",
    changeparams: "参数调整",
  },

  log: {
    search: '搜索',
    service: '业务',
    server: '主机名',
    timerange: '时间段',
    linenum: '行数',
    cmd: '命令',
    stop: '停止',
    syntax: 'ES查询语法规则',
    alisyntax:'阿里查询语法规则',
    fields: '显示字段',

    logstore:'业务组',
    podname:'容器名称',
  },

  mcloud_hosts: {
    template: '主机模板',
    count: '主机数量(1)',
    name: '实例ID/名称',
    os: '操作系统',
    ip: 'ip地址',
    conf: '配置',
    chargetype: '付费方式',
    PostPaid: "转换后付费",
    status: '运行状态',
    region: '区域',
    startup: '开机',
    shutdown: '关机',
    reboot: '重启',
    shutdownf: '强制关机',
    update: '升配降配',
    copy: '复制',
    destroy: '销毁',
    region_id: "地域ID",
    zone_id: "可用区ID",
    hostname: "主机名",
    image_id: "系统镜像ID",
    system_disk_size: "系统盘大小(G)",
    data_disk_size: "数据盘大小(G)",
    data_disk_category: "数据盘类型",
    instance_charge_type: "计费方式",
    instance_type: "实例类型",
    security_group_id: "安全组ID",
    vpc_id: "专有网络",
    vswitch_id: "子网",
    run_status: '运行状态',
    idc_name: '所在区域',
    instancetype: '主机类型',
    model: '主机类型',
    zone_name: '可用区域',
    subnets: '子网',
    res_status: '资源状态',
    net_wr: '网络读/写量',
    mem_per: 'mem使用率',
    cpu_per: 'cpu使用率',
    cluster: '集群',
    asset_no: '资产编号',
    host_hostname: '宿主机',
  },

  mcloud_lbs: {
    name: "实例名",
    id: "实例ID",
    ip: "实例ip",
    project: "项目名",
    create_time: "创建时间",
    app: '应用',
    server: "后端实例详情",
    listener: "创建监听器",
    lbserver: "绑定四层实例",
    lbrule:  "转发规则配置",
    ruleserver: "绑定七层实例",
    rule_domain: "域名",
    rule_url: "URL",
    listen_protocol: "监听协议",
    listen_port: "监听端口",
    listen_name: "监听名称",
    server_port: "服务器端口",
    lb_instanceid: "服务器实例ID",
    lb_instanceport: "服务器实例端口",

  },

  mcloud_redis: {
    name: '实例ID/名称',
    region: '区域',
    zone: "可用区",
    vpc: '专有网络',
    vswitch: '交换网络',
    version: '版本',
    nodetype: '节点类型',
    instance_class: '实例类型',
    chargetype: '付费方式',
    network: '网络类型',
    QPS: 'QPS',
    max_conn: '最大连接数',
    mem_per: 'mem使用率',
    port: '端口',
    ConnectionDomain: '域名',
    Connections: '连接',
    Bandwidth: '最大内网带宽',
    status: '状态',
    reboot: '重启',
    update: '升配降配',
    copy: '复制',
    password: '密码',
    confirmpwd: '确认密码',
    instance_name: '实例名',
    delete: '释放',
    flush: '清除数据',
    size: '实例大小',
    detail: '实例详情',
  },

  mk8s_harbor: {
    name: '项目名字',
    public: '访问级别',
    repo_count: '镜像仓库数',
    tags_count: '标签数',
    pull_count: '下载数',
    repo_tag: '标签',
    repo_name: '项目',
    docker_version: '版本',
    author: '作者',
    pull: 'Pull命令',
    size: '大小',
    cmd: '操作',
    scan_time: '扫描完成时间',
    repo: '镜像',
  },

  mk8s_pub:{
    projects:'项目组',
    repo:'应用',
    label:'标签',
    pub:'发布',
    name:'名称',
    node_name:'node节点',
    status:'状态',
    pods:'容器组',
    created:'已创建',
    pubtype:'发布策略',
    curtag:'当前版本',
    tag:'版本',
  },

  iapetus:{
    ltype:'定位维度',
    parent:'父节点',
    app_type:'应用类型',
    app_id:'应用名字',
    chain_name:'业务线',
    show_chainnode:'业务链'
  },

  cca:{
    'cloud_tag_entry':'云标签录入',
    'stree_entry':'服务树录入',
  },

  socialTable: {
    provider: '绑定帐号信息',
    bindtime: '绑定时间',
    details: '详情',
    unbind: '解除绑定',
  },

  errorLog: {
    tips: '请点击右上角bug小图标',
    description: '现在的管理后台基本都是spa的形式了，它增强了用户体验，但同时也会增加页面出问题的可能性，可能一个小小的疏忽就导致整个页面的死锁。好在 Vue 官网提供了一个方法来捕获处理异常，你可以在其中进行错误处理或者异常上报。',
    documentation: '文档介绍'
  },

  excel: {
    export: '导出',
    selectedExport: '导出已选择项',
    placeholder: '请输入文件名(默认excel-list)'
  },

  zip: {
    export: '导出',
    placeholder: '请输入文件名(默认file)'
  },

  theme: {
    change: '换肤',
    documentation: '换肤文档',
    tips: 'Tips: 它区别于 navbar 上的 theme-pick, 是两种不同的换肤方法，各自有不同的应用场景，具体请参考文档。'
  },

  tagsView: {
    refresh: '刷新',
    close: '关闭',
    closeOthers: '关闭其它',
    closeAll: '关闭所有'
  },
  tableUser: {
    cname: '姓名',
    date_joined: '入职时间',
  },

  dialog: {
    create: '新增',
    update: '编辑',
    delete: '删除',
    detail: '详情',
  }
}
