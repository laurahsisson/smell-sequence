<script setup>
import Graph from '@/components/Graph.vue'
import Sequencer from '@/components/Sequencer.vue'
import Listing from '@/components/Listing.vue'
import Crate from '@/components/Crate.vue'

const data = [
    { name: "para-cresyl acetate", SMILES: 'CC(=O)CCC1=CC=C(C=C1)OC', probability: 1, concentration: 0.0032, x: 0.45, y: 0.67 },
    { name: "ambroxan", SMILES: 'CC([C@@H]1CCC@(C)C=C)C(=O)CC=C(C)C', probability: .8, concentration: 0.0008, x: 0.15, y: 0.45 },
    { name: "cinnamyl alcohol", SMILES: 'CCCCCCCC(=O)OC1=CC=C(C=C1)C', probability: .4, concentration: 6.4900e-06, x: 0.88, y: 0.23 }
]
</script>
<template>
    <div class="surface-ground" style="height: 100vh">
        <div class="p-4 mx-auto" style="max-width: 60vw;">
            <div class="grid justify-content-center py-2">
                <div class="col-auto mx-2">
                    <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
                        <Sequencer />
                    </div>
                </div>
                <div class="col-auto mx-2">
                    <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
                        <Graph :results="data" />
                    </div>
                </div>
                <div class="col-auto mx-2">
                    <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
                        <Listing :results="data" />
                    </div>
                </div>
            </div>
            <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
                <Crate />
            </div>
        </div>
    </div>
</template>