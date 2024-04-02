<script>
import * as d3 from "d3";
// Have to use this annoying structure because d3 is an es module.
export default {
    data() {
        return {
            data: [
                { SMILES: 'CC(=O)CCC1=CC=C(C=C1)OC', probability: 1, concentration: 0.0032, x: 0.35, y: 0.67 },
                { SMILES: 'CC([C@@H]1CCC@(C)C=C)C(=O)CC=C(C)C', probability: .8, concentration: 0.0008, x: 0.12, y: 0.45 },
                { SMILES: 'CCCCCCCC(=O)OC1=CC=C(C=C1)C', probability: .4, concentration: 6.4900e-06, x: 0.88, y: 0.23 }

            ],
            graphSize: 400,
            radiusFactor: 20
        };
    },
    methods: {
        handleClick(res) {
            console.log("Clicked:", res);
        }
    },
    mounted() {
        // You can keep your D3 logic here if needed
    },
};
</script>
<template>
    <div class="grid">
        <svg class="col-auto" :width="graphSize" :height="graphSize">
            <g v-for="res in data">
                <circle :cx="res.x*graphSize" :cy="res.y*graphSize" :r="res.probability*radiusFactor" @click="handleClick(res)">
                </circle>
                <text :x="res.x*graphSize" :y="res.y * graphSize - res.probability * radiusFactor - 10" text-anchor="middle">{{res.SMILES}}</text>
            </g>
        </svg>
        <div class="col-auto">
            <div v-for="res in data">
                {{res.SMILES}} : <div class="text-xl">{{res.probability}}</div>
                <br>
            </div>
        </div>
    </div>
</template>