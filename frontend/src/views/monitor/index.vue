<template>
<div>
    <el-row :gutter="60">
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="margin-left:250px;font-size:20px">温室监控</span>
          </div>
          <div>
            <img :src="require('@/assets/monitor_videos/monitor_01.gif')">
          </div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="margin-left:250px;font-size:20px">采摘苹果</span>
          </div>
          <div>
            <img :src="require('@/assets/monitor_videos/monitor_02.gif')">
          </div>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="60">
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="margin-left:250px;font-size:20px">种子培育</span>
          </div>
          <div>
            <img :src="require('@/assets/monitor_videos/monitor_03.gif')">
          </div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="margin-left:250px;font-size:20px">无水栽培</span>
          </div>
          <div>
            <img :src="require('@/assets/monitor_videos/monitor_04.gif')">
          </div>
        </el-card>
      </el-col>
    </el-row>
   

    
      <el-row :gutter="60">
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="margin-left:270px;font-size:20px">监控点1</span>
          </div>
          <div>
            <img :src="require('@/assets/monitor_videos/monitor_05.gif')">
          </div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="margin-left:270px;font-size:20px">监控点2</span>
          </div>
          <div>
            <img :src="require('@/assets/monitor_videos/monitor_06.gif')">
          </div>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="60">
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="margin-left:270px;font-size:20px">监控点3</span>
          </div>
          <div>
            <img :src="require('@/assets/monitor_videos/monitor_07.gif')">
          </div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="margin-left:270px;font-size:20px">监控点4</span>
          </div>
          <div>
            <img :src="require('@/assets/monitor_videos/monitor_08.gif')">
          </div>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="60">
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="margin-left:280px;font-size:20px">番茄</span>
          </div>
          <div>
            <img :src="require('@/assets/monitor_videos/monitor_09.jpg')" style="height:400px">
          </div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="margin-left:280px;font-size:20px">秋葵</span>
          </div>
          <div >
            <img :src="require('@/assets/monitor_videos/monitor_10.jpg')" style="height:400px">
          </div>
        </el-card>
      </el-col>
    </el-row>

 </div>
</template>

<script>
</script>

<style>
.img{
    display: inline-block;
    margin-left:40px;
}
.el_card{
    padding: 0;
}
</style>