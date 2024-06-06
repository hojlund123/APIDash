<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <h1>Customizable Dashboard</h1>
        <v-btn @click="addWidget">Add Widget</v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col v-for="widget in widgets" :key="widget.id">
        <component :is="widget.component" :data="widget.data"></component>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

export default defineComponent({
  setup() {
    const widgets = ref<{ id: number; component: string; data: any }[]>([])

    const addWidget = () => {
      widgets.value.push({
        id: widgets.value.length,
        component: 'ChartWidget', // This should match the component name for your widgets
        data: {} // Placeholder for actual data
      })
    }

    return { widgets, addWidget }
  }
})
</script>
