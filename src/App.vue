<script setup>
import { ref } from 'vue';

import Graph from '@/components/Graph.vue'
import Sequencer from '@/components/Sequencer.vue'
import Listing from '@/components/Listing.vue'
import Crate from '@/components/Crate.vue'

// const data = ref([
//     { name: "para-cresyl acetate", SMILES: 'CC(=O)CCC1=CC=C(C=C1)OC', probability: 1, concentration: 0.0032, x: 0.45, y: 0.67 },
//     { name: "ambroxan", SMILES: 'CC([C@@H]1CCC@(C)C=C)C(=O)CC=C(C)C', probability: .8, concentration: 0.0008, x: 0.15, y: 0.45 },
//     { name: "cinnamyl alcohol", SMILES: 'CCCCCCCC(=O)OC1=CC=C(C=C1)C', probability: .4, concentration: 6.4900e-06, x: 0.88, y: 0.23 }
// ])

const data = ref([])

const sequence = ref([
])

function appendResult(res) {
    console.log("BECAUSE WE ARE UNSHIFTING (adding to the front), our sequence model is innacurate.")
    sequence.value.unshift(res);
    getResults(3);
}

function tempAppend(res) {
    sequence.value.unshift(res);
}

function deleteLast() {
    sequence.value.pop();
}


function getResults(k) {
    const sequence_str = JSON.stringify(sequence.value);
    fetch("http://127.0.0.1:5000/recommendation/?sequence=" + encodeURIComponent(sequence_str) + "&k=" + k)
        .then(response => response.json())
        .then(response_data => {
            // Process the JSON response data
            data.value = response_data;
        })
        .catch(error => {
            // Handle any errors that occur during the fetch
            console.error('Error:', error);
        });
}

getResults(3);

</script>
<template>
    <div class="surface-ground" style="height: 100%">
        <div class="p-4 mx-auto">
            <div class="grid justify-content-center py-2">
                <div class="col-auto mx-2">
                    <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
                        <Sequencer :sequence="sequence" />
                    </div>
                </div>
                <div class="col-auto mx-2">
                    <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
                        <Graph :results="data" @result-appended="appendResult" @temp-appended="tempAppend" @delete-last="deleteLast" />
                    </div>
                </div>
                <div class="col-auto mx-2">
                    <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
                        <Listing :results="data" />
                    </div>
                </div>
            </div>
            <div class="shadow-2 p-3 surface-card mx-auto" style="border-radius: 6px; max-width: 100em;">
                <Crate />
            </div>
        </div>
    </div>
</template>