<script setup>
import { ref } from 'vue';

import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';
import Checkbox from 'primevue/checkbox';

const props = defineProps(['cratesList', 'cratesSelected', 'cratesData', 'getCrate'])
</script>
<template>
    <TabView @update:activeIndex="(activeIndex)=>getCrate(cratesList[activeIndex].name)">
        <TabPanel v-for="crate in cratesList">
            <template #header>
                <Checkbox v-model="cratesSelected[crate.name]" :binary="true" />
                {{crate.name}} ({{crate.size}})
            </template>
            <p class="m-0">
                {{crate.description}}
            </p>
            <!-- getCrate() -->
            <DataTable :value="cratesData.data" showGridlines stripedRows scrollable scrollHeight="400px">
                <Column field="name" header="Name" class="overflow-hidden text-overflow-ellipsis"><template #body="slotProps">
                        {{slotProps.data.name}} ({{slotProps.data.concentration.toFixed(3)}}%)
                    </template>
                </Column>
                <Column field="CAS" header="CAS"></Column>
                <Column field="notes" header="Notes">
                    <template #body="slotProps">
                        {{slotProps.data.notes.join(", ")}}
                    </template>
                </Column>
            </DataTable>
        </TabPanel>
    </TabView>
</template>