<template>
  <div class="aa">
    <NotifyScroll :lists="list" class="scrollContainer"/>
  </div>
</template>
<script>
  import NotifyScroll from "@/components/NotifyScroll"

  export default {
    components: {NotifyScroll},
    data() {
      return {
        list: ["欢迎大家来一起学习", "在一起学习", "一起学习", "学无止境"]
      };
    }
  };
</script>
<style scoped>
  /*样式的话可以写*/
  .scrollContainer {
    /* color: red; */
    font-size: 16px;
    margin-left: 10px;
    width: 500px;
    height: 30px;
    border: 1px solid #000;
    line-height: 30px;
    overflow: hidden;
  }
</style>
