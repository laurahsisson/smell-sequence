<script>
import * as d3 from "d3";
// Have to use this annoying structure because d3 is an es module.
export default {
    data() {
        return {
            graphSize: 400,
            radiusFactor: 20
        };
    },
    methods: {
        handleClick(res) {
            console.log("Clicked:", res);
        }
    },
    props: ['results'],
    mounted() {
        // You can keep your D3 logic here if needed
    },
};
</script>
<template>
    <svg :width="graphSize" :height="graphSize">
        <g v-for="res in results">
            <circle :cx="res.x*graphSize" :cy="res.y*graphSize" :r="res.probability*radiusFactor" @click="handleClick(res)">
            </circle>
            <text :x="res.x*graphSize" :y="res.y * graphSize - res.probability * radiusFactor - 10" text-anchor="middle">{{res.SMILES}}</text>
        </g>
    </svg>
</template>