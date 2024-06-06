// src/components/ChartWidget.vue
<template>
  <div>
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import { Chart } from 'chart.js'
import { fetchData } from '../services/apiService'

export default defineComponent({
  props: {
    data: {
      type: Object,
      required: true
    }
  },
  setup(props) {
    const chartCanvas = ref<HTMLCanvasElement | null>(null)
    const chartData = ref<any>(null)

    onMounted(async () => {
      chartData.value = await fetchData('https://api.example.com/data')
      if (chartCanvas.value) {
        new Chart(chartCanvas.value, {
          type: 'bar',
          data: chartData.value,
          options: {}
        })
      }
    })

    return { chartCanvas, chartData }
  }
})
</script>
