<template>
  <div>
    <b-form @submit="onSubmit">
      <b-form-group>
        <b-form-input
          id="name-input"
          v-model="form.name"
          required
          placeholder="Name"
        ></b-form-input>
      </b-form-group>

      <b-form-group>
        <b-form-file
          id="file-input"
          v-model="form.file"
          required
          placeholder="File"
          drop-placeholder="Drop file here..."
        ></b-form-file>
      </b-form-group>

      <b-form-group>
        <b-form-input
          id="step-input"
          v-model="form.step"
          type="number"
          required
          placeholder="Prediction step (months)"
        ></b-form-input>
      </b-form-group>

      <b-button block type="submit" variant="primary">Create</b-button>
    </b-form>
  </div>
</template>

<script>
  import axios from 'axios'

  const baseDomain = "http://localhost:5000"
  const baseUrl = `${baseDomain}/api/tasks/`

  export default {
    data() {
      return {
        form: {
          name: '',
          file: null,
          step: null
        }
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        axios
        .post(baseUrl, {
          name: '' + this.form.name,
          step: '' + this.form.step,
          file_path: '' + this.form.file.name
        })
        .then(() => {
          this.$router.push('/')
        })
      }
    }
  }
</script>