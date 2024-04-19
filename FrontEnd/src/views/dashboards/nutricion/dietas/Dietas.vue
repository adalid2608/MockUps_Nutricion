<script setup>
import { ref } from 'vue';
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';
import { BasicDatatables } from '@/_mockApis/components/datatable/dataTable';

const page = ref({ title: 'Seguimiento de Dietas' });
const breadcrumbs = ref([
    {
        text: 'Dietas',
        disabled: false,
        href: '#'
    },
    {
        text: 'Seguimiento',
        disabled: true,
        href: '#'
    }
]);




</script>
<template>
    <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
    <v-row>
        <v-col cols="12">
            <UiParentCard title="Dietas Asignadas">
                <v-data-table items-per-page="5"  :items="BasicDatatables" item-value="Usuario"
                    class="border rounded-md">
                    <template v-slot:column.name="{ column }">
                        {{ column.title.toUpperCase() }}
                    </template>
                </v-data-table>
            </UiParentCard>
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
  