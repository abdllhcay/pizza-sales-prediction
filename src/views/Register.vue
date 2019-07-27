<template>
  <div class="home">
    <b-container class="bv-example-row">
      <b-row>
        <b-col sm="4" offset="4">
          <h1 class="mt-4 mb-4">Register</h1>
          <RegisterForm/>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import RegisterForm from '@/components/RegisterForm.vue'

export default {
  name: 'register',
  components: {
    RegisterForm
  }
}
</script>
