// window.addEventListener("load", mainScript)
var latInput;
var longInput;
var button;
var form;
mainScript();

function mainScript(){

  //sets HTML variables
  latInput = document.getElementById("latitudeInput");
  lonInput = document.getElementById("longitudeInput");
  button = document.getElementById("reportButton");
  form = document.getElementById("hiddenForm")

  //hides button until the location is accessible to prevent error
  button.style.display = "None";

  //reveals button once location is downloaded
  facilitator(() => {button.style.display = "Block";});

  //adds listener for button click
  button.addEventListener("click", onClick);

}

//https://stackoverflow.com/questions/21518381/proper-way-to-wait-for-one-function-to-finish-before-continuing
function facilitator(_callback){
    //requests to get location upon page loading
    getLocation();

    // do some asynchronous work
    // and when the asynchronous stuff is complete
    _callback();
}

//runs when button is clicked
function onClick(){
  //https://www.w3schools.com/jsref/met_win_confirm.asp
  //chance to confirm
  var confirmReport = confirm("Are you sure you want to report an incident?");
  if (confirmReport == true) {
    //submits hidden form
    form.submit()
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
