<template>
  <div id="app">
    <NodesList heading="A list of all nodes" :nodes="nodes" @updated="fetchNodes"/>
    <AddNode heading="Add a new node" @updated="fetchNodes"/>
  </div>
</template>

<script>
import axios from 'axios'
import NodesList from './components/NodesList.vue'
import AddNode from './components/AddNode'

export default {
  name: 'App',
  components: {
    NodesList,
    AddNode
  },
  data() {
    return {
      nodes: [],
    }
  },
  methods: {
    fetchNodes() {
      console.log('GET \'.../api/nodes\'')
      axios.get('/api/nodes')
          .then(response => {
            console.log(response.data)
            this.nodes = response.data
          })
    }
  },
  mounted() {
    this.fetchNodes()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 64px auto;
  min-width: 512px;
  max-width: 768px;
}
</style>
