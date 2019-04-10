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
      },
      backColor: {
        type: Array,
        required: false
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
            label: 'Average salary',
            borderColor: '#2E1609',
            borderWidth: 2,
            backgroundColor: this.backColor,
            data: this.chartData
          }
        ]
      }, this.options)
    }
  }
</script>