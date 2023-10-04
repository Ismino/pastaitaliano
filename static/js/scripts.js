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

/* Map */

function initMap() {
    var stockholm = { lat: 59.3293, lng: 18.0686 }; // Stockholm coordinates
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: stockholm
    });

    var marker = new google.maps.Marker({
        position: stockholm,
        map: map,
        title: 'Stockholm'
    });

}
window.onload = function() {
    initMap();
}



