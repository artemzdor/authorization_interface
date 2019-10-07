<template>
  <div class="home">
    <div class="Menu">
      <router-link to='/login'>Логин</router-link>
      <router-link to='/registration'>Регистрация</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
  .Menu {
    width: 200px;
    margin: 0 auto;
    display: -webkit-flex;
    display: -moz-flex;
    display: -ms-flex;
    display: -o-flex;
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px
  }
</style>

<script>
export default {
  name: 'home'
}
</script>
