<script setup>
    import { ref } from 'vue'

import Button from 'primevue/button';
import Card from 'primevue/card';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Menu from 'primevue/menu';
import Divider from 'primevue/divider';
import Chips from 'primevue/chips';
import ColumnGroup from 'primevue/columngroup'; // optional
import Row from 'primevue/row'; // optional
import Panel from 'primevue/panel';
import InputText from 'primevue/inputtext';

import { deepClone, deepEquals } from "@/constants.js"

const props = defineProps(['boxes']);
defineEmits(['update']);

const data = ref(deepClone(props.boxes));
// For adding a new box
const newName = ref("");

const header = "<b>Hello</b>";

// For editing an existing box
const editing = ref(-1);
const changeName = ref("");

function revert() {
    data.value = deepClone(props.boxes);
}

function remove(box) {
    const index = data.value.indexOf(box);
    data.value.splice(index, 1);
}

// This is a very inefficient method of equality checking but probs fine for now. The issue is that it is called multiple times per DOM update.
function hasUnsaved() {
    return !deepEquals(data.value, props.boxes);
}

function switchBy(idx, incr) {
    const temp = data.value[idx + incr];
    data.value[idx + incr] = data.value[idx];
    data.value[idx] = temp;
}

function add() {
    data.value.unshift({name:newName.value,notes:[]});
    newName.value = "";
}

function confirm(idx) {
    editing.value = -1;
    data.value[idx].name = changeName.value;
    changeName.value = "";
}

// THINKING WITH CLOSURES.
function makeMenu(idx) {
    return [{
        label: 'Rename',
        icon: 'pi pi-pencil',
        command: (ev) => {
            editing.value = idx;
        }
    },
    {
        label: 'Delete',
        icon: 'pi pi-times',
        command: (ev) => {
            remove(i);
        }
    },
    {
        label: "Move Up",
        icon: 'pi pi-sort-up',
        command: (ev) => {
            switchBy(idx, -1)
        },
        disabled: (ev) => {
            return idx === 0;
        },
    },
    {
        label: "Move Down",
        icon: 'pi pi-sort-down',
        command: (ev) => {
            switchBy(idx, -1)
        },
        disabled: (ev) => {
            return idx === data.value.length-1
        },
    }];
}


</script>
<template>
    <div class="text-900 font-bold text-6xl text-center">
        Edit the the display boxes.
    </div>
    <div class="text-center">
        <Button label="Save" :disabled="!hasUnsaved()" @click="$emit('update',data)" />
        <Button label="Revert" :disabled="!hasUnsaved()" severity="danger" @click="revert()" />
        <p class="text-red-500" v-if="hasUnsaved()">You have unsaved changes.</p>
    </div>
    <div class="p-3 h-full">
        <div class="shadow-2 p-3 surface-card" style="border-radius: 6px">
            <div class="my-2">
                <InputText placeholder="Box Label" type="text" v-model="newName" />
                <Button severity="success" rounded icon="pi pi-plus" @click="add()" />
            </div>
            <div class="grid p-3">
                <div class="col-3" v-for="(box,i) in data">
                    <Panel>
                        <template #header>
                            <InputText v-if="editing===i" type='text' v-model='changeName' class="w-4" />
                            <div v-else>{{box.name}}</div>
                        </template>
                        <template #icons>
                            <button v-if='editing!==i' class="p-panel-header-icon p-link mr-2" @click="(event) => this.$refs.menu[i].toggle(event)">
                                <span class="pi pi-cog"></span>
                            </button>
                            <Button v-else icon="pi pi-check" text rounded size="small" @click="confirm(i)" :disabled="!changeName"/>
                            <Menu ref="menu" :idx="i" :model="makeMenu(i)" popup></Menu>
                        </template>
                        <p class="m-0">
                            <Chips v-model="box.notes" />
                        </p>
                    </Panel>
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
</style>