       
       
       
 let cartItems = [
    { id: 1, name: 'Margherita Pizza', price: 12.99, quantity: 1 },
    { id: 2, name: 'Burger Combo', price: 15.99, quantity: 2 },
    { id: 3, name: 'Caesar Salad', price: 8.99, quantity: 1 }
];

// Initialize floating food items
const foodEmojis = ['🍕', '🍔', '🍟', '🌮', '🥗', '🍜', '☕'];
const floatingItems = document.getElementById('floatingItems');

for (let i = 0; i < 20; i++) {
    const item = document.createElement('div');
    item.className = 'floating-item';
    item.textContent = foodEmojis[Math.floor(Math.random() * foodEmojis.length)];
    item.style.setProperty('--rotation', `${Math.random() * 360}deg`);
    item.style.left = `${Math.random() * 100}%`;
    item.style.top = `${Math.random() * 100}%`;
    item.style.fontSize = `${Math.random() * 30 + 20}px`;
    floatingItems.appendChild(item);

    // Random floating animation
    gsap.to(item, {
        y: `${Math.random() * 100 - 50}px`,
        x: `${Math.random() * 100 - 50}px`,
        rotation: `${Math.random() * 360}deg`,
        duration: Math.random() * 5 + 5,
        repeat: -1,
        yoyo: true,
        ease: 'none'
    });
}

// Cart functionality
function updateCart() {
    const cartContainer = document.getElementById('cartItems');
    const totalItems = cartItems.reduce((sum, item) => sum + item.quantity, 0);
    const totalAmount = cartItems.reduce((sum, item) => sum + item.price * item.quantity, 0);

    // Update cart count
    document.getElementById('itemCount').textContent = `${totalItems} items`;
    document.getElementById('totalAmount').textContent = `$${totalAmount.toFixed(2)}`;
    document.getElementById('checkoutBtn').textContent = `Checkout (${totalItems} items)`;

    // Render cart items
    cartContainer.innerHTML = cartItems.map(item => `
        <div class="cart-item" data-id="${item.id}">
            <div class="item-details">
                <h3>${item.name}</h3>
                <div class="item-price">$${item.price.toFixed(2)}</div>
            </div>
            <div class="quantity-controls">
                <button class="quantity-btn" onclick="updateQuantity(${item.id}, -1)">-</button>
                <span class="quantity">${item.quantity}</span>
                <button class="quantity-btn" onclick="updateQuantity(${item.id}, 1)">+</button>
                <div class="subtotal">$${(item.price * item.quantity).toFixed(2)}</div>
                <button class="remove-btn" onclick="removeItem(${item.id})">×</button>
            </div>
        </div>
    `).join('');
}

function updateQuantity(id, change) {
    const item = cartItems.find(item => item.id === id);
    if (item) {
        item.quantity = Math.max(1, item.quantity + change);
        updateCart();
    }
}

function removeItem(id) {
    cartItems = cartItems.filter(item => item.id !== id);
    updateCart();
}

// Initialize cart
updateCart();

// Checkout button click handler
document.getElementById('checkoutBtn').addEventListener('click', () => {
    alert('Proceeding to checkout...');
});