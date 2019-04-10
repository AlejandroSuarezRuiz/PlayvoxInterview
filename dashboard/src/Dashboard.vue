<template>
    <div class="app">
        <center> 
        <div class="columns is-vcentered">
            <div class="column">
                <authors></authors>
            </div>

            <div class="column">
                <logs></logs>
            </div>
        </div>
        
        <salaries></salaries>

        </center>
    </div>
</template>

<script>
import salaries from './salaries'
import authors from './authors'
import logs from './logs'
export default {
  components: {
    salaries,
    authors,
    logs
  }
}
</script>

<style>
  .small {
    max-width: 600px;
  }
  .input{
    margin: 10px;
  }
</style>

