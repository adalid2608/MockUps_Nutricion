<script setup lang="ts">
import { ref } from "vue";

import TheSalesOverview from "../../../../components/dashboards/analytical/TheSalesOverview.vue";
import ProductPerformance from "../../../../components/dashboards/ecommerce/ProductPerformance.vue";
import ApexRadialRadarChart from '../../../../views/charts/ApexRadialRadarChart.vue'

</script>
<template>
    <h1>Graficas</h1>
    <v-row>
        <v-col cols="12" lg="6">
            <TheSalesOverview/>
        </v-col>
        <v-col cols="12" lg="6" class="d-flex align-items-stretch">
            <ProductPerformance />
        </v-col>
        <v-col cols="12" lg="12" class="d-flex align-items-stretch">
            <ApexRadialRadarChart />
        </v-col>
    </v-row>
</template>