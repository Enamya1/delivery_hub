const API_BASE_URL = 'https://your-api-url.com'; // Replace with your actual API base URL

// Handle form submission for sign-up
document.getElementById('signup-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (!name || !email || !password) {
        alert('Please fill in all fields.');
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/api/signup`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, email, password })
        });

        if (response.ok) {
            alert('Sign up successful! You can now log in.');
            window.location.href = 'signin.html'; // Redirect to login page
        } else {
            alert('Error signing up. Please try again later.');
        }
    } catch (error) {
        console.error('Error signing up:', error);
        alert('Error signing up. Please try again later.');
    }
});
