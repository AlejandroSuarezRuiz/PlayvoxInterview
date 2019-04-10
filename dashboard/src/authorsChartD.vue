<script>
  import { Bar } from 'vue-chartjs'
  export default {
    extends: Bar,
    props: {
      chartData: {
        type: Array | Object,
        required: false
      },
      chartLabels: {
        type: Array,
        required: true
      }
    },
    data () {
      return {
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              },
              gridLines: {
                display: true
              }
            }],
            xAxes: [ {
              gridLines: {
                display: false
              }
            }]
          },
          legend: {
            display: false
          },
          responsive: true,
          maintainAspectRatio: false
        }
      }
    },
    mounted () {
      this.renderChart({
        labels: this.chartLabels,
        datasets: [
          {
            label: 'Sold copies',
            borderColor: '#2E1609',
            borderWidth: 2,
            backgroundColor: ['rgba(66,165,219,0.6)','rgba(76,219,66,0.6)','rgba(178,219,66,0.6)','rgba(219,142,66,0.6)','rgba(219,66,69,0.6)'],
            data: this.chartData
          }
        ]
      }, this.options)
    }
  }
</script>