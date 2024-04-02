<script setup>
    import Button from 'primevue/button';
import Chart from 'primevue/chart';

const molecules = [
    {name:"costus valerolactone",  concentration: 0.02},
    {name:"phenyl propyl acetate",  concentration: 0.15},
    {name:"decanol", concentration: 0.003}]

// Radar chart looks bad if the values are at or close to 0. We set the minimum to be this value.
const MIN_VALUE = .3;
const chartData = {
    labels: ['Citrus', 'Warm', 'Sweet', 'Green', 'Fruity', 'Floral', 'Fresh', 'Spicy', 'Woody'],
    datasets: [
        {
            label: 'My Second dataset',
            data: [0, 1, .25, .6, 0, 0, 0, .6, 1]
        }
    ]
}

const chartOptions = {
    scales: {
        r: {
            ticks: {
                display: false,
                count: 5,
            },
        },
    },
    elements: {
        line: {
            // This should be very small. Past like .5 it breaks
            tension: 0.1,

        },
        point: {
            pointStyle: false,
        }
    },
    plugins: {
        legend: {
            display: false
        },
    }
}
function setMinimums(chartData) {
    // console.log(chartData)
    const newData = JSON.parse(JSON.stringify(chartData));
    newData.datasets.forEach(dataset => {
        dataset.data = dataset.data.map(value => Math.max(value, MIN_VALUE));
    });
    // console.log(newData)
    return newData
}
</script>
<template>
    <Chart type="radar" :data="setMinimums(chartData)" :options="chartOptions" />
    <ul class="list-none p-0">
        <li v-for="box in molecules">
            {{box.name}} ({{box.concentration}}%)
        </li>
    </ul>
</template>