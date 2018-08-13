window.addEventListener("load", mainScript)

function mainScript(){

  //sets HTML variables
  var latInput = document.getElementById("latitudeInput");
  var lonInput = document.getElementById("longitudeInput");
  var button = document.getElementById("reportButton");

  //requests to get location upon page loading
  getLocation();

  //adds listener for button click
  button.addEventListener("click", onClick);

  //runs when button is clicked
  function onClick(){

    //https://www.w3schools.com/jsref/met_win_confirm.asp
    //chance to confirm
    var confirmReport = confirm("Are you sure you want to report an incident?");
    if (confirmReport == true) {
      //calls post method
      console.log("POST")
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
}
