var latInput = document.getElementById("latitudeInput");
var lonInput = document.getElementById("longitudeInput");
var button = document.getElementById("reportButton");

button.addEventListener("click", onClick())

function onClick(){

  //https://www.w3schools.com/jsref/met_win_confirm.asp
  var r = confirm("Are you sure you want to report an incident?");
  if (r == true) {
    getLocation();
  }
}

}

//https://www.w3schools.com/htmL/html5_geolocation.asp
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        console.log("Geolocation is not supported by this browser.");
    }
}
function showPosition(position) {
    latInput.value = position.coords.latitude;
    lonInput.value = position.coords.longitude;
    console.log(latInput.value);
    console.log(lonInput.value);
}
