
<!--<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <button @click="$store.dispatch('login', credentials)">로그인</button>
  </div>  
</template>-->

<template>
  <div>
    <div class='d-flex justify-content-center' id='imgdiv'>
      <img src="@/assets/login.png" alt="" id="loginImg">
    </div>
    <div class="container d-flex justify-content-center">
      <form @submit="onSubmit">
        <div class="mb-4">
          <input placeholder="ID" class="form-control" type="text" id="idInput" v-model="credentials.username">
          <div class="form-text">We'll never share your ID with anyone else.</div>
        </div>
        <div class="mb-4">
          <input placeholder="Password" class="form-control" type="password" id="passwordInput" v-model="credentials.password">
        </div>
        <button class="btn" id="loginbtn">로그인</button>
        <div class="mt-3">
          <a :href="kakao_URL"><img src="@/assets/kakao_login.png" alt=""></a>
        </div>
      </form>
    </div>
    <div>
    </div>
  </div>
</template>



<script>
// import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      },
      kakao_URL : `https://kauth.kakao.com/oauth/authorize?client_id=0ba410c0f796197638aeaf933efde905&redirect_uri=http://localhost:8080/&response_type=code`
    }
  },
  methods: {
    onSubmit: function(event) {
      event.preventDefault()
      this.$store.dispatch('login', this.credentials)
    }
  },
  
}
</script>

<style>
#loginImg{
  width: 300px;
  height: 100px;
}

#imgdiv{
  padding: 71px 0px 35px 0px;
}

#idInput, #passwordInput, #passwordConfirmationInput {
  width: 500px;
  height: 50px;
  border-block: 1px;
}

#loginbtn {
  width: 500px;
  height: 50px;
  color: #262223;
  font-size: 25px;
  background-color: #DDC6B6;
}
</style>