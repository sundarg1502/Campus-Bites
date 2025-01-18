const cart = {
    items: {},
    count: 0
};

// Update quantity
function updateQuantity(productId, change) {
    const input = document.querySelector(`input[data-product-id="${productId}"]`);
    let newValue = parseInt(input.value) + change;
    newValue = Math.max(0, newValue); // Prevent negative values
    input.value = newValue;
}

// Add to cart
function addToCart(productId) {
    const input = document.querySelector(`input[data-product-id="${productId}"]`);
    const quantity = parseInt(input.value);
    
    if (quantity > 0) {
        // Update cart count
        cart.count += quantity;
        document.getElementById('cartCount').textContent = cart.count;
        
        // Show success animation
        const button = document.querySelector(`[data-product-id="${productId}"] .add-to-cart-btn`);
        button.classList.add('success-animation');
        button.innerHTML = '<i class="fas fa-check me-2"></i>Added!';
        
        // Reset after animation
        setTimeout(() => {
            button.classList.remove('success-animation');
            button.innerHTML = '<i class="fas fa-cart-plus me-2"></i>Add to Cart';
        }, 1500);
        
        // Reset quantity
        input.value = 0;
    }
}