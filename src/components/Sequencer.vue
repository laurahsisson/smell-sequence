<script setup>

import Button from 'primevue/button';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';


const props = defineProps(['options','sequence']);
defineEmits(['delete-last','delete-all']);

</script>
<template>
    <!-- Reversing because we want to have the last elements in the sequence first. -->
    <Button icon="pi pi-arrow-left" severity="secondary" :disabled="sequence.length == 0" @click="$emit('delete-last')"/>
    <Button icon="pi pi-refresh" severity="secondary" :disabled="sequence.length == 0" @click="$emit('delete-all')"/>
    <DataTable :value="sequence.toReversed()" stripedRows scrollable scrollHeight="200px" :showHeaders="false">
        <Column field="name" header="Name" class="overflow-hidden text-overflow-ellipsis"><template #body="slotProps">
                {{slotProps.data.names[0]}} ({{slotProps.data.concentration.toLocaleString(undefined,{style: 'percent', minimumFractionDigits:2})}})
            </template></Column>
        <Column field="dosage" header="Dosage">
            <template #body="slotProps">
                {{slotProps.data.dosage.toFixed(1)}} {{options.unit.symbol}}
            </template>
        </Column>
    </DataTable>
</template>