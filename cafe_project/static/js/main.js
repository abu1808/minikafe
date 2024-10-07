// Эффект при добавлении в корзину
const buttons = document.querySelectorAll('button');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        // Создание эффекта при добавлении в корзину
        const originalText = button.innerText; // Сохраняем текст кнопки
        button.innerText = 'Добавлено!'; // Изменяем текст на "Добавлено!"
        
        setTimeout(() => {
            button.innerText = originalText; // Возвращаем оригинальный текст через 1 секунду
        }, 1000);

        // Эффект анимации при нажатии
        button.classList.add('clicked');
        setTimeout(() => {
            button.classList.remove('clicked');
        }, 300);
    });
});
