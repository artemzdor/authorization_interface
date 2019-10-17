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
      let dataForSend = {
        login: document.getElementById('Login').value,
        password: document.getElementById('Password').value,
        repPass: document.getElementById('RepiatePassword').value
      }
      if ((!!dataForSend.login && !!dataForSend.password && !!dataForSend.repPass) && (dataForSend.password === dataForSend.repPass)) {
        this.$store.dispatch('registration', dataForSend)
          .then(result => {
            console.log('result',result)
            if (result.data.status === 200) {
              document.cookie = `session=${result.data.session}; max-age=${result.data.tm / 1000}`
              this.$router.push('lk')
            } else {
              alert(`Регистрация не удалась`)
            }
          })
          .catch(err => {
            alert(`Регистрация не удалась`)
          })
      } else {
        alert('Введены не все данные или пароли не совпадают')
      }
    }
  }
}
</script>
