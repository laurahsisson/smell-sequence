<script setup>
import { ref } from 'vue'
import { CardState } from '@/constants.js'

import Button from 'primevue/button';
import Grid from '@/components/Grid.vue'

const props = defineProps(['boxes', 'notes'])

const state = ref(getNewState());

const maxNotes = 3

function getNewState() {
    const newStates = {}

    props.boxes.forEach((box) => {
        newStates[box.name] = { state: CardState.Default, enabled: true };
    });

    return { cardStates: newStates, selectedNotes: [], card: "" };
}

function resetState() {
    state.value = getNewState()
}

function selectCard(box) {
    if (state.value.name == box.name) {
        resetState();
        return;
    }

    resetState();
    state.value.selectedNotes = box.notes;
    state.value.card = box.name;
    state.value.cardStates[box.name] = { state: CardState.Highlighted, enabled: true }
}

function hasMatch(box,notes) {
    for (var i = 0; i < notes.length; i++) {
        const note = notes[i];
        if (!box.notes.includes(note)) {
            return false;
        }
    }
    return true;
}

function calculateState(box) {
    if (!hasMatch(box,state.value.selectedNotes)) {
        return CardState.Default;
    }
    
    return CardState.Selected;
}

function selectNote(note) {
    if (state.value.card) {
        resetState();
    }

    if (state.value.selectedNotes.includes(note)) {
        const index = state.value.selectedNotes.indexOf(note);
        state.value.selectedNotes.splice(index, 1);
    } else {
        state.value.selectedNotes.push(note);
    }

    const newStates = {}
    props.boxes.forEach((box) => {
        newStates[box.name] = { state: calculateState(box), enabled: true };
    });
    state.value.cardStates = newStates;
}

function severity(note) {
    if (!state.value.selectedNotes.includes(note)) {
        return "secondary";
    }
    if (state.value.card) {
        return "info";
    } else {
        return "success";
    }
}

function canAdd(note) {
    const mergedNotes = state.value.selectedNotes.concat([note]);
    for (var i = 0; i < props.boxes.length; i++) {
        const box = props.boxes[i];
        if (hasMatch(box,mergedNotes)) {
            return true;
        }
    }
    return false;
}

function disabled(note) {
    if (state.value.card) {
        return false;
    }
    return !canAdd(note);
}

// This is truly so hacky but I don't want to add a preprocessor for a single section.
function title() {
    return "text-900 font-bold text-6xl"
}
</script>
<template>
    <div class="text-center">
        <div :class="title()" v-if="!state.selectedNotes.length">Select a note or box to learn.</div>
        <div v-else>
            <div  :class="title()" v-if="state.card">Learn about {{state.card}}
            </div>
            <div  :class="title()" v-else>Learn about {{state.selectedNotes.join(", ")}} notes.</div>
        </div>
        <Button class="my-0" @click="resetState()" :disabled="!state.selectedNotes.length" label="Clear"/>
    </div>
    <div class="grid p-3">
        <div class="col-4">
            <div class="p-3 h-full">
                <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
                    <div class="flex flex-column">
                        <Button class="flex text-2xl my-1 text-center" v-for="note in notes" outlined :raised="state.selectedNotes.includes(note)" :disabled="disabled(note)" :severity="severity(note)" @click="selectNote(note)" :class="{'font-semibold': state.selectedNotes.includes(note)}" :label="note"/>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-8">
            <div class="p-3 h-full">
                <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
                    <Grid @select-card="selectCard" :boxes="boxes" :states="state.cardStates" />
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
</style>