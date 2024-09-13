let content = document.querySelector('.Grid__grid');
let lastItems = Array.from(content.children).slice(-14);
content.innerHTML = '';
lastItems.forEach(
    item => content.append(item)
)