
// Animation for page elements
gsap.to('.section-title', {
    opacity: 1,
    y: 0,
    duration: 1,
    scrollTrigger: {
        trigger: '.section-title'
    }
});

gsap.to('.contact-grid', {
    opacity: 1,
    y: 0,
    duration: 1,
    delay: 0.3,
    scrollTrigger: {
        trigger: '.contact-grid'
    }
});

gsap.to('.location-map', {
    opacity: 1,
    y: 0,
    duration: 1,
    delay: 0.5,
    scrollTrigger: {
        trigger: '.location-map'
    }
});

// Form submission handling
document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Thank you for your message! We will get back to you soon.');
    this.reset();
});
