async function initPage(counterPromise) {
    // counterPromise.then(result => console.log(result.value))
    try {
        const result = await counterPromise;
        setCounterValue(result.value);
        setEventHandlers();
    } catch (error) {
        console.error(error);
    }
}

function setEventHandlers() {
    // TODO
}

function setCounterValue(value) {
    const counterElement = document.getElementById('counter-value');
    counterElement.innerText = value;
}

function dummyResponse() {
    return Promise.resolve({value: 6});
}

function main() {
    const counterPromise = fetch('/counter');
    counterPromise.then(response => initPage(response.json()));
}

main()
