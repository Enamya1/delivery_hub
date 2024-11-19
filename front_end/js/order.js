// Fetch food items for the order form
fetch('https://api.example.com/menu')
    .then(response => response.json())
    .then(data => {
        const selectElement = document.getElementById('item');
        data.forEach(item => {
            const option = document.createElement('option');
            option.value = item.id;
            option.textContent = item.name;
            selectElement.appendChild(option);
        });
    });

// Handle form submission to create an order
document.getElementById('order-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const orderData = {
        itemId: document.getElementById('item').value,
        address: document.getElementById('address').value,
    };
    fetch('https://api.example.com/orders
