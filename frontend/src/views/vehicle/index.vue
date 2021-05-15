<template>
<el-button icon="el-icon-question" type="primary" @click="guide">
  Show Guide
</el-button>
</template>

<script>

export default {
  name: 'Vehicle',
  methods: {
    guide() {
      console.log(1)
    }
  }
}
</script>

