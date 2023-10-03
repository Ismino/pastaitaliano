/* Messages */
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);

/* Nav bar */

$(document).ready(function () {
    $('.navbar-toggler').click(function () {
        $('body').toggleClass('navbar-expanded');
    });
});

