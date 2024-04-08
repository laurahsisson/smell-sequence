<script setup>
const props = defineProps(['results'])
</script>
<template>
    <div class="text-center text-2xl">
        Options
    </div>
    <ul class="list-none p-0">
        <li v-for="res in results">
            {{res.names[0]}} ({{res.concentration.toFixed(2)}}%) : {{res.probability.toFixed(2)}}
            <br>
        </li>
    </ul>
</template>