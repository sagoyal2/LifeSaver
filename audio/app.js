// set up basic variables for app

var record = document.querySelector('.record');
var stop = document.querySelector('.stop');
var soundClips = document.querySelector('.sound-clips');
var canvas = document.querySelector('.visualizer');
var mainSection = document.querySelector('.main-controls');
// var hiddenInputURL = document.querySelector('#url');

var blobContents;

// var submitButton = document.querySelector('#submitButton');
// submitButton.onclick = function() {

function uploadAudio(){
  var HTML_apiKey = document.querySelector('#firebase_apiKey');
  var HTML_authDomain = document.querySelector('#firebase_authDomain');
  var HTML_databaseURL = document.querySelector('#firebase_databaseURL');
  var HTML_projectId = document.querySelector('#firebase_projectId');
  var HTML_storageBucket = document.querySelector('#firebase_storageBucket');
  var HTML_messagingSenderId = document.querySelector('#firebase_messagingSenderId');

  // Initialize Firebase
  var config = {
    apiKey: HTML_apiKey.value,
    authDomain: HTML_authDomain.value,
    databaseURL: HTML_databaseURL.value,
    projectId: HTML_projectId.value,
    storageBucket: HTML_storageBucket.value,
    messagingSenderId: HTML_messagingSenderId.value
  };
  firebase.initializeApp(config);

  console.log("initialized app!")

  // Get a reference to the storage service, which is used to create references in your storage bucket
  var storage = firebase.storage();

  // Create a root reference
  var storageRef = firebase.storage().ref();

  var fileName = 'message' + Date.now() + '.ogg';
  console.log(fileName);
  var fileNameInput = document.querySelector('#fileNameInput');
  // fileNameInput.innerHTML = "Video Name: " + fileName;
  fileNameInput.value = fileName;

  var filePath = 'audio/' + fileName;
  console.log(filePath);
  var filePathInput = document.querySelector('#filePathInput');
  // filePathInput.innerHTML = "Video Path: " + filePath;
  filePathInput.value = filePath;

  // Create a reference to 'mountains.jpg'
  var messageRef = storageRef.child(fileName);

  // Create a reference to 'images/mountains.jpg'
  var messageAudioRef = storageRef.child(filePath);

  // // While the file names are the same, the references point to different files
  // mountainsRef.name === mountainImagesRef.name            // true
  // mountainsRef.fullPath === mountainImagesRef.fullPath    // false

  console.log(blobContents)

  //THESE RESOURCES USED
  //https://firebase.google.com/docs/storage/web/start
  //https://firebase.google.com/docs/storage/web/create-reference
  //https://firebase.google.com/docs/storage/web/upload-files

  var file = blobContents // use the Blob or File API
  messageAudioRef.put(file).then(function(snapshot) {
    console.log('Uploaded a blob or file!');
    // console.log("BEFORE JQUERY POST")
    // $.post("/report")
    // console.log("AFTER JQUERY POST")
  });

  var x = "TEMP"

}


// disable stop button while not recording

stop.disabled = true;

// visualiser setup - create web audio api context and canvas

var audioCtx = new (window.AudioContext || webkitAudioContext)();
var canvasCtx = canvas.getContext("2d");

//main block for doing the audio recording

if (navigator.mediaDevices.getUserMedia) {
  console.log('getUserMedia supported.');

  var constraints = { audio: true };
  var chunks = [];

  var onSuccess = function(stream) {
    var mediaRecorder = new MediaRecorder(stream);

    visualize(stream);

    record.onclick = function() {
      mediaRecorder.start();
      console.log(mediaRecorder.state);
      console.log("recorder started");
      record.style.background = "red";

      stop.disabled = false;
      record.disabled = true;
    }

    stop.onclick = function() {
      mediaRecorder.stop();
      console.log(mediaRecorder.state);
      console.log("recorder stopped");
      record.style.background = "";
      record.style.color = "";
      // mediaRecorder.requestData();

      stop.disabled = true;
      record.disabled = false;
    }

    mediaRecorder.onstop = function(e) {
      console.log("data available after MediaRecorder.stop() called.");

      //var clipName = prompt('Enter a name for your sound clip?','My unnamed clip');
      var clipName = "Your Recorded Message"
      console.log(clipName);
      var clipContainer = document.createElement('article');
      var clipLabel = document.createElement('p');
      var audio = document.createElement('audio');
      var deleteButton = document.createElement('button');

      clipContainer.classList.add('clip');
      audio.setAttribute('controls', '');
      // deleteButton.textContent = 'Delete';
      // deleteButton.className = 'delete';

      if(clipName === null) {
        clipLabel.textContent = 'My unnamed clip';
      } else {
        clipLabel.textContent = clipName;
      }

      clipContainer.appendChild(audio);
      clipContainer.appendChild(clipLabel);
      // clipContainer.appendChild(deleteButton);
      soundClips.appendChild(clipContainer);

      audio.controls = true;
      var blob = new Blob(chunks, { 'type' : 'audio/ogg; codecs=opus' });
      //var blob = new Blob(chunks, { 'type' : 'audio/wav; codecs=opus' }); //THIS SHOULD DO THE TRICK FOR WAV

      blobContents = blob;
      chunks = [];
      var audioURL = window.URL.createObjectURL(blob);
      audio.src = audioURL;
      console.log("recorder stopped");
      //hiddenInputURL.value = audioURL;
      console.log(audioURL);

      // deleteButton.onclick = function(e) {
      //   evtTgt = e.target;
      //   evtTgt.parentNode.parentNode.removeChild(evtTgt.parentNode);
      // }

      // clipLabel.onclick = function() {
      //   var existingName = clipLabel.textContent;
      //   var newClipName = prompt('Enter a new name for your sound clip?');
      //   if(newClipName === null) {
      //     clipLabel.textContent = existingName;
      //   } else {
      //     clipLabel.textContent = newClipName;
      //   }
      // }

      uploadAudio();
    }

    mediaRecorder.ondataavailable = function(e) {
      chunks.push(e.data);
    }
  }

  var onError = function(err) {
    console.log('The following error occured: ' + err);
  }

  navigator.mediaDevices.getUserMedia(constraints).then(onSuccess, onError);

} else {
   console.log('getUserMedia not supported on your browser!');
}

function visualize(stream) {
  var source = audioCtx.createMediaStreamSource(stream);

  var analyser = audioCtx.createAnalyser();
  analyser.fftSize = 2048;
  var bufferLength = analyser.frequencyBinCount;
  var dataArray = new Uint8Array(bufferLength);

  source.connect(analyser);
  //analyser.connect(audioCtx.destination);

  draw()

  function draw() {
    WIDTH = canvas.width
    HEIGHT = canvas.height;

    requestAnimationFrame(draw);

    analyser.getByteTimeDomainData(dataArray);

    canvasCtx.fillStyle = 'rgb(200, 200, 200)';
    canvasCtx.fillRect(0, 0, WIDTH, HEIGHT);

    canvasCtx.lineWidth = 2;
    canvasCtx.strokeStyle = 'rgb(0, 0, 0)';

    canvasCtx.beginPath();

    var sliceWidth = WIDTH * 1.0 / bufferLength;
    var x = 0;


    for(var i = 0; i < bufferLength; i++) {

      var v = dataArray[i] / 128.0;
      var y = v * HEIGHT/2;

      if(i === 0) {
        canvasCtx.moveTo(x, y);
      } else {
        canvasCtx.lineTo(x, y);
      }

      x += sliceWidth;
    }

    canvasCtx.lineTo(canvas.width, canvas.height/2);
    canvasCtx.stroke();

  }
}

window.onresize = function() {
  canvas.width = mainSection.offsetWidth;
}

window.onresize();
