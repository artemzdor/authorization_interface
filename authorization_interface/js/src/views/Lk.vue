<template>
  <div class="Lk">
    <label for="" class="Lk-Label">Новый пароль</label>
    <input type="text" v-model="newPass" class="Lk-Input" id='NewPass'>
    <label for="" class="Lk-Label">Повтор нового пароля</label>
    <input type="text" class="Lk-Input" id='RepNewPass'>
    <label for="" class="Lk-Label">Старый пароль</label>
    <input type="text" v-model='oldPass' class="Lk-Input" id='OldPass'>
    <div>
      <button v-on:click = 'changePassword'>Изменить пароль</button>
      <button v-on:click = 'logOut'>Выйти</button>
    </div>
  </div>
</template>

<style lang="stylus">
.Lk
  width 300px
  margin 0 auto
  display flex
  flex-direction column
</style>

<script>
function getCookie (name) {
  // eslint-disable-next-line
  let matches = document.cookie.match (new RegExp(
    // eslint-disable-next-line
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ))
  return matches ? decodeURIComponent(matches[1]) : undefined
}

function deleteCookie (name) {
  document.cookie = `${name}=''; max-age=-1`
}

export default {
  data () {
    return {
      newPass: '',
      oldPass: ''
    }
  },
  methods: {
    changePassword () {
      let dataForSend = {
        session: getCookie('session'),
        newPass: this.newPass,
        oldPass: this.oldPass
      }
      this.$store.dispatch('changePassword', dataForSend)
        .then(response => {
          if (response.data.status === 200) {
            alert('Пароль изменен')
          } else {
            alert('Пароль не изменен')
          }
        })
        .catch(err => {
          alert('Пароль не изменен', err)
        })
    },
    logOut () {
      let dataForSend = {
        session: getCookie('session')
      }
      this.$store.dispatch('logOut', dataForSend)
        .then(response => {
          console.log('logout', response.data.status)
          if (response.data.status === 200) {
            deleteCookie('session')
            this.$router.push('/')
          } else {
            alert('Выход не удался')
          }
        })
        .catch(err => {
          console.log(err)
          alert('Выход не удался', err)
        })
    }
  }
}
</script>
