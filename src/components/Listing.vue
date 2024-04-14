<script setup>
const props = defineProps(['results','dosage'])
</script>
<template>
    <div class="text-center text-2xl">
        Options w/ Dosage of {{dosage.toFixed(1)}}
    </div>
    <ul class="list-none p-0">
        <li v-for="res in results">
            {{res.names[0]}} ({{res.concentration.toFixed(3)}}%) : {{res.probability.toFixed(2)}}
            <br>
        </li>
    </ul>
</template>