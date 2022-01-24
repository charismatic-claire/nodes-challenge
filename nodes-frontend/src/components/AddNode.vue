<template>
  <div id="add-node">
    <h1>{{ heading }}</h1>
    <div class="dialog">
      <div class="left">
        <p>Please select a node:</p>
        <select v-model="selectedNode">
          <option disabled value="">Pick a node</option>
          <option v-for="option in options" :key="option.name" :value="option">
            {{ option.name }}
          </option>
        </select>
        <p>Please set a description (string):</p>
        <input v-model="description" placeholder="Your description here">
        <p>Set a predecessor (integer):</p>
        <input v-model="predecessor" placeholder="Your predecessor here">
      </div>
      <div class="right">
        <button type="button" class="submit" @click="submit" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "AddNode",
  props: {
    heading: String
  },
  data() {
    return {
      options: [
        { type: 'Source', name: 'CSV Reader' },
        { type: 'Source', name: 'Table Reader' },
        { type: 'Sink', name: 'CSV Writer' },
        { type: 'Sink', name: 'Table Writer' },
        { type: 'Manipulator', name: 'Column Filter' },
        { type: 'Manipulator', name: 'Row Filter' },
        { type: 'Manipulator', name: 'Row Sampling'},
        { type: 'Visualizer', name: 'Scatter Plot' },
        { type: 'Visualizer', name: 'Table View' },
        { type: 'Predictor', name: 'XGBoost Predictor'},
        { type: 'Predictor', name: 'Naive Bayes Predictor'},
        { type: 'Learner', name: 'XGBoost Tree Ensemble Learner' },
        { type: 'Learner', name: 'Naive Bayes Learner' }
      ],
      selectedNode: '',
      description: '',
      predecessor: null
    }
  },
  methods: {
    reset() {
      this.selectedNode = ''
      this.description = ''
      this.predecessor = null
    },
    async submit() {
      let node = this.selectedNode
      node.description = this.description
      node.predecessor = this.predecessor
      const url = '/api/nodes'
      console.log('POST <' + JSON.stringify(node) + '> to <' + url + '>')
      const response = await axios.post(url, node)
      console.log(response.data)
      this.reset()
      this.$emit('updated')
    }
  }
}
</script>

<style scoped>
.dialog {
  border: 1px solid gray;
  border-radius: 8px;
  padding: 16px;
  margin: 16px 0px;
  overflow: hidden;
}
.left {
  float: left;
  margin: 16px
}
.right {
  float: right;
  margin: 16px
}
.right button {
  margin-left: 10px;
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 4px;
  background-color: white;
  opacity: 0.5;
}
.right .submit {
  background-image: url(../assets/ok_button.png);
}
.right .submit:hover {
  opacity: 1.0;
}
</style>
