<template>
    <div class="console" id="terminal" style="height: 800px"></div>
</template>
<script>
  import Terminal from './Xterm'
  import * as fit from "xterm/lib/addons/fit/fit"
  import 'xterm/dist/xterm.css'
  import {isRealObj} from '@/utils'

  export default {
    name: 'Console',
    props: {
      terminal: {
        type: Object,
        default: {}
      },
      consoleurl: {
        type: String,
        required: true
      }
    },
    data() {
      return {
        term: null,
        terminalSocket: null
      }
    },
    methods: {
      init() {
        let terminalContainer = document.getElementById('terminal')
        terminalContainer.style.width = this.terminal.width;
        terminalContainer.style.height = this.terminal.height;
        this.term = new Terminal();
        this.term.open(terminalContainer)
        this.terminalSocket = new WebSocket(this.consoleurl)
        this.terminalSocket.onopen = this.runRealTerminal
        this.terminalSocket.onclose = this.closeRealTerminal
        this.terminalSocket.onerror = this.errorRealTerminal
        this.term.attach(this.terminalSocket)
        this.term._initialized = true
      },
      runRealTerminal() {
        this.terminalSocket.send("su - zeus_RD\nclear\n");
        console.log('webSocket is finished')
      },
      errorRealTerminal() {
        console.log('error')
      },
      closeRealTerminal() {
        if (this.terminalSocket != null) {
          this.terminalSocket.close()
          this.terminalSocket = null
        }
        if (this.term != null) {
          this.term.destroy()
          this.term = null
        }
        this.$emit("handleCancel")
      }
    },
    mounted() {
      let terminalContainer = document.getElementById('terminal')
      terminalContainer.style.width = window.screen.availWidth;
      terminalContainer.style.height = window.screen.availHeight;
      console.log(terminalContainer)

      this.term = new Terminal();
      this.term.open(terminalContainer, true);
      console.log(this.term)
      // open websocket
      // let socket = new WebSocket(`ws://*******command=env&command=TERM%3Dxterm&command=COLUMNS%3D${term.cols}&command=LINES%3D${rows}&command=/bin/bash&********`,"channel.k8s.io");
      var wsurl=this.consoleurl
      console.log("wsur--->",wsurl)
      this.terminalSocket = new WebSocket(wsurl)
      this.terminalSocket.onopen = this.runRealTerminal
      this.terminalSocket.onclose = this.closeRealTerminal
      this.terminalSocket.onerror = this.errorRealTerminal

      this.term.attach(this.terminalSocket)
      this.term._initialized = true
      console.log('mounted is going on')
    },
    beforeDestroy() {
      this.terminalSocket.close()
      this.term.destroy()
    }
  }
</script>
