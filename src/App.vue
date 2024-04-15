<script setup>
import { ref, watch } from 'vue'

import Radar from '@/components/Radar.vue'
import Graph from '@/components/Graph.vue'
import Sequencer from '@/components/Sequencer.vue'
import Listing from '@/components/Listing.vue'
import Crate from '@/components/Crate.vue'


const data = ref([]);

const sequence = ref([])

const options = ref({k:15,global_tsne:false})

const dosage = ref(0);

const tempResult = ref({});

const cratesSelected = ref({});
const cratesList = ref([]);
const cratesData = ref({});

function appendResult(res) {
    res["dosage"] = dosage.value;
    sequence.value.push(res);
}

function deleteLast() {
    sequence.value.pop();
}

function setTempValue(res) {
    tempResult.value = res;
}

function getResults() {
    const sequence_str = JSON.stringify(sequence.value);

    const crates = Object.keys(cratesSelected.value).filter(key => cratesSelected.value[key]);
    const crates_str = JSON.stringify(crates);
    const options_str = JSON.stringify(options.value);

    fetch("http://127.0.0.1:5000/recommendation/?sequence=" + encodeURIComponent(sequence_str) + "&crates=" + encodeURIComponent(crates_str) + "&options=" + encodeURIComponent(options_str))
        .then(response => response.json())
        .then(response_data => {
            // Process the JSON response data
            data.value = response_data.options;
            dosage.value = response_data.dosage;
        })
        .catch(error => {
            // Handle any errors that occur during the fetch
            console.error('Error:', error);
        });
}

function listCrates() {
    fetch("http://127.0.0.1:5000/crates")
        .then(response => response.json())
        .then(response_data => {
            cratesList.value = response_data;
            response_data.forEach((crate) => cratesSelected.value[crate.name] = true);
            getCrate(response_data[0].name)
        })
        .catch(error => {
            // Handle any errors that occur during the fetch
            console.error('Error:', error);
        });
}

function getCrate(name) {
    fetch("http://127.0.0.1:5000/crates/" + name)
        .then(response => response.json())
        .then(response_data => {
            cratesData.value = response_data;
        })
        .catch(error => {
            // Handle any errors that occur during the fetch
            console.error('Error:', error);
        });
}

listCrates();

watch(cratesSelected, async () => {
    getResults();
}, { deep: true });

watch(sequence, async () => {
    getResults();
}, { deep: true });

watch(options, async () => {
    getResults();
}, { deep: true });

</script>
<template>
    <div class="surface-ground" style="height: 100%">
        <div class="p-4 mx-auto">
            <div class="shadow-2 p-3 my-2 surface-card mx-auto" style="border-radius: 6px; max-width: 60em;">
                <Graph :results="data" :options="options" @result-appended="appendResult" @set-temp-value="setTempValue" />
            </div>
            <div class="grid justify-content-center py-2">
                <div class="col-auto mx-2">
                    <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
                        <Radar :sequence="sequence" :tempResult="tempResult"/>
                    </div>
                </div>
                <div class="col-auto mx-2">
                    <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
                        <Sequencer :sequence="sequence" @delete-last="deleteLast"/>
                    </div>
                </div>
                <div class="col-auto mx-2">
                    <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
                        <Listing :results="data" :dosage="dosage" />
                    </div>
                </div>
            </div>
            <div class="shadow-2 p-3 my-2 surface-card mx-auto" style="border-radius: 6px; max-width: 100em;">
                <Crate :cratesList="cratesList" :cratesSelected="cratesSelected" :cratesData="cratesData" :getCrate="getCrate" />
            </div>
        </div>
    </div>
</template>