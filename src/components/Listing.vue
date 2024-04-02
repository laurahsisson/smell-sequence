<script setup>
const props = defineProps(['results'])
</script>
<template>
    <li v-for="res in results">
        {{res.SMILES}} : {{res.probability}}
        <br>
    </li>
</template>