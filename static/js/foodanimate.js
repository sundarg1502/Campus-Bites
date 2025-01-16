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