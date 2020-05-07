function initPage(counterPromise) {
    counterPromise.then(result => console.log(result.value))
}

function dummyResponse() {
    return Promise.resolve({value: 6});
}

function main() {
    const counterPromise = fetch('/counter');
    counterPromise.then(response => initPage(response.json));
}

main()
