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
</template>
  