window.addEventListener("load", mainScript)

function mainScript(){

  //sets HTML variables
  var latInput = document.getElementById("latitudeInput");
  var lonInput = document.getElementById("longitudeInput");

  //requests to get location upon page loading
  getLocation();

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
}
