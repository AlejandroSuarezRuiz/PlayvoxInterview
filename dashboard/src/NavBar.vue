<template>
  <div id="app">
    <nav class="navbar is-light" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item">
          <img src="./assets/playvox.png" width="115" height="32">
        </a>

        <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
          <a class="navbar-item">
            Home
          </a>

          <a class="navbar-item">
            Dashboard
          </a>

          <a class="navbar-item">
            About
          </a>
        </div>
      </div>
    </nav>
    
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  data () {
    return {
      msg: 'Playvox Navbar.'
    }
  }
}
</script>

<style>
</style>