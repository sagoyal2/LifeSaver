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

  //while location is loading, this handler alerts that the user needs to wait
  button.addEventListener("click", waitToLoad);

  getLocation();

}

//runs when button is clicked
function waitToLoad(){
  alert("You need to wait for your location to load!")
}

//runs when button is clicked
function onClick(){
  //https://www.w3schools.com/jsref/met_win_confirm.asp
  //chance to confirm
  var confirmReport = confirm("Are you sure you want to report an incident?");
  if (confirmReport == true) {
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

    // console.log("TEST 1")
    // //waits a certain amount of time before it changes listener
    // sleep(2000).then(() => {
    //     // Do something after the sleep!
    // console.log("TEST 2")

    //removes the first alert when button is clicked- replaces with confirm/post method
    //https://www.w3schools.com/jsref/met_element_removeeventlistener.asp
    button.removeEventListener("click", waitToLoad);
    button.addEventListener("click", onClick);
    // })
}

// https://davidwalsh.name/javascript-sleep-function
// https://zeit.co/blog/async-and-await
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}
