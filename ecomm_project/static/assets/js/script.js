
setTimeout(function() {
    let alertBox = document.getElementById("alert-box");
    if (alertBox) {
        alertBox.style.transition = "opacity 0.5s";
        alertBox.style.opacity = "0";
        setTimeout(() => alertBox.style.display = "none", 500); // Completely remove after fade-out
    }
}, 3000);