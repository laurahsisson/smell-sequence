<script>
// Not using chart.js because this is much easier and cleaner.
import * as d3 from "d3";

// Have to use this annoying structure because d3 is an es module.
export default {
    emits: ['result-appended'], 
    data() {
        return {
            graphSize: 400,
            radiusFactor: 20,
            graphPadding: 50,
        };
    },
    methods: {
        handleClick(res) {
            this.$emit('result-appended', {name:res.names[0],CAS:res.CAS,concentration:res.concentration});
        },
        handleMouseover(i) {
            document.getElementById('tooltip'+i).style.visibility = 'visible';
        },
        handleMouseout(i) {
            document.getElementById('tooltip'+i).style.visibility = 'hidden';
        },
    },
    props: ['results'],
    mounted() {
        // You can keep your D3 logic here if needed
    },
};
</script>
<template>
    <svg :width="graphSize+2*graphPadding" :height="graphSize+2*graphPadding">
        <g v-for="(res,i) in results">
            <circle :cx="res.position.x*graphSize + graphPadding" :cy="res.position.y*graphSize + graphPadding" :r="res.probability*radiusFactor" @click="handleClick(res)" @mouseover="handleMouseover(i)" @mouseout="handleMouseout(i)">
            </circle>
            <text :x="res.position.x*graphSize + graphPadding" :y="res.position.y * graphSize + graphPadding - res.probability * radiusFactor - 10" text-anchor="middle">{{res.names[0]}}</text>
            <text :id="'tooltip'+i" :x="res.position.x*graphSize + graphPadding" :y="res.position.y * graphSize + graphPadding - res.probability * radiusFactor - 30" :visibility="'hidden'" text-anchor="middle">{{res.SMILES}}</text>
        </g>
    </svg>
</template>