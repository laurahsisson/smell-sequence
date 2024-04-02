<script setup>
import { ref } from 'vue'
import { CardState } from '@/constants.js'

import Button from 'primevue/button';
import Grid from '@/components/Grid.vue'


const props = defineProps(['boxes', 'notes'])

const choiceCount = 3
const choiceRetries = 15

const state = ref(getNewState());

function getRandom(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

function getNewQuestion() {
    const newCard = getRandom(props.boxes)
    const newNote = getRandom(newCard.notes)

    const newChoices = [newCard.name]
    var i = 0;
    while (newChoices.length < choiceCount && i < choiceRetries) {
        i += 1;
        const potential = getRandom(props.boxes);

        if (newChoices.includes(potential.name)) {
            continue;
        }
        if (potential.notes.includes(newNote)) {
            continue;
        }

        newChoices.push(potential.name)
    }

    return { answer: newCard.name, note: newNote, choices: newChoices }
}

function getNewState() {
    const question = getNewQuestion();

    const newStates = {}

    props.boxes.forEach((box) => {
        if (question.choices.includes(box.name)) {
            newStates[box.name] = { state: CardState.Selected, enabled: true }
        } else {
            newStates[box.name] = { state: CardState.Default, enabled: false }
        }
    });

    return { cardStates: newStates, answer: question.answer, note: question.note, choices: question.choices, selected: "" };
}

function resetState() {
    state.value = getNewState()
}

function selectCard(box) {
    state.value.selected = box.name;

    state.value.choices.forEach((name) => {
        state.value.cardStates[name] = { state: CardState.Default, enabled: false }
    });

    if (box.name == state.value.answer) {
        state.value.cardStates[box.name] = { state: CardState.Highlighted, enabled: false }
    } else {
        state.value.cardStates[box.name] = { state: CardState.Danger, enabled: false }
        state.value.cardStates[state.value.answer] = { state: CardState.Highlighted, enabled: false }
    }
}
</script>
<template>
    <div class="text-900 font-bold text-6xl text-center">
        Test your knowledge.
    </div>
    <div class="grid p-3">
        <div class="col-4">
            <div class="p-3 h-full">
                <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
                    <p class="text-xl">
                        <div v-if="!state.selected">
                            <p>Please select the</p>
                            <p class="font-bold">{{state.note}}</p>
                            <p>fragrance between</p>
                            <p class="font-bold">{{state.choices.join(", ")}}.</p>
                        </div>
                        <div v-else>
                            <p>Your choice was</p>
                            <p class="font-bold">{{(state.selected == state.answer) ? "correct" : "incorrect"}}.</p>
                            <p>The answer was</p>
                            <p class="font-bold">{{state.answer}}</p>
                            <p>is the</p>
                            <p class="font-bold">{{state.note}}</p>
                            <p>fragrance</p>
                            <Button text raised @click="resetState()" label="Next"/>
                        </div>
                    </p>
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