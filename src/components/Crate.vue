<script setup>
import Button from 'primevue/button';

const molecules = ["A", "B", "C", "D"]
</script>
<template>
    <div class="grid p-3">
        <div class="col-12" v-for="(box,i) in molecules">
            {{box}}
        </div>
    </div>
</template>