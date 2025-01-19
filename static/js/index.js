// Optimized animations with better performance
document.addEventListener('DOMContentLoaded', () => {
    // Initialize animations only when page is loaded
    initializeAnimations();
    initializeScrollEffects();
    initializeFloatingItems();
});

function initializeAnimations() {
    // Hero section animations
    const heroElements = [
        { element: '.hero h1', delay: 0 },
        { element: '.hero p', delay: 300 },
        { element: '.cta-button', delay: 600 }
    ];

    heroElements.forEach(({ element, delay }) => {
        const el = document.querySelector(element);
        if (el) {
            setTimeout(() => {
                el.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
                el.style.opacity = '1';
                el.style.transform = 'translateY(0)';
            }, delay);
        }
    });
}

function initializeScrollEffects() {
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                if (entry.target.classList.contains('masonry-item')) {
                    entry.target.style.transitionDelay = `${entry.target.dataset.index * 100}ms`;
                }
            }
        });
    }, observerOptions);

    // Observe category title
    const categoryTitle = document.querySelector('.category h2');
    if (categoryTitle) {
        scrollObserver.observe(categoryTitle);
    }

    // Observe masonry items
    const masonryItems = document.querySelectorAll('.masonry-item');
    masonryItems.forEach((item, index) => {
        item.dataset.index = index;
        scrollObserver.observe(item);
    });
}

function initializeFloatingItems() {
    const foodEmojis = ['🍕', '🍔', '🍟', '🌮', '🥗', '🍜', '☕'];
    const floatingItems = document.getElementById('floatingItems');
    
    if (!floatingItems) return;

    // Clear existing items
    floatingItems.innerHTML = '';

    // Create new floating items with optimized animations
    for (let i = 0; i < 12; i++) {
        const item = document.createElement('div');
        item.className = 'floating-item';
        item.textContent = foodEmojis[Math.floor(Math.random() * foodEmojis.length)];
        
        // Set initial position
        const randomX = Math.random() * 100;
        const randomY = Math.random() * 100;
        
        item.style.cssText = `
            left: ${randomX}%;
            top: ${randomY}%;
            font-size: ${Math.random() * 20 + 15}px;
            opacity: 0.1;
            transform: translate(-50%, -50%);
        `;

        floatingItems.appendChild(item);

        // Efficient animation using CSS transforms
        animateFloatingItem(item);
    }
}

function animateFloatingItem(item) {
    const duration = 5000 + Math.random() * 5000;
    const startPos = {
        x: parseFloat(item.style.left),
        y: parseFloat(item.style.top)
    };

    function update() {
        const time = Date.now() * 0.001;
        const offsetX = Math.sin(time) * 30;
        const offsetY = Math.cos(time * 0.8) * 30;

        item.style.transform = `
            translate(
                calc(${offsetX}px - 50%),
                calc(${offsetY}px - 50%)
            )
            rotate(${Math.sin(time) * 20}deg)
        `;

        requestAnimationFrame(update);
    }

    requestAnimationFrame(update);
}

// Optional: Add smooth scrolling for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Optional: Add loading animation for images
document.querySelectorAll('.masonry-item img').forEach(img => {
    img.addEventListener('load', function() {
        this.style.opacity = '1';
    });
});