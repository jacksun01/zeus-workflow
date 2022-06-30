<template>
  <div class="wrap">
    <ul id="marquee">
      <li v-for="(item,index) in lists" :key="index">{{item}}</li>
    </ul>
  </div>
</template>
<script type="text/ecmascript-6">
  import {isRealObj} from "../../utils";

  export default {
    name: "NotifyScroller",
    props: ["lists"], // 父组件传入数据， 数组形式
    data() {
      return {
        timer:undefined,
      }
    },
    watch: {
      lists: {
        handler() {
          this.init()
        },
        immediate: true
      }
    },
    methods: {
      init(){
        console.log("----init----------------->",this.lists,this.timer)
        if(isRealObj(this.timer)){
          clearInterval(this.timer);
          this.timer=undefined
          this.move()
        }
      },
      move() {
        // 获取内容区宽度
        let width = document.getElementById("marquee").scrollWidth;
        let leftstart=width*0.60
        let marquee = document.getElementById("marquee");
        let speed = 600; // 位移距离
        // 设置位移
        this.timer =setInterval(function () {
          speed = speed - 1;
          // 如果位移超过文字宽度，则回到起点
          if (-speed >= (width-leftstart)) {
            speed = 600;
          }
          console.log(speed)
          marquee.style.transform = "translateX(" + speed + "px)";
        }, 60);
      }
    },
    mounted: function () {
      this.move();
    }
  };
</script>
<style scoped>
  /*样式的话可以写*/
  .wrap {
    overflow: hidden;
    color: red;
  }

  #box {
    height: 100%;
  }

  ul,
  li {
    margin: 0;
    padding: 0;
  }

  ul {
    white-space: nowrap;
    margin: 0 10px;
  }

  li {
    height: 100%;
    list-style: none;
    margin-right: 10px;
    display: inline-block;
  }
</style>
