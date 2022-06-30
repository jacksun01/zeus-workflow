<template>
  <div class="dashboard-container">
    <el-tabs v-model="activeName" @tab-click="handleClick" style="margin-left: 10px">
      <el-tab-pane label="地址导航" name="first">
        <el-table
          :data="tableData"
          style="width: 90%;margin-left: 3%"
          :row-class-name="tableRowClassName">
          <el-table-column
            prop="name"
            label="简称"
          >
          </el-table-column>
          <el-table-column prop="produrl" label="生产">
            <template slot-scope="scope">
              <span class="link-type">{{scope.row.url}}</span>
            </template>
          </el-table-column>

          <el-table-column prop="testurl" label="测试">
            <template slot-scope="scope">
              <span class="link-type">{{scope.row.testurl}}</span>
            </template>
          </el-table-column>
          <el-table-column prop="devurl" label="开发">
            <template slot-scope="scope">
              <span class="link-type">{{scope.row.devurl}}</span>
            </template>
          </el-table-column>
          <el-table-column
            prop="detail"
            label="描述">
          </el-table-column>
        </el-table>
      </el-tab-pane>

    </el-tabs>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'
  import adminDashboard from './admin'
  import editorDashboard from './editor'

  export default {
    name: 'Dashboard',
    components: {adminDashboard, editorDashboard},
    data() {
      return {
        currentRole: 'adminDashboard',
        activeName: 'first',
        tableData: [
          {
            name: 'xxxx-xxxx',
            url: 'https://www.zeus.com/dashboard',
            qaurl: '',
            simurl: '',
            devurl: '',
            detail: '工作文档',
          },
        ]
      }
    },
    computed: {
      ...mapGetters([
        'roles'
      ])
    },
    created() {
      if (!this.roles.includes('admin')) {
        this.currentRole = 'editorDashboard'
      }
    },
    methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      },
      handleGoUrl(url) {
        window.open(url, '_blank');
      },
      tableRowClassName({row, rowIndex}) {
        if (rowIndex === 1) {
          return 'warning-row';
        } else if (rowIndex === 3) {
          return 'success-row';
        } else if (rowIndex === 5) {
          return 'info-row';
        } else if (rowIndex === 8) {
          return 'transp-row';
        } else if (rowIndex === 11) {
          return 'zzz-row';
        }else if (rowIndex === 14) {
          return 'success-row';
        }
        return '';
      }
    }
  }
</script>
<style>
  .el-table .warning-row {
    background: oldlace;
  }

  .el-table .success-row {
    background: #f0f9eb;
  }

  .el-table .info-row {
    background: #ccffff;
  }

  .el-table .transp-row {
    background: #cce5ff;
  }

  .el-table .zzz-row {
    background: #ffccff;
  }

</style>
