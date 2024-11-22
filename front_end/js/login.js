const API_BASE_URL = 'https://your-api-url.com'; // Replace with your actual API base URL

// Handle form submission for login
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (!email || !password) {
        alert('Please enter both email and password.');
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/api/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email, password })
        });

        if (response.ok) {
            const data = await response.json();
            alert('Login successful!');
            // Optionally, store user data or token for session management
            // localStorage.setItem('token', data.token);
            window.location.href = 'index.html'; // Redirect to homepage or dashboard
        } else {
            alert('Invalid credentials.');
        }
    } catch (error) {
        console.error('Error logging in:', error);
        alert('Error logging in. Please try again later.');
    }
});
