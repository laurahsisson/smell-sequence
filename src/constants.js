const Modes = {
    Train: "Train",
    Test: "Test",
    Edit: "Edit"
}

const CardState = {
    Default: 0, // Default state
    Selected: 1, // User actively chooses the card
    Highlighted: 2, // User takes an action that indirectly selects the card
    Danger: 3, // Red alert
}

function deepClone(obj) {
    return JSON.parse(JSON.stringify(obj));
}

function deepEquals(obj1,obj2) {
    return JSON.stringify(obj1) === JSON.stringify(obj2);
}

export { Modes, CardState, deepClone, deepEquals};