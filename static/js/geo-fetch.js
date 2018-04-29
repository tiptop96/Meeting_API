function dynamicallyLoadScript(url) {
    var script = document.createElement("script"); // Make a script DOM node
    script.src = url; // Set it's src to the provided URL

    document.head.appendChild(script); // Add it to the end of the head section of the page (could change 'head' to 'body' to add it to the end of the body section instead)
}

dynamicallyLoadScript("http://maps.googleapis.com/maps/api/js?key=AIzaSyDuM6eujTcwnwpkRfvnK0TAreyG_E-s1y8")

window.onload= function(){
    geocoder = new google.maps.Geocoder();
    document.getElementById("id_country").onchange = getAndSetLongLat
    document.getElementById("id_city").onchange = getAndSetLongLat
    document.getElementById("id_street").onchange = getAndSetLongLat
}
function getAndSetLongLat() {
    var longlat = document.getElementById("id_longlat")
    var formattedAddress = document.getElementById("id_formatted_address")
    var fullAddress;
    var country = document.getElementById("id_country").value
    var city = document.getElementById("id_city").value
    var street = document.getElementById("id_street").value
    fullAddress = country + " " + city + " " + street;
    serachGoogleAndSetLongLat(fullAddress, longlat, formattedAddress)
}

function serachGoogleAndSetLongLat(address, longlatElement, formattedAddressElement) {

    geocoder.geocode( { 'address' : address }, function( results, status ) {
        if( status == google.maps.GeocoderStatus.OK ) {
            //console.log(results[0])
            formattedAddressElement.value = results[0].formatted_address
            longlatElement.value = results[0].geometry.location.toString()
            //console.log(formattedAddressElement.value)
        } /*else {
            alert( 'Geocode was not successful for the following reason: ' + status );
        }*/
    } );
}