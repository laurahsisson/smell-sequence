<script setup>
const props = defineProps(['results'])
</script>
<template>
    <div class="text-center text-2xl">
        Options
    </div>
    <ul class="list-none p-0">
        <li v-for="res in results">
            {{res.name}} ({{res.concentration}}%) : {{res.probability}}
            <br>
        </li>
    </ul>
</template>