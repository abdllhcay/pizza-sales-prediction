<template>
  <div class="home">
    <b-container class="bv-example-row">
      <b-row>
        <b-col>
          <h1 class="mt-4 mb-4">Task List</h1>
          <TaskList/>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import TaskList from '@/components/TaskList.vue'

export default {
  name: 'home',
  components: {
    TaskList
  }
}
</script>
