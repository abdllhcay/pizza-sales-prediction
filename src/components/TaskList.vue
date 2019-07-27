<template>
  <div>
    <b-table 
      id="task-list"
      :items="tasks"
      :fields="fields"
      :current-page="currentPage"
      :per-page="perPage"
      responsive 
      striped 
      bordered 
    >

    <template slot="name" slot-scope="row">
        {{ row.value}}
    </template>

    <template slot="operation" slot-scope="data">
      <b-button size="sm" @click="predict(data.item, data.index)" class="mr-2" variant="primary">
        Start
      </b-button>
      <b-button size="sm" @click="result(data.item)" variant="success">
        Result
      </b-button>
    </template>

    </b-table>

    <b-row>
      <b-col md="6" class="my-1">
        <b-pagination
          v-model="currentPage"
          :total-rows="totalItems"
          :per-page="perPage"
          class="my-0"
        ></b-pagination>
      </b-col>
    </b-row>
  </div>
</template>

<script>
  import axios from 'axios'

  const baseDomain = "http://localhost:5000"
  const baseUrl = `${baseDomain}/api/tasks/`

  export default {
    data() {
      return {
        fields: [
          { key: "name", sortable: true },
          { key: "started", sortable: true },
          { key: "finished", sortable: true },
          { key: "status", sortable: true },
          { key: "operation", sortable: false }
        ],
        tasks: [],
        currentPage: 1,
        totalItems: 1,
        perPage: 8,
        id: 0
      }
    },
    created(){
      this.getTaskList()
    },
    methods:{
      getTaskList(){
        axios
        .get(baseUrl)
        .then(response => {
          this.tasks = response.data
          this.totalItems = this.tasks.length
        })
      },
      result(item) {
        this.id = item.id
        window.location.href = `/result/${this.id}`
      },
      predict(item, index){
        this.id = item.id
        this.tasks[index].status = "Continue"
        axios
        .post(`http://localhost:5000/api/predict/${this.id}`, {
        })
        .then(response => {
          if(response.data == "Success"){
            this.tasks[index].status = "Success"
          }
          else{
            this.tasks[index].status = "Failure"
          }
        })
      }
    }
  }
</script>