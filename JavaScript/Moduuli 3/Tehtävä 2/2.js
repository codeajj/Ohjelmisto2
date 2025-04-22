const target = document.getElementById('target');

const ul = document.createElement('ul');

ul.innerHTML = `
<li>First item</li>
<li class="my-item">Second item</li>
<li>Third item</li>`

target.appendChild(ul);