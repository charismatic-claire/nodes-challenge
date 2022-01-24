<template>
  <div class="node">
    <div class="viewer" v-show="showViewer">
      <div class="item">
        <h2>{{ node.name }} (#{{ node.id }})</h2>
        <div class="box-wrapper">
          <div class="number">
            <p>{{ node.predecessor }}</p>
          </div>
          <div class="right-arrow" :class="{ background: hasPredecessor }"/>
          <div class="box" :style="{ backgroundColor: boxColor }"/>
          <div class="right-arrow" :class="{ background: hasSuccessor }"/>
        </div>
        <p>{{ node.description }}</p>
      </div>
      <div class="buttons">
        <button type="button" class="edit" @click="editNode" />
        <button type="button" class="delete" @click="deleteNode" />
      </div>
    </div>
    <div id="editor" v-show="showEditor">
      <div class="item">
        <h2>{{ node.name }} (#{{ node.id }})</h2>
        <p>Update description (string):</p>
        <input v-model="description" :placeholder="description">
        <p>Update predecessor (integer):</p>
        <input v-model="predecessor" :placeholder="predecessor">
      </div>
      <div class="buttons">
        <button type="button" class="submit" @click="closeEditor" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "Node",
  props: {
    node: Object,
  },
  data() {
    return {
      showViewer: true,
      showEditor: false,
      description: '',
      predecessor: ''
    }
  },
  methods: {
    async deleteNode() {
      const url = '/api/nodes/' + this.node.id + '/'
      console.log('DELETE <' + url + '>')
      const response = await axios.delete(url)
      console.log(response.data)
      this.$emit('updated')
    },
    editNode() {
      console.log('Editor should appear for node <{(' + this.node.id + ') ' + this.node.name + '>')
      this.showViewer = false
      this.showEditor = true
    },
    closeEditor() {
      console.log('Editor should disappear for node <{(' + this.node.id + ') ' + this.node.name + '>')
      let node = this.node
      node.description = this.description
      node.predecessor = this.predecessor
      this.updateNode(node)
      this.showViewer = true
      this.showEditor = false
    },
    async updateNode(node) {
      const url = '/api/nodes'
      console.log('PUT <' + JSON.stringify(node) + '> to <' + url + '>')
      const response = await axios.put(url, node)
      console.log(response.data)
      this.$emit('updated')
    }
  },
  computed: {
    boxColor() {
      switch (this.node.type) {
        case 'Source':
          return '#ff9632'
        case 'Manipulator':
          return '#ffd200'
        case 'Visualizer':
          return '#4ba1bf'
        case 'Sink':
          return '#ff4b4b'
        case 'Learner':
          return '#c8e632'
        case 'Predictor':
          return '#41be78'
        default:
          return 'grey'
      }
    },
    hasPredecessor() {
      switch (this.node.type) {
        case 'Source':
          return false
        default:
          return true
      }
    },
    hasSuccessor() {
      switch (this.node.type) {
        case 'Sink':
          return false
        default:
          return true
      }
    }
  },
  mounted() {
    this.description = this.node.description
    this.predecessor = this.node.predecessor
  }
}
</script>

<style scoped>
.node {
  border: 1px solid gray;
  border-radius: 8px;
  padding: 16px;
  margin: 16px 0px;
  overflow: hidden;
}
.item {
  float: left;
  margin: 16px
}
.buttons {
  float: right;
  margin: 16px;
}
.buttons button {
  margin-left: 10px;
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 4px;
  background-color: white;
  opacity: 0.5;
}
.buttons .edit {
  background-image: url(../assets/edit_button.png);
}
.buttons .delete {
  background-image: url(../assets/delete_button.png);
}
.buttons .submit {
  background-image: url(../assets/ok_button.png);
}
.buttons .edit:hover, .buttons .delete:hover, .buttons .submit:hover {
  opacity: 1.0;
}
.box {
  width: 64px;
  height: 64px;
  border-radius: 8px;
}
.box-wrapper {
  overflow: hidden;
}
.box-wrapper div {
  float: left;
}
.right-arrow {
  margin-top: 24px;
  width: 14px;
  height: 16px;
}
.right-arrow.background {
  background-image: url(../assets/arrow_right.png);
}
.number {
  margin-top: 24px;
  margin-right: 8px;
  min-width: 14px;
  height: 16px;
}
.number p {
  margin: 0px;
}

</style>