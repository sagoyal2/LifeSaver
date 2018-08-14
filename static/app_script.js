// window.addEventListener("load", mainScript)
var latInput;
var longInput;
var button;
var form;
var buttonDiv;
mainScript();

function mainScript(){

  //sets HTML variables
  latInput = document.getElementById("latitudeInput");
  lonInput = document.getElementById("longitudeInput");
  button = document.getElementById("reportButton");
  buttonDiv = document.getElementById("reportButtonDiv");
  form = document.getElementById("hiddenForm")

  //hides button until the location is accessible to prevent error
  //https://www.w3schools.com/jsref/prop_style_display.asp
  buttonDiv.style.display = "none";

  facilitator(() => {

    //reveals button once location is downloaded - this currently doesn't work
    buttonDiv.style.display = "block";

    //also adds listener for button click once location is downloaded
    button.addEventListener("click", onClick);

});
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
    //submits hidden form, waiting a certain amount of time before it submits [currently 3 seconds]
    //https://stackoverflow.com/questions/8133947/how-to-wait-for-a-period-of-time-after-a-function-run/8133991
    setTimeout(function() {
    // rest of code here
    }, 3000);
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
