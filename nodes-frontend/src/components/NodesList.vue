<template>
  <div id="nodes-list">
    <h1>{{ heading }}</h1>
    <Node v-for="node in nodes" :key="node.id" :node="node" @updated="forwardToParent"/>
  </div>
</template>

<script>
import Node from './Node.vue'

export default {
  name: "NodeList",
  components: {
    Node
  },
  props: {
    heading: String,
    nodes: Array
  },
  methods: {
    forwardToParent() {
      this.$emit('updated')
    }
  }
}
</script>

<style scoped>

</style>