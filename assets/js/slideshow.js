const track = document.querySelector(".slideshow-track");
const slides = track.children;

let current = 0;

function showSlide(index) {
  current = (index + slides.length) % slides.length;
  track.style.transform = `translateX(-${current * 100}%)`;
}

document.querySelector(".slideshow-btn-fwd").addEventListener("click", () => {
  showSlide(current + 1);
});

document.querySelector(".slideshow-btn-back").addEventListener("click", () => {
  showSlide(current - 1);
});
