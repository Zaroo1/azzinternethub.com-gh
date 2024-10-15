document.addEventListener('DOMContentLoaded', function () {
    console.log('AZZ Internet Hub website loaded');
});

// JavaScript remains the same. Add this to your existing JavaScript

// Function to enlarge image in modal
function enlargeImage(img) {
    const modal = document.getElementById("imageModal");
    const modalImg = document.getElementById("modalImage");
    modal.style.display = "block";
    modalImg.src = img.src;
}

// Function to close the modal
function closeModal() {
    const modal = document.getElementById("imageModal");
    modal.style.display = "none";
}

// Handle Rating Form Submission
document.querySelector('.rate-us form').addEventListener('submit', function(event) {
    event.preventDefault();
    const rating = document.getElementById('rating').value;
    alert('Thank you for rating us ' + rating + ' stars!');
});

// Handle Newsletter Subscription Form Submission
document.querySelector('.subscribe form').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('newsletter-email').value;
    alert('Thank you for subscribing with ' + email + '!');
});
