<script setup>

import Chart from 'primevue/chart';

const props = defineProps(['sequence','tempResult']);

const all_labels = ['Citrus', 'Warm', 'Sweet', 'Green', 'Fruity', 'Floral', 'Fresh', 'Spicy', 'Woody'];

// Radar chart looks bad if the values are at or close to 0. We set the minimum to be this value.
const MIN_VALUE = .3;

const chartOptions = {
    scales: {
        r: {
            ticks: {
                display: false,
                count: 5,
            },
        },
    },
    animation: {
        duration: 0,
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

function makeChartData() {
    const sequence_notes = props.sequence.map(result => 
        ({data: all_labels.map(note => result.radar[note])})
    );
    if (props.tempResult.radar) {
        sequence_notes.push({data: all_labels.map(note => props.tempResult.radar[note])})
    }

    return {
        labels: all_labels,
        datasets: sequence_notes,
    }
}

function setMinimums(chartData) {
    if (!chartData.datasets){
        return chartData;
    }

    const newData = JSON.parse(JSON.stringify(chartData));
    newData.datasets.forEach(dataset => {
        dataset.data = dataset.data.map(value => Math.max(value, MIN_VALUE));
    });
    newData.datasets.splice(0, newData.datasets.length - 1);
    return newData
}

</script>
<template>
    <Chart type="radar" :data="setMinimums(makeChartData())" :options="chartOptions" />
</template>