<script setup>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';

const props = defineProps(['results', 'dosage'])

// ({{res.concentration.toFixed(3)}}%)

</script>
<template>
    <div class="text-center text-2xl">
        Options w/ Dosage of {{dosage.toFixed(1)}}
    </div>
    <DataTable :value="results" stripedRows scrollable scrollHeight="200px" :showHeaders="false">
        <Column field="name" header="Name" class="overflow-hidden text-overflow-ellipsis"><template #body="slotProps">
            {{slotProps.data.names[0]}} ({{slotProps.data.concentration.toFixed(3)}}%)
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