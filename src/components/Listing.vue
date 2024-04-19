<script setup>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';

const props = defineProps(['options','results', 'dosage'])
defineEmits(['result-appended']);

// ({{res.concentration.toFixed(3)}}%)

</script>
<template>
    <div class="text-center text-2xl">
        Options w/ Dosage of {{dosage.toFixed(1)}}  {{options.unit.symbol}}
    </div>
    <DataTable :value="results" stripedRows scrollable scrollHeight="200px" :showHeaders="false">
        <Column field="name" header="Name" class="overflow-hidden text-overflow-ellipsis"><template #body="slotProps">
            <Button icon="pi pi-plus" severity="success" text rounded @click="this.$emit('result-appended', slotProps.data);"/>
            {{slotProps.data.names[0]}} ({{slotProps.data.concentration.toLocaleString(undefined,{style: 'percent', minimumFractionDigits:2})}})
            </template>
        </Column>
        <Column field="probability" header="probability">
            <template #body="slotProps">
                {{slotProps.data.probability.toFixed(2)}}
            </template>
        </Column>
        <Column field="notes" header="Notes">
            <template #body="slotProps">
                {{slotProps.data.notes.join(", ")}}
            </template>
        </Column>
    </DataTable>
</template>