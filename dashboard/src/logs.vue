<template>
    <div class="app">
        <center> 
        <div class="box">
            <div class="card">
            <div class="card-content">
                <p class="title">
                Images insertion log
                </p>
                <p class="subtitle">
                Number of users with insertion between 1000 and 2000:
                </p>
            </div>
            
            <div class="card-content">
                <p class="is-size-1 has-text-info" v-if="loaded">{{ logs }}</p>
            </div>

            <div class="card-content"  v-if="fetched">
                <p class="subtitle">
                    Fetched date: {{ fDate }}
                </p>
            </div>

            <footer class="card-footer">
                <p class="card-footer-item">
                    <button class="button is-success is-outlined"
                    v-on:click="consulteData()"
                    @click.prevent 
                    v-bind:disabled="CBdisabled"
                    v-bind:class="{'is-loading':CBloading}">Consult</button>
                </p>
                <p class="card-footer-item">
                    <button class="button is-info is-outlined" 
                    v-on:click="requestData()"
                    @click.prevent
                    v-bind:disabled="PBdisabled"
                    v-bind:class="{'is-loading':PBloading}">Process</button>
                </p>
            </footer>
            </div>
        </div>
        </center>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        data () {
        return {
            loaded: false,
            logs: null,
            fDate: null,
            PBdisabled: false,
            PBloading: false,
            CBdisabled: false,
            CBloading: false,
            fetched: false
        }
        },
        methods: {
            resetState () {
                this.loaded = false
            },
            consulteData () {
                this.resetState()
                this.CBloading = true
                this.PBdisabled = true
                this.CBdisabled = true
                this.fetched = true
                axios.get(`http://localhost:5000/api/consultelogs`)
                .then(response => {
                    this.logs = response.data.myCount
                    this.fDate = response.data.date
                    this.loaded = true
                    this.CBloading = false
                    this.PBdisabled = false
                    this.CBdisabled = false
                })
                .catch(err => {
                    swal("Problem connecting with the server.","There's some problems, please check it...","error")
                    this.CBloading = false
                    this.PBdisabled = false
                    this.CBdisabled = false
                })
            },
            requestData () {
                this.resetState()
                this.PBloading = true
                this.PBdisabled = true
                this.CBdisabled = true
                this.fetched = false
                axios.get(`http://localhost:5000/api/logs`)
                .then(response => {
                    var ans = JSON.parse(response.data)
                    this.logs = ans[0].myCount
                    this.loaded = true
                    this.PBdisabled = false
                    this.PBloading = false
                    this.CBdisabled = false
                })
                .catch(err => {
                    swal("Problem connecting with the server.","There's some problems, please check it...","error")
                    this.PBdisabled = false
                    this.PBloading = false
                    this.CBdisabled = false
                })
            }
            }
        }
</script>

<style>
</style>