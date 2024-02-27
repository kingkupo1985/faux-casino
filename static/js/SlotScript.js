document.addEventListener("DOMContentLoaded", function() {
    // Add the 'active' class to all .col elements to start all animations simultaneously
    document.querySelectorAll('.col').forEach(function(col) {
        col.classList.add('active');
    });
});
