// Fetch menu items and display them on the Menu page
fetch('./menu.json')
    .then(response => response.json())
    .then(data => {
        const menuContainer = document.getElementById('menu-items');
        data.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.classList.add('menu-item');
            itemElement.innerHTML = `
                <img src="${item.image_url}" alt="${item.name}">
                <h3>${item.name}</h3>
                <p>${item.description}</p>
                <span>$${item.price}</span>
            `;
            menuContainer.appendChild(itemElement);
        });
    });
