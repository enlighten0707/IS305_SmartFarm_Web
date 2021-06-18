<template>
  <div class="dashboard-editor-container">
    <panel-group @handleSetLineChartData="handleSetLineChartData" />
    
    <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:32px;">
      <line-chart :chart-data="lineChartData" />
    </el-row>

  </div>
</template>

<script>
import GithubCorner from '@/components/GithubCorner'
import PanelGroup from './components/PanelGroup'
import LineChart from './components/LineChart'
import RaddarChart from './components/RaddarChart'
import PieChart from './components/PieChart'
import BarChart from './components/BarChart'
import TransactionTable from './components/TransactionTable'
import TodoList from './components/TodoList'
import BoxCard from './components/BoxCard'

// const lineChartData = {
//   price: {
//     expectedData: [590, 592, 600, 630, 610, 620, 600],
//     dim: '$',
//   },
//   change_num: {
//     expectedData: [9.9, 9.2, 9.5, 10.2, 9.7, 9.8, 10],
//     dim: '$',
//   },
//   change_ratio: {
//     expectedData: [0.8, 1.1, 1.2, 1.0, 0.9, 1.3, 1.5],
//     dim: '%',
//   },
//   shoppings: {
//     expectedData: [19.5, 20.5, 20.3, 18.9, 20.2, 19, 20],
//     dim:'万',
//   },
//   // humidity_soil: {
//   //   expectedData: [1230, 140, 141, 142, 145, 150, 160],
//   //   dim:'%',
//   // },
//   // rain: {
//   //   expectedData: [130, 140, 141, 142, 145, 150, 160],
//   //   dim:'%',
//   // }
// }

import axios from 'axios'
export default {
  name: 'DashboardAdmin',
  components: {
    GithubCorner,
    PanelGroup,
    LineChart,
    RaddarChart,
    PieChart,
    BarChart,
    TransactionTable,
    TodoList,
    BoxCard
  },
  data() {
    return {
      // lineChartData: lineChartData.price,
      lineChartData: {
        expectedData: [],
        dim: '',
      }
    }
  },
  methods: {
    handleSetLineChartData(type) {
      // this.lineChartData = lineChartData[type]
      this.lineChartData.expectedData = [1,2,3];
      this.lineChartData.dim='$';
      console.log(this.lineChartData);
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;

  .github-corner {
    position: absolute;
    top: 0px;
    border: 0;
    right: 0;
  }

  .chart-wrapper {
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
}

@media (max-width:1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>
