// order.js

document.addEventListener('DOMContentLoaded', function () {
    const menuSelect = document.getElementById('item');
    const orderForm = document.getElementById('order-form');
    
    // Fetch menu items from API
    fetch('http://127.0.0.1:5000/menu_items')
        .then(response => response.json())
        .then(data => {
            // Populate the menu dropdown
            data.forEach(item => {
                const option = document.createElement('option');
                option.value = item.id;
                option.textContent = `${item.name} - $${item.price}`;
                menuSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching menu items:', error);
        });

    // Handle form submission
    orderForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const selectedItemId = menuSelect.value;
        const address = document.getElementById('address').value;

        const orderData = {
            item_id: selectedItemId,
            delivery_address: address,
        };

        // Send order data to the API
        fetch('http://127.0.0.1:5000/orders', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(orderData),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Order placed successfully!');
                orderForm.reset();
            } else {
                alert('Error placing order. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error placing order:', error);
        });
    });
});
