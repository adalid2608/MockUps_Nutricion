<script setup lang="ts">
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { Form } from 'vee-validate';

/*Social icons*/
import google from '@/assets/images/svgs/google-icon.svg';
import facebook from '@/assets/images/svgs/facebook-icon.svg';

const checkbox = ref(false);
const valid = ref(false);
const show1 = ref(false);
const password = ref('admin123');
const username = ref('info@wrappixel.com');
const passwordRules = ref([
    (v: string) => !!v || 'Password is required',
    (v: string) => (v && v.length <= 10) || 'Password must be less than 10 characters'
]);
const emailRules = ref([(v: string) => !!v || 'E-mail is required', (v: string) => /.+@.+\..+/.test(v) || 'E-mail must be valid']);

function validate(values: any, { setErrors }: any) {
    const authStore = useAuthStore();
    return authStore.login(username.value, password.value).catch((error) => setErrors({ apiError: error }));
}
</script>

<template>
    <v-row class="d-flex mb-3">
        <v-col cols="6" sm="6" class="pr-2">
            <v-btn variant="outlined" size="large" class="border text-subtitle-1 red" block>
                <img :src="google" height="16" class="mr-2" alt="google" />
                <span class="d-sm-flex d-none mr-1 text">Sign in with Google</span>
            </v-btn>
        </v-col>
        <v-col cols="6" sm="6" class="pl-2">
            <v-btn variant="outlined" size="large" class="border text-subtitle-1 red " block>
                <img :src="facebook" width="25" height="25" class="mr-1" alt="facebook" />
                <span class="d-sm-flex d-none mr-1 text">Sign in with FB</span>
            </v-btn>
        </v-col>
    </v-row>
    <div class="d-flex align-center text-center mb-6">
        <div class="text-h6 w-100 px-5 font-weight-regular auth-divider position-relative">
            <span class="bg-surface px-5 py-3 position-relative text rounded">or sign in with</span>
        </div>  
    </div>
    <Form @submit="validate" v-slot="{ errors, isSubmitting }" class="mt-5">
        <v-label class="text-subtitle-1 font-weight-medium pb-2 text">Username</v-label>
        <VTextField
            v-model="username"
            :rules="emailRules"
            class="mb-8"
            required
            hide-details="auto"
        ></VTextField>
        <v-label class="text-subtitle-1 font-weight-medium pb-2 text">Password</v-label>
        <VTextField
            v-model="password"
            :rules="passwordRules"
            required
            hide-details="auto"
            type="password"
        ></VTextField>
        <div class="d-flex flex-wrap align-center my-3 ml-n2">
            
            <div class="ml-sm-auto">
                <RouterLink to="" class="url text-decoration-none text-body-1 font-weight-medium text"
                    >Forgot Password ?</RouterLink
                >
            </div>
        </div>
        <v-btn size="large" :loading="isSubmitting":disabled="valid" block type="submit" flat class="fondo text">Sign In</v-btn>
        <div v-if="errors.apiError" class="mt-2">
            <v-alert color="error">{{ errors.apiError }}</v-alert>
        </div>
    </Form>
</template>

<style>
    .text {
        color: white;
    }
    .url {
        color: white;
    }
    .fondo {
        background-color: rgb(226,13,23);
    }
    .rounded {
        border-radius: 50;
    }
    .red{
        background-color: black;
    }
</style>
