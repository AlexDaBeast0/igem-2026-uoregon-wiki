// based on https://www.nieknijland.nl/blog/make-a-responsive-carousel-with-just-css
function handleClick(direction, button) {
    const carousel = button.closest(".carousel-container");
    const list = carousel.querySelector(".carousel-list");
    const itemWidth = list.querySelector("li").offsetWidth;

    const scrollAmount = direction === "previous" ? -itemWidth : itemWidth;
    list.scrollBy({ left: scrollAmount, behavior: "smooth" });
}
