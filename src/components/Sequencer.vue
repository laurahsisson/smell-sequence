<script setup>

import Button from 'primevue/button';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';


const props = defineProps(['sequence']);
defineEmits(['delete-last']);

</script>
<template>
    <!-- Reversing because we want to have the last elements in the sequence first. -->
    <Button icon="pi pi-arrow-left" severity="secondary" :disabled="sequence.length == 0" @click="$emit('delete-last')"/>
    <DataTable :value="sequence.toReversed()" stripedRows scrollable scrollHeight="200px" :showHeaders="false">
        <Column field="name" header="Name" class="overflow-hidden text-overflow-ellipsis"><template #body="slotProps">
                {{slotProps.data.names[0]}} ({{slotProps.data.concentration.toFixed(3)}}%)
            </template></Column>
        <Column field="dosage" header="Dosage">
            <template #body="slotProps">
                {{slotProps.data.dosage.toFixed(1)}}
            </template>
        </Column>
    </DataTable>
</template>