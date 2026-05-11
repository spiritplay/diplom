const cards = document.querySelectorAll('.course-card');

cards.forEach((card) => {
    card.addEventListener('mouseenter', () => {
        card.style.transform = 'translateY(-6px)';
        card.style.transition = '0.25s';
    });

    card.addEventListener('mouseleave', () => {
        card.style.transform = 'translateY(0)';
    });
});
