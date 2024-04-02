<script setup>
import { ref } from 'vue'

import Menubar from 'primevue/menubar';

const emit = defineEmits(['select-mode'])
const props = defineProps(['modes'])

function setMode(event) {
    const { label } = event.item;
    emit('select-mode', label)
}

const items = ref([{
        label: props.modes.Test,
        command: setMode,
        icon: 'pi pi-fw pi-chart-bar'
    },
    {
        label: props.modes.Train,
        command: setMode,
        icon: 'pi pi-fw pi-book'
    },
    {
        label: props.modes.Edit,
        command: setMode,
        icon: 'pi pi-fw pi-file-edit'
    }
]);
</script>
<template>
    <Menubar :model="items" :pt="{
        content: ({
            class: 'px-1'
        }),
        label: ({
            class: 'text-3xl'
        }),
        icon: ({
            class: 'text-xl'
        })

    }"/>
</template>
<style scoped>
</style>