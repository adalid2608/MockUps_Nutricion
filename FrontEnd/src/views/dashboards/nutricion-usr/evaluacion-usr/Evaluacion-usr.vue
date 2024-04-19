<script setup lang="ts">
import { ref } from 'vue';
const location = ref(['De 1 a 2 comidas', 'De 2 a 3 comidas', 'De 3 a 5 comidas', 'Más de 5 comidas']);
const slider5 = ref(0);

</script>
<template>
    <v-card elevation="10" >
        <v-card-item>
            <div class="d-sm-flex align-center justify-space-between">
                <v-card-title class="text-h5">Información Nutrimental</v-card-title>
            </div>
        </v-card-item>
        <v-divider></v-divider>
        <!----Account Details---->
        <v-card-text class="pb-0">
            <div class="mt-6">
                <v-row class="align-center mb-3">
                    <v-col cols="12" sm="3" class="pb-sm-3 pb-0">
                        <v-label class=" font-weight-medium">Nombre Completo</v-label>
                    </v-col>
                    <v-col cols="12" sm="9">
                        <v-text-field color="primary" variant="outlined" type="text" placeholder="John Doe Amador Cortez" hide-details />
                    </v-col>
                </v-row>
                <v-row class="align-center mb-3">
                    <v-col cols="12" sm="3" class="pb-sm-3 pb-0">
                        <v-label class=" font-weight-medium">Email</v-label>
                    </v-col>
                    <v-col cols="12" sm="9">
                        <v-text-field
                            color="primary"
                            variant="outlined"
                            type="email"
                            placeholder="john.doe"
                            suffix="@example.com"
                            hide-details
                        />
                    </v-col>
                </v-row>
                <v-row class="align-center mb-3">
                  <v-col cols="12" sm="3" class="pb-sm-3 pb-0">
                      <v-label class=" font-weight-medium">Fecha de Nacimiento</v-label>
                  </v-col>
                  <v-col cols="12" sm="9">
                      <v-text-field color="primary" variant="outlined" type="date" hide-details></v-text-field>
                  </v-col>
                </v-row>
                <v-row class="align-center mb-3">
                  <v-col cols="12" sm="3" class="pb-sm-3 pb-0">
                      <v-label class=" font-weight-medium">Comidas al dia regularmente</v-label>
                  </v-col>
                  <v-col cols="12" sm="9">
                      <v-select
                          v-model="select"
                          :items="location"
                          item-title="state"
                          item-value="abbr"
                          label="Select"
                          return-object
                          single-line
                          variant="outlined"
                          hide-details
                      ></v-select>
                    </v-col>
                  </v-row>
            </div>
        </v-card-text>
        <v-divider></v-divider>
        <!----Personal Info---->
        <v-card-text class="pb-1">
            <div class="mt-6">
                <v-row class="align-center mb-3">
                    <v-col cols="12" sm="4" class="pb-sm-3 pb-0">
                        <v-label class=" font-weight-medium">Ejercicio</v-label>
                    </v-col>
                    <div class="d-flex gap-3 align-center justify-center">
                      <v-checkbox-btn :model-value="false" color='primary'>Si</v-checkbox-btn>
                      <v-checkbox-btn :model-value="false" color='secondary'>No</v-checkbox-btn>
                  </div>
                </v-row>
                <v-row class="align-center mb-3">
                  <v-col cols="12" sm="4" class="pb-sm-3 pb-0">
                      <v-label class=" font-weight-medium">Medicamentos Actualmente</v-label>
                  </v-col>
                  <div class="d-flex gap-3 align-center justify-center">
                    <v-checkbox-btn :model-value="false" color='primary'>Si</v-checkbox-btn>
                    <v-checkbox-btn :model-value="false" color='secondary'>No</v-checkbox-btn>
                </div>
              </v-row>
                <v-row class="align-center mb-3">
                    <v-col cols="12" sm="3" class="pb-sm-3 pb-0">
                        <v-label class=" font-weight-medium">Peso en Kg</v-label>
                    </v-col>
                    <v-slider class="mt-3" v-model="slider5" hide-details color="primary" step="1" thumb-label="always"></v-slider>
                </v-row>
                <v-row class="align-center mb-3">
                  <v-col cols="12" sm="3" class="pb-sm-3 pb-0">
                      <v-label class=" font-weight-medium">Altura en Cm</v-label>
                  </v-col>
                  <v-slider class="mt-3" v-model="slider5" hide-details color="primary" step="1" thumb-label="always"></v-slider>
              </v-row>
                <v-row class="align-center mb-3">
                    <v-col cols="12" sm="3" class="pb-sm-3 pb-0">
                        <v-label class=" font-weight-medium">IMC</v-label>
                    </v-col>
                    <v-col cols="12" sm="9">
                        <v-text-field color="primary" variant="outlined" type="text" placeholder="" hide-details>
                        </v-text-field>
                    </v-col>
                </v-row>
                <v-row class="align-center mb-3">
                    <v-col cols="12" sm="9" offset-sm="3">
                        <v-btn color="success" flat>Enviar</v-btn>
                        <v-btn class="bg-lighterror text-error ml-4" flat>Cancelar</v-btn>
                    </v-col>
                </v-row>
            </div>
        </v-card-text>
    </v-card>
</template>