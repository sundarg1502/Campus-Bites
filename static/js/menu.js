const cart = {
    items: {},
    count: 0
};

// Update quantity
function updateQuantity(productId, change) {
    console.log(productId)
    const input = document.querySelector(`input[data-product-id="${productId}"]`);
    let newValue = parseInt(input.value) + change;
    newValue = Math.max(0, newValue); // Prevent negative values
    input.value = newValue;
}

// Add to cart
// function addToCart(productId) {
//     const input = document.querySelector(`input[data-product-id="${productId}"]`);
//     const quantity = parseInt(input.value);
    
//     if (quantity > 0) {
//         // Update cart count
//         console.log(quantity);
//         // Show success animation
//         const button = document.querySelector('[data-product-id="${productId}"] .add-to-cart-btn');
//         // button.classList.add('success-animation');
//         // button.innerHTML = '<i class="fas fa-check me-2"></i>Added!';
        
//         // Reset after animation
//         // setTimeout(() => {
//         //     button.classList.remove('success-animation');
//         //     button.innerHTML = '<i class="fas fa-cart-plus me-2"></i>Add to Cart';
//         // }, 1500);
        
//         // Reset quantity
//         input.value = 0;
//     }
// }
    function addToCart(productId) {
        // Gather form data
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;

        // Check if form inputs are valid
        if (!name || !email) {
            alert("Please fill in all fields.");
            return;
        }

        // Make the fetch call
        fetch("/your-django-endpoint/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie('csrftoken'), // CSRF token for security
            },
            body: JSON.stringify({ name: name, email: email }),
        })
        .then(response => {
            if (response.ok) {
                return response.json(); // Parse JSON response
            }
            throw new Error("Network response was not ok");
        })
        .then(data => {
            alert("Data submitted successfully: " + JSON.stringify(data));
        })
        .catch(error => {
            console.error("There was a problem with the fetch operation:", error);
            alert("Error submitting data");
        });
    }

    // Function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
