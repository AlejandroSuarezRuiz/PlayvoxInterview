<template>
    <div class="app">
        <center> 
        <div class="box">
            <div class="card">
            <div class="card-content">
                <p class="title">
                Salaries
                </p>
                <p class="subtitle">
                    Salaries below 1000000 COP (Red)
                </p>
            </div>
            
            <div class="card-content">
                <div class="content small">
                    <salariesChartD v-if="loaded" :chart-data="salaries" :chart-labels="labels" :back-color="colors"></salariesChartD>
                </div>
            </div>

            <div class="card-content" v-if="loaded">
                <p class="subtitle">
                    Currency converter from USD to COP: {{ cValue }}
                </p>
            </div>

            <footer class="card-footer">
                <p class="card-footer-item">
                    <button class="button is-success is-outlined" 
                    v-on:click="getAuthors()"
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
    import salariesChartD from './salariesChartD'

    export default {
        components: {salariesChartD},
        data () {
        return {
            loaded: false,
            cValue: null,
            CBdisabled: false,
            CBloading: false,
            targetSalary: 1000000,
            salaries: [],
            labels: [],
            colors: []
        }
        },
        methods: {
            resetState () {
                this.loaded = false
            },
            getAuthors () {
                axios.get(`https://free.currencyconverterapi.com/api/v6/convert?q=USD_COP&compact=ultra&apiKey=a0771d0998840fa4d754`)
                .then(response => {
                    this.CBdisabled = true
                    this.CBloading = true
                    this.cValue = Number(response.data.USD_COP)
                    this.requestData()
                })
                .catch(err => {
                    swal("Problem connecting with currency API.","There's some problems connecting with the currency converter API, please check it...","error")
                    this.CBdisabled = false
                    this.CBloading = false
                })
            },
            requestData () {
                this.resetState()
                axios.get(`http://localhost:5000/api/salaries`)
                .then(response => {
                    var ans = JSON.parse(response.data)
                    for(var i = 0;i<8;i++){
                        var salary = Number(Number(ans[i]["averageQuantity"]["$numberDecimal"]).toFixed(2))
                        this.salaries[i] = salary
                        if(salary<(this.targetSalary/this.cValue)){
                            this.colors[i] = "#CB5757"
                        } else {
                            this.colors[i] = "rgba(87, 131, 203, 0.6)"
                        }
                    }
                    this.labels = ["Area1","Area2","Area3","Area4","Area5","Area6","Area7","Area8"]
                    this.loaded = true
                    this.CBdisabled = false
                    this.CBloading = false
                })
                .catch(err => {
                    swal("Problem connecting with the server.","There's some problems, please check it...","error")
                    this.CBdisabled = false
                    this.CBloading = false
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