// Отримуємо всі колонки
const columns = document.querySelectorAll('.marketing .fade-in-up');

// Функція для додавання класу "visible"
const checkVisibility = () => {
    const windowHeight = window.innerHeight;

    columns.forEach(column => {
        const columnTop = column.getBoundingClientRect().top;

        // Анімація починається, коли елемент на 150 пікселів від верхньої частини вікна
        if (columnTop < windowHeight - 150) {
            column.classList.add('visible'); // Додаємо клас для активації анімації
        }
    });
};

// Додаємо слухача подій на прокрутку
window.addEventListener('scroll', checkVisibility);
// Викликаємо функцію при завантаженні сторінки
checkVisibility();

document.addEventListener('DOMContentLoaded', function() {
    const fadeElements = document.querySelectorAll('.fade-in-up');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    });

    fadeElements.forEach(element => {
        observer.observe(element);
    });
});
