<script setup>
import Graph from '@/components/Graph.vue'
import Crate from '@/components/Crate.vue'
</script>
<template>
    <div class="surface-ground" style="height: 100vh">
        <div class="grid m-4">
            <div class="col6 mx-2">
                <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
                    <Crate />
                </div>
            </div>
            <div class="col8 mx-2">
                <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
                    <Graph />
                </div>
            </div>
        </div>
    </div>
</template>