<template>
<div class="Main">
  <NavBar></NavBar>
  <dashboard></dashboard>
</div>
</template>

<script>
import NavBar from './NavBar'
import dashboard from './Dashboard'

export default {
  components: {
    NavBar,
    dashboard
  }
}
</script>

