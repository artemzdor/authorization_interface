<template>
  <div class="Registration">
    <form class="Registration-Form">
        <label class="Registration-Label">Логин</label>
        <input class="Registration-Input" type="text" name="Login" id='Login'>
        <label class="Registration-Label">Пароль</label>
        <input class="Registration-Input" type="password" name="Password" id='Password'>
        <label class="Registration-Label">Повторите пароль</label>
        <input class="Registration-Input" type="password" name="RepiatePassword" id='RepiatePassword'>
        <button class="Registration-Button" v-on:click = 'reg'>Регистрация</button>
      </form>
  </div>
</template>

<style type="text/css">
  .Registration-Form {
    width: 300px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
  }
  .Registration-Label {
    font-size: 16px;
    margin-bottom: 10px;
  }
  .Registration-Input {
    padding: 5px;
    font-size: 20px;
    margin-bottom: 15px;
  }
  .Registration-Button {
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
    reg (event) {
      event.preventDefault()
      let data = {
        login: document.getElementById('Login').value,
        password: document.getElementById('Password').value,
        repPass: document.getElementById('RepiatePassword').value
      }
      if ((!!data.login && !!data.password && !!data.repPass) && (data.password === data.repPass)) {
        this.$store.dispatch('registration', data)
          .then(data => {
            console.log(data)
          })
          .catch(data => {
            console.log(data)
          })
      } else {
        alert('Введены не все данные или пароли не совпадают')
      }
    }
  }
}
</script>
