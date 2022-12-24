<template>
  <form @submit.prevent="fetch">
    <input v-model="path" />
    <button type="submit">teste</button>
  </form>
</template>

<script setup>
import { $axios } from '~/api';
import { ref } from 'vue';

const path = ref("")

const fetch = () => {
  $axios.get(path.value).then((r) => console.log(r))
}
</script>
