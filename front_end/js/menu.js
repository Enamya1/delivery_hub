document.addEventListener('DOMContentLoaded', () => {
    const menuItemsContainer = document.getElementById('item'); // Use the select tag with id 'item'

    // The API endpoint for fetching menu items
    const apiUrl = './data/menu.json'; // Assuming this is the correct endpoint for the menu items

    // Function to fetch menu items from the API
    async function fetchMenuItems() {
        try {
            const response = await fetch(apiUrl);
            if (!response.ok) {
                throw new Error(`Error loading menu items: ${response.status}`);
            }
            const menuItems = await response.json();
            displayMenuItems(menuItems);
        } catch (error) {
            console.error('Error fetching menu items:', error);
            menuItemsContainer.innerHTML = '<option value="">Error loading menu items. Please try again later.</option>';
        }
    }

    // Function to display menu items in the select dropdown
    function displayMenuItems(items) {
        menuItemsContainer.innerHTML = ''; // Clear the existing options

        // Add a default "Select" option
        const defaultOption = document.createElement('option');
        defaultOption.value = '';
        defaultOption.textContent = 'Select Food Item';
        menuItemsContainer.appendChild(defaultOption);

        // Create an option for each menu item
        items.forEach(item => {
            const option = document.createElement('option');
            option.value = item.id;  // Assuming item.id is the unique identifier
            option.textContent = item.name;  // Assuming item.name is the name of the food item
            menuItemsContainer.appendChild(option);
        });
    }

    // Fetch and display menu items on page load
    fetchMenuItems();
});
