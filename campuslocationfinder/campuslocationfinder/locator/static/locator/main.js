// main.js
let origin, destination
let directionsRenderer, directionsService
// Define the initMap function for initializing the Google Map.
function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 8.98921, lng: 7.18141 },
        zoom: 6 // Adjust the zoom level as needed
    });
     var startpointautocomplete = new google.maps.places.Autocomplete(
        document.getElementById('origin')
    )
    var destinationautocomplete = new google.maps.places.Autocomplete(
        document.getElementById('destination')
    )
    document.getElementById('getDirection').addEventListener('click', getDirections);
    // Now, you have an initialized map.

}

function getDirections() {
    var origin = document.getElementById('origin').value;
    var destination = document.getElementById('destination').value;
    var travelMode = "DRIVING";

    // Log the values before sending the AJAX request.
    console.log("Origin:", origin);
    console.log("Destination:", destination);

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12, // Adjust the zoom level as needed
        center: { lat: 8.98921, lng: 7.18141  } // Set the initial map center coordinates
    });

    directionsService = new google.maps.DirectionsService();
    directionsRenderer = new google.maps.DirectionsRenderer({ map: map });

    var request = {
        origin: origin,
        destination: destination,
        travelMode: travelMode
    };
    directionsService.route(request, function (response, status) {
        if (status === 'OK') {
            // Display the directions on the map
            directionsRenderer.setDirections(response);
        } else {
            // Handle the error
            console.error('Directions request failed:', status);
        }
    });



}

// Event listener for the "Get Directions" button.
document.addEventListener('DOMContentLoaded', initMap);
