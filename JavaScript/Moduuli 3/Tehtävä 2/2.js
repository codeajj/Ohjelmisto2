const ulElement = document.querySelector('#target');

const li = document.createElement('ul');

li.innerHTML = `<li>First item</li>
                <li>Second item</li>
                <li>Third item</li>`

document.getElementById("target").appendChild(li);

ulElement.classList.add('my-item')
ulElement.innerHTML = li.innerHTML;