<template>
  <div class="Login">
    <form class="LoginForm">
      <label class="LoginForm-Label">Логин</label>
      <input class="LoginForm-Input" type="text" name="Login" id='Login'>
      <label class="LoginForm-Label">Пароль</label>
      <input class="LoginForm-Input" type="password" name="Password" id='Password'>
      <button class="LoginForm-Button" v-on:click = 'login'>Войти</button>
    </form>
  </div>
</template>

<style type="text/css">
  .LoginForm {
    width: 300px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
  }
  .LoginForm-Label {
    font-size: 16px;
    margin-bottom: 10px;
  }
  .LoginForm-Input {
    padding: 5px;
    font-size: 20px;
    margin-bottom: 15px;
  }
  .LoginForm-Button {
    background-color: white;
    border: 1px solid black;
    padding: 10px 0;
    font-size: 20px
  }
</style>

<script>
export default {
  name: 'login',
  methods: {
    login (event) {
      event.preventDefault()
      let dataForSend = {
        login: document.getElementById('Login').value,
        password: document.getElementById('Password').value
      }
      if (!!dataForSend.login && !!dataForSend.password) {
        this.$store.dispatch('login', dataForSend)
        .then(response => {
          if (response.data.status === 200) {
            document.cookie = `session=${response.data.session}; max-age=${response.data.tm / 1000}`
            this.$router.push('lk')
          }
        })
      } else {
        alert('Введены не все данные')
      }
    }
  }
}
</script>
