<template>
  <div class="create">
    <b-container class="bv-example-row">
      <b-row>
        <b-col sm="4" offset="4">
          <h1 class="mt-4 mb-4">Create Task</h1>
          <TaskForm/>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import TaskForm from '@/components/TaskForm.vue'

export default {
  name: 'create',
  components: {
    TaskForm,
  }
}
</script>
