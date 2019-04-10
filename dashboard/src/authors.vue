<template>
    <div class="app">
        <center> 
        <div class="box">
            <div class="card">
            <div class="card-content">
                <p class="title">
                Books
                </p>
                <p class="subtitle">
                TOP 5 - Authors with most book sells
                </p>
            </div>
            
            <div class="card-content">
                <div class="content small">
                    <authorsChartD v-if="loaded" :chart-data="authors" :chart-labels="labels"></authorsChartD>
                </div>
            </div>

            <footer class="card-footer">
                <p class="card-footer-item">
                    <button class="button is-success is-outlined" 
                    v-on:click="requestData()"
                    @click.prevent
                    v-bind:disabled="CBdisabled"
                    v-bind:class="{'is-loading':CBloading}">Consult</button>
                </p>
            </footer>
            </div>
        </div>
        </center>
    </div>
</template>

<script>
    import axios from 'axios'
    import authorsChartD from './authorsChartD'

    export default {
        components: {authorsChartD},
        data () {
        return {
            loaded: false,
            CBdisabled: false,
            CBloading: false,
            authors: [],
            labels: []
        }
        },
        methods: {
            resetState () {
                this.loaded = false
            },
            requestData () {
                this.resetState()
                this.CBdisabled = true
                this.CBloading = true
                axios.get(`http://localhost:5000/api/authors`)
                .then(response => {
                    var ans = JSON.parse(response.data)
                    console.log(ans[0]["_id"])
                    for(var i=0;i<5;i++){
                        this.labels[i] = ans[i]["_id"]
                        this.authors[i] = ans[i]["copies"]["$numberDecimal"]
                    }
                    this.CBdisabled = false
                    this.CBloading = false
                    this.loaded = true
                })
                .catch(err => {
                    swal("Problem connecting with the server.","There's some problems, please check it...","error")
                })
            }
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