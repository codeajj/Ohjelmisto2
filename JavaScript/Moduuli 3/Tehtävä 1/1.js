const ulElement = document.querySelector('#target');

const html = `
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>`

ulElement.classList.add("my-list");
ulElement.innerHTML = html