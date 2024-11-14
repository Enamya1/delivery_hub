// Define the API base URL in a variable
const apiBaseUrl = "http://127.0.0.1:5000";  // API address
console.log("jdasodfasd")
// Function to handle user signup
document.getElementById("signup-form").addEventListener("submit", function(e) {
    e.preventDefault();
    const username = document.getElementById("signup-username").value;
    const email = document.getElementById("signup-email").value;
    const password = document.getElementById("signup-password").value;
    
    fetch(`${apiBaseUrl}/signup`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password,
            email: email
        })
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
});

// Function to handle user login
document.getElementById("login-form").addEventListener("submit", function(e) {
    e.preventDefault();
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;
    
    fetch(`${apiBaseUrl}/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
});

// Fetch all users from API
function fetchUsers() {
    fetch(`${apiBaseUrl}/users`)
    .then(response => response.json())
    .then(data => {
        const userList = document.getElementById("user-list");
        userList.innerHTML = "";
        data.forEach(user => {
            const li = document.createElement("li");
            li.textContent = `Username: ${user.username}, Email: ${user.email}`;
            userList.appendChild(li);
        });
    })
    .catch(error => console.error('Error:', error));
}
