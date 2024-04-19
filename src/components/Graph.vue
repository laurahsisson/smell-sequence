<script>
// Not using chart.js because this is much easier and cleaner.
import * as d3 from "d3";

import Checkbox from 'primevue/checkbox';
import InputNumber from 'primevue/inputnumber';
import Dropdown from 'primevue/dropdown';

// Have to use this annoying structure because d3 is an es module.
export default {
    emits: ['result-appended', 'set-temp-value'],
    data() {
        return {
            graphWidth: 3*160,
            graphHeight: 2*160,
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
        noteToColor(note) {
            switch (note) {
                case 'Citrus':
                    return "#F7B538"
                case 'Warm':
                    return "#6B0F1A"
                case 'Sweet':
                    return "#FEF686"
                case 'Green':
                    return "#A0E426"
                case 'Fruity':
                    return "#F588C8"
                case 'Floral':
                    return "#F588C8"
                case 'Fresh':
                    return "#7DF9FF"
                case 'Spicy':
                    return "#8A3324"
                case 'Woody':
                    return "#4F200F"
            }
        },
        hexToRgb(hex) {
            // Convert hex color to RGB
            const bigint = parseInt(hex.slice(1), 16);
            const r = (bigint >> 16) & 255;
            const g = (bigint >> 8) & 255;
            const b = bigint & 255;
            return { r, g, b };
        },
        rgbToHex({ r, g, b }) {
            // Convert RGB to hex color
            return `#${((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1)}`;
        },
        averageHexColors(color1, color2) {
            // Calculate average of two hex colors
            const rgb1 = this.hexToRgb(color1);
            const rgb2 = this.hexToRgb(color2);
            const avgRgb = {
                r: Math.floor((rgb1.r + rgb2.r) / 2),
                g: Math.floor((rgb1.g + rgb2.g) / 2),
                b: Math.floor((rgb1.b + rgb2.b) / 2)
            };
            return this.rgbToHex(avgRgb);
        },
        color(res) {
            // Shout out to GPT for this monstrosity.
            const [firstNote, secondNote] = Object.entries(res.radar).reduce(([maxKey, secondMaxKey, maxValue, secondMaxValue], [k, v]) =>
                v > maxValue ? [k, maxKey, v, maxValue] : v > secondMaxValue ? [maxKey, k, maxValue, v] : [maxKey, secondMaxKey, maxValue, secondMaxValue], [null, null, -Infinity, -Infinity]).slice(0, 2);

            return this.averageHexColors(this.noteToColor(firstNote), this.noteToColor(secondNote));

            // return this.noteToColor(firstNote);
            // console.log(keyWithHighestValue);
            // return '#FF0000'
        }
    },
    components: {
        Checkbox, // Register Checkbox as a component
        InputNumber,
        Dropdown,
    },
    props: ['units', 'results', 'options'],
    mounted() {
        // You can keep your D3 logic here if needed
    },
};
</script>
<!-- TODO, some way to handle zooming? -->
<template>
    <div >
        <svg class="block mx-auto" :width="graphWidth+2*graphPadding" :height="graphHeight+2*graphPadding" style="outline: thin solid black;">
            <!-- Reversing it so that more probable molecules are rendered on top. -->
            <g v-for="res in results.toReversed()">
                <circle stroke="black" :cx="res.position.x * graphWidth + graphPadding" :cy="res.position.y * graphHeight + graphPadding" :r="res.probability*radiusFactor" @click="handleClick(res)" @mouseover="handleMouseover(res)" @mouseout="handleMouseout(res)" :style="{fill: color(res),cursor: 'pointer'}">
                </circle>
                <text :x="res.position.x*graphWidth + graphPadding" :y="res.position.y * graphHeight + graphPadding" text-anchor="middle" @click="handleClick(res)" @mouseover="handleMouseover(res)" @mouseout="handleMouseout(res)" style="font-weight: 500; cursor: pointer;" >{{res.names[0]}}</text>
            </g>
        </svg>
    </div>
    <div class="grid justify-content-center py-2">
        <div class="col-auto mx-2 my-auto ">
            <InputNumber v-model="options.k" :min="3" :max="30" showButtons buttonLayout="horizontal">
                <template #incrementbuttonicon>
                    <span class="pi pi-plus" />
                </template>
                <template #decrementbuttonicon>
                    <span class="pi pi-minus" />
                </template>
            </InputNumber>
        </div>
        <Dropdown v-model="options.unit" :options="units" optionLabel="name" placeholder="Select a Unit" />
        <div class="col-auto mx-2 my-auto ">
            <Checkbox v-model="options.global_tsne" inputId="tsne" :binary="true" />
            <label for="tsne" class="ml-2"> Global TSNE? </label>
        </div>
    </div>
</template>