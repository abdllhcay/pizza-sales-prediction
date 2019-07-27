<template>
  <div class="home">
    <b-container class="bv-example-row">
      <b-row>
        <b-col sm="4" offset="4">
          <h1 class="mt-4 mb-4">Login</h1>
          <LoginForm/>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'

export default {
  name: 'login',
  components: {
    LoginForm
  }
}
</script>
