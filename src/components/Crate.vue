<script setup>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';

const products = [{
        cas: '20-30-15',
        name: 'Ethylbenzene',
        concentration: 0.65,
        notes: ["Fruity", "Floral", "Warm", "Green"]
    },
    {
        cas: '1-34-11',
        name: 'Diethyl ether',
        concentration: 0.72,
        notes: ["Citrus", "Floral", "Warm", "Green"]
    },
    {
        cas: '98-2-80',
        name: 'Butyl acetate',
        concentration: 0.79,
        notes: ["Citrus", "Woody", "Green"]
    },
    {
        cas: '34-60-23',
        name: 'Vanillin butyrate',
        concentration: 0.29,
        notes: ["Citrus", "Fruity", "Floral"]
    },
    {
        cas: '1-48-98',
        name: 'Ethanolamine',
        concentration: 0.15,
        notes: ["Citrus", "Woody", "Green"]
    },
    {
        cas: '34-248',
        name: 'Methyl jasmonate',
        concentration: 0.120,
        notes: ["Citrus", "Warm", "Green"]
    },
    {
        cas: '23-87',
        name: 'Chakra Bracelet',
        concentration: 0.32,
        notes: ["Warm", "Green"]
    },
    {
        cas: '3-23-78',
        name: 'Eugenyl acetate',
        concentration: 0.34,
        notes: ["Citrus", "Green"]
    },
    {
        cas: '34-68',
        name: 'Allyl benzoate',
        concentration: 0.99,
        notes: ["Citrus", "Woody", "Fruity"]
    },
]
</script>
<template>
    <DataTable :value="products" showGridlines stripedRows scrollable scrollHeight="400px">
        <Column field="name" header="Name"></Column>
        <Column field="cas" header="CAS"></Column>
        <Column field="concentration" header="Concentration">
            <template #body="slotProps">
                {{slotProps.data.concentration}}%
            </template>
        </Column>
        <Column field="notes" header="Notes">
            <template #body="slotProps">
                {{slotProps.data.notes.join(", ")}}
            </template>
        </Column>
    </DataTable>
</template>