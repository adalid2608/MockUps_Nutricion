<script setup lang="ts">
import { ref } from "vue";
const tab = ref(null);
</script>
<template>
    <v-tabs v-model="tab" bg-color="primary">
        <v-tab value="one">Item One</v-tab>
        <v-tab value="two">Item Two</v-tab>
        <v-tab value="three">Item Three</v-tab>
    </v-tabs>
    <v-divider></v-divider>
    <v-card-text class="bg-grey100 mt-4 rounded-md">
        <v-window v-model="tab">
            <v-window-item value="one">
               Item One
            </v-window-item>
            <v-window-item value="two">
                Item Two
            </v-window-item>
            <v-window-item value="three">
                 Item Three
            </v-window-item>
        </v-window>
    </v-card-text>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
