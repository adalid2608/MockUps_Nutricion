<script setup lang="ts">
import { productsCard } from '@/_mockApis/components/widget/card';

</script>
<template>
    <v-row>
        <v-col cols="12" lg="3" sm="6" v-for="card in productsCard" :key="card.title">
            <v-card elevation="10"  rounded="md">
                <RouterLink :to="card.link">
                    <v-img :src="card.photo" height="90%" class="rounded-t-md"></v-img>
                </RouterLink>
                <div class="d-flex justify-end mr-3 mt-n3">
                    <v-btn size="30" icon variant="flat" class="bg-primary d-flex">
                        <v-avatar size="30" class="text-white">
                            <BasketIcon size="17" />
                        </v-avatar>
                        <v-tooltip
                            activator="parent"
                            location="bottom"
                        >Más Información
                        </v-tooltip>
                    </v-btn>
                </div>
                <v-card-item class="pt-0">
                    <h6 class="text-h6" v-text="card.title"></h6>
                    <div class="d-flex align-center justify-space-between mt-1">
                        <div>
                            <span class="text-h6"></span>
                            <span class="text-body-1 ml-2 text-medium-emphasis text-decoration-line-through"></span>
                        </div>
                        <v-rating density="compact" color="warning" size="small" v-model="card.rating" readonly></v-rating>
                    </div>
                </v-card-item>
            </v-card>
        </v-col>
    </v-row>
</template>
