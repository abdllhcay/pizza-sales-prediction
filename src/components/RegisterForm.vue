<template>
  <div>
    <b-form  @submit.prevent="register">
      <b-form-group>
        <b-form-input
          v-model="form.username"
          required
          placeholder="Username"
        ></b-form-input>
      </b-form-group>
      <b-form-group>
        <b-form-input
          v-model="form.password"
          required
          placeholder="Password"
          type="password"
        ></b-form-input>
      </b-form-group>
      <b-button block type="submit" variant="primary">Register</b-button>
    </b-form>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        form: {
          username: "",
          password: "",
        }
      }
    },
    methods: {
      register: function () {
        let data = {
          username: this.form.username,
          password: this.form.password,
        }
        this.$store.dispatch('register', data)
        .then(() => this.$router.push('/'))
        .catch(err => console.log(err))
      }
    }
  }
</script>