<script>
// Not using chart.js because this is much easier and cleaner.
import * as d3 from "d3";

// Have to use this annoying structure because d3 is an es module.
export default {
    emits: ['result-appended','set-temp-value'], 
    data() {
        return {
            graphSize: 400,
            radiusFactor: 20,
            graphPadding: 50,
        };
    },
    methods: {
        handleClick(res) {
            this.$emit('result-appended', res);
        },
        handleMouseover(res) {
            this.$emit('set-temp-value', res);
        },
        handleMouseout(res) {
            this.$emit('set-temp-value', {});
        },
    },
    props: ['results'],
    mounted() {
        // You can keep your D3 logic here if needed
    },
};
</script>
<!-- TODO, some way to handle zooming? -->
<template>
    <svg :width="graphSize+2*graphPadding" :height="graphSize+2*graphPadding">
        <g v-for="res in results">
            <circle stroke="black" :cx="res.position.x*graphSize + graphPadding" :cy="res.position.y*graphSize + graphPadding" :r="res.probability*radiusFactor" @click="handleClick(res)" @mouseover="handleMouseover(res)" @mouseout="handleMouseout(res)" style="fill: #808080; cursor: pointer;">
            </circle>
            <text :x="res.position.x*graphSize + graphPadding" :y="res.position.y * graphSize + graphPadding - res.probability * radiusFactor - 10" text-anchor="middle">{{res.names[0]}}</text>
        </g>
    </svg>
</template>