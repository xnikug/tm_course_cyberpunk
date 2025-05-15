// filepath: d:\src\utm\tasks\tm\tm1\static\js\script.js
document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll(".menu a");
    
    links.forEach(link => {
        link.addEventListener("click", function(event) {
            event.preventDefault();
            const room = this.getAttribute("href").split("=")[1];
            loadRoom(room);
        });
    });

    function loadRoom(room) {
        fetch(`/?room=${room}`)
            .then(response => response.text())
            .then(data => {
                document.body.innerHTML = data;
            })
            .catch(error => console.error("Error loading room:", error));
    }
});