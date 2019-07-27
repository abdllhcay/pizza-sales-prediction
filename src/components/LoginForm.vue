<template>
  <div>
    <b-form  @submit.prevent="login">
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
      <b-button block type="submit" variant="primary">Login</b-button>
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
      login: function () {
        let username = this.form.username 
        let password = this.form.password
        this.$store.dispatch('login', { username, password })
        .then(() => this.$router.push('/'))
        .catch(err => console.log(err))
      }
    }
  }
</script>