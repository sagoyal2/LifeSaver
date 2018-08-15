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

  //handler to trigger events when Report button clicked
  button.addEventListener("click", onClick);

}

//runs when button is clicked after initial report
function waitToLoad(){
  alert("Please wait for your location to load!")
}

//runs when button is clicked
function onClick(){
  console.log("Report button was clicked!")

  //removes the first handler for when report button is clicked- replaces with normal alert
  //https://www.w3schools.com/jsref/met_element_removeeventlistener.asp
  button.removeEventListener("click", onClick);
  button.addEventListener("click", waitToLoad);

  console.log("Handlers changed!")

  getLocation();

  alert("Your browser may ask if we can access your location. This is needed to accurately report your location. After you give us permission, it may take a few seconds to load your location.")
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


    // })

    //https://www.w3schools.com/jsref/met_win_confirm.asp
    //chance to confirm
    var confirmReport = confirm("Are you sure you want to report an incident?");
    if (confirmReport == true) {
      console.log("FORM SUBMITTING")
      form.submit()
    }

    //in case they cancel, add back handler for report submitting
    button.removeEventListener("click", waitToLoad);
    button.addEventListener("click", onClick);
}

// https://davidwalsh.name/javascript-sleep-function
// https://zeit.co/blog/async-and-await
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}
