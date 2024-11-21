document.addEventListener('DOMContentLoaded', () => {
    const menuItemsContainer = document.getElementById('menu-items');

    // Local JSON file path
    const localJsonPath = './data/menu.json';

    // Function to fetch menu items from the local JSON file
    async function fetchMenuItems() {
        try {
            const response = await fetch(localJsonPath);
            if (!response.ok) {
                throw new Error(`Error loading JSON file: ${response.status}`);
            }
            const menuItems = await response.json();
            displayMenuItems(menuItems);
        } catch (error) {
            console.error('Error fetching menu items:', error);
            menuItemsContainer.innerHTML = '<p>Error loading menu items. Please try again later.</p>';
        }
    }

    // Function to display menu items on the page
    function displayMenuItems(items) {
        menuItemsContainer.innerHTML = ''; // Clear existing content
        items.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.classList.add('menu-item');
            itemElement.innerHTML = `
                <img src="${item.image_url}" alt="${item.name}" class="menu-item-image">
                <h3>${item.name}</h3>
                <p>${item.description}</p>
                <p>Price: $${item.price.toFixed(2)}</p>
                <button class="order-btn" data-id="${item.id}">Order</button>
            `;
            menuItemsContainer.appendChild(itemElement);
        });

        // Add event listeners to order buttons
        document.querySelectorAll('.order-btn').forEach(button => {
            button.addEventListener('click', () => {
                const itemId = button.getAttribute('data-id');
                alert(`Order placed for item ID: ${itemId}`);
            });
        });
    }

    // Fetch and display menu items on page load
    fetchMenuItems();
});
