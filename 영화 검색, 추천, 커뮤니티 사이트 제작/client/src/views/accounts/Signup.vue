<!--<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation">
    </div>
    <button @click="$store.dispatch('signup', credentials)">회원가입</button>
  </div>
</template> -->

<template>
  <div>
    <div class='d-flex justify-content-center' id='imgdiv'>
      <img src="@/assets/signin.png" alt="" id="loginImg">
    </div>
    <div class="container d-flex justify-content-center">
      <form @submit="onSubmit">
        <div class="mb-4">
          <input size='50' placeholder="ID" type="text" id="idInput" v-model="credentials.username">
          <div id="emailHelp" class="form-text">We'll never share your ID with anyone else.</div>
        </div>
        <div class="mb-4">
          <input placeholder="Password" type="password" id="passwordInput" v-model="credentials.password">
        </div>
        <div class="mb-4">
          <input placeholder="PasswordConfirmation" type="password" id="passwordConfirmationInput" v-model="credentials.passwordConfirmation">
        </div>

        <button class="btn" id="signupbtn">회원가입</button>
      </form>
    </div>
  </div>
</template>



<script>
// import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },

  methods: {
    onSubmit: function(event) {
      event.preventDefault()
      this.$store.dispatch('signup', this.credentials)
    }
  }

}
</script>

<style>
#signupbtn{
  width: 500px;
  height: 50px;
  color: #262223;
  font-size: 25px;
  background-color: #DDC6B6;
}
</style>