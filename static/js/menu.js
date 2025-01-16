// Animation for category cards
const cards = document.querySelectorAll('.card');
        
gsap.to(cards, {
    opacity: 1,
    y: 0,
    duration: 0.8,
    stagger: 0.2,
    ease: "power2.out"
});

// Filter buttons interaction
const filterBtns = document.querySelectorAll('.filter-btn');

filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        // Animate cards on filter change
        gsap.fromTo(cards, 
            { opacity: 0, y: 30 },
            { 
                opacity: 1, 
                y: 0, 
                duration: 0.5, 
                stagger: 0.1,
                ease: "power2.out"
            }
        );
    });
});