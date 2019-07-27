<template>
  <div class="result">
    <b-container class="bv-example-row">
      <b-row>
        <b-col sm="8" offset="2">
          <h1 class="mt-4 mb-4">Task Result</h1>
          <b-col sm="4">
            <b-form-select v-model="selectedCategory" :options="categoryOptions" @change="changeCategory">
            </b-form-select>
          </b-col>
          <apexchart type="line" :options="options" :series="series"></apexchart>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'
import VueApexCharts from 'vue-apexcharts'

export default {
  name: 'result',
  components: {
    apexchart: VueApexCharts,
  },
  data(){
    return{
      categories: [],
      selectedCategory: "Category",
      categoryOptions: [],
      result: [],
      resultDates: [],
      resultData: [],
      JSONResult: null,
      id: 0,
      options: {
        chart: {
          id: 'vuechart-example'
        },
        xaxis: {
          categories: [""]
        }
      },
      series: [{
        name: 'Pizza',
        data: [""]
      }]
    }
  },
    created(){
      this.id = this.$route.params.id;
      this.getTask()
    },
    methods:{
      getTask(){
        axios
        .get(`http://localhost:5000/api/tasks/${this.id}`)
        .then(response => {
          this.result = response.data[0].result
          this.JSONResult = JSON.parse(this.result)
          this.categories = Object.keys(this.JSONResult)
          this.categories = ["Category"].concat(this.categories)
          
          this.categoryOptions = this.categories 
        })
      },
      changeCategory(){
        this.resultData = []
        this.resultDates = []
        this.result = this.JSONResult[this.selectedCategory].split("\n")

        for(var i = 0; i < this.result.length-1; i++){
          var element = this.result[i].replace(/\s\s+/g, ' ').split(' ')
          this.resultDates.push(element[0])
          this.resultData.push(element[1].split(".")[0])
          }

        this.updateChart()
      },
      updateChart(){
        this.series = [{
          data: this.resultData
        }]
        this.options = {
          xaxis: {
            categories: this.resultDates
          }
        }
      }
    }
}
</script>