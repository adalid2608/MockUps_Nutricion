<script setup lang="ts">
import { ref } from "vue";

import TheSalesOverview from "../../../../components/dashboards/analytical/TheSalesOverview.vue";
import ProductPerformance from "../../../../components/dashboards/ecommerce/ProductPerformance.vue";
import ApexRadialRadarChart from '../../../../views/charts/ApexRadialRadarChart.vue'

</script>
<template>
    <h1>Graficas</h1>
    <v-row>
        <v-col cols="12" lg="12">
            <TheSalesOverview/>
        </v-col>
        <v-col cols="12" lg="12" class="d-flex align-items-stretch">
            <ProductPerformance />
        </v-col>
        <v-col cols="12" lg="12" class="d-flex align-items-stretch">
            <ApexRadialRadarChart />
        </v-col>
    </v-row>
    <br>
    <v-card elevation="0" rounded="md" class="bg-surface border-0">
        <v-card-item class="py-0">
            <v-row>
                <v-col cols="12" sm="7" class="pa-6">
                    <h5 class="text-h5 pt-3">Welcome back Mathew!</h5>
                    <h6 class="text-subtitle-1 text-13 py-4 textSecondary">
                        You have earned 54% more than last month which is great thing.
                    </h6>
                    <v-btn flat color="success">Check</v-btn>
                </v-col>
                <v-col cols="12" sm="5">
                    <div class="mb-n2">
                        <img src="@/assets/images/backgrounds/welcome-bg2.png" class="mb-n16 mt-4" alt="image" width="300" />
                    </div>
                </v-col>
            </v-row>
        </v-card-item>
    </v-card>
</template>