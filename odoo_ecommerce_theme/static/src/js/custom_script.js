document.addEventListener('DOMContentLoaded', function() {
    const navItems = document.querySelectorAll('.navbar-nav .nav-item');

    navItems.forEach(item => {
        item.addEventListener('mouseover', function() {
            const hoverContent = item.querySelector('.hover-content');
            hoverContent.style.display = 'block';
        });

        item.addEventListener('mouseout', function() {
            const hoverContent = item.querySelector('.hover-content');
            hoverContent.style.display = 'none';
        });
    });
});
document.addEventListener('DOMContentLoaded', function () {
const sliderContainer = document.querySelector('.slider-container');
const sliderItems = document.querySelectorAll('.slider-item');
const prevButton = document.querySelector('.slider-prev');
const nextButton = document.querySelector('.slider-next');
const totalItems = sliderItems.length;
const itemsToShow = 4; // Number of items to show at a time
let currentIndex = 0;

function updateSliderPosition() {
    const offset = -currentIndex * (100 / itemsToShow); // Adjust offset based on visible items
    sliderContainer.style.transform = `translateX(${offset}%)`;
}

function goToNextSlide() {
    if (currentIndex >= totalItems - itemsToShow) {
        currentIndex = 0; // Loop back to the beginning
    } else {
        currentIndex++;
    }
    updateSliderPosition();
}

function goToPreviousSlide() {
    if (currentIndex &lt;= 0) {
        currentIndex = totalItems - itemsToShow; // Loop to the end
    } else {
        currentIndex--;
    }
    updateSliderPosition();
}

prevButton.addEventListener('click', goToPreviousSlide);
nextButton.addEventListener('click', goToNextSlide);

updateSliderPosition(); // Initialize the slider position
});
