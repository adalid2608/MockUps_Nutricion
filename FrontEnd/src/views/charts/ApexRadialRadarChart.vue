<script setup lang="ts">
import { computed } from 'vue';
import { useTheme } from 'vuetify';
import UiChildCard from '@/components/shared/UiChildCard.vue';

const theme = useTheme();
const success = theme.current.value.colors.success;
const accent = theme.current.value.colors.accent;
const warning = theme.current.value.colors.warning;

const radialBarchartOptions = computed(() => {
    return {
        chart: {
            type: 'radialBar',
            height: 800,
            fontFamily: `inherit`,
            foreColor: '#adb0bb',
            toolbar: {
                show: true
            }
        },
        colors: ['#6ac3fd', '#0b70fb', '#f64e60', '#ffa800', '#008f39'],
        plotOptions: {
            radialBar: {
                dataLabels: {
                    name: {
                        fontSize: '12px'
                    },
                    value: {
                        fontSize: '16px'
                    },
                    total: {
                        show: true,
                        label: 'Balance Nutricional',
                        formatter() {
                            return '100% de la dieta';
                        }
                    }
                }
            }
        },
    };
});

const radialBarChart = {
    series: [13, 15, 27, 22, 23]
};

const radarOptions = computed(() => {
    return {
        chart: {
            type: 'radar',
            height: 800,
            fontFamily: `inherit`,
             toolbar: {
                    show: true,
                },
        },
        colors: ['#0b70fb'],
        labels: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    };
});

const radarChart = {
    series: [
        {
            name: ['Peso en Kg'],
            data: [100, 84, 70, 67, 70, 66],
        }
    ]
};
</script>

<template>
    <v-row>
        <v-col cols="12">
            <v-row>
                <v-col cols="12" lg="12">
                    <!-- ---------------------------------------------------- -->
                    <!-- Radialbar Chart -->
                    <!-- ---------------------------------------------------- -->
                    <UiChildCard title="Balance Nutrimental" class="bg-surface">
                        <apexchart type="radialBar" height="300" :options="radialBarchartOptions" :series="radialBarChart.series">
                        </apexchart>
                        <div class="d-flex align-center px-2">
                            <span style="color: #6ac3fd">
                              <span class="text-overline">
                                <i class="mdi mdi-brightness-1 mx-1"></i>
                              </span>
                              <span class="text-subtitle-1">Ingesta de alimentos</span>
                            </span>
                          </div>
                          <div class="d-flex align-center px-2">
                            <span style="color: #0b70fb">
                              <span class="text-overline">
                                <i class="mdi mdi-brightness-1 mx-1"></i>
                              </span>
                              <span class="text-subtitle-1">Diversidad de alimentos</span>
                            </span>
                          </div>
                          <div class="d-flex align-center px-2">
                            <span style="color: #f64e60">
                              <span class="text-overline">
                                <i class="mdi mdi-brightness-1 mx-1"></i>
                              </span>
                              <span class="text-subtitle-1">Control de Porciones</span>
                            </span>
                          </div>
                          <div class="d-flex align-center px-2">
                            <span style="color: #ffa800">
                              <span class="text-overline">
                                <i class="mdi mdi-brightness-1 mx-1"></i>
                              </span>
                              <span class="text-subtitle-1">Consumo de Agua</span>
                            </span>
                          </div>
                          <div class="d-flex align-center px-2">
                            <span style="color: #008f39">
                              <span class="text-overline">
                                <i class="mdi mdi-brightness-1 mx-1"></i>
                              </span>
                              <span class="text-subtitle-1">Balance de Carbohidratos</span>
                            </span>
                          </div>
                    </UiChildCard>
                </v-col>
                <v-col cols="12" lg="12">
                    <!-- ---------------------------------------------------- -->
                    <!-- Radar Chart -->
                    <!-- ---------------------------------------------------- -->
                    <UiChildCard title="Perdida o ganancia de peso" class="bg-surface">
                        <apexchart type="radar" height="300" :options="radarOptions" :series="radarChart.series"> </apexchart>
                    </UiChildCard>
                </v-col>
            </v-row>
        </v-col>
    </v-row>
</template>
