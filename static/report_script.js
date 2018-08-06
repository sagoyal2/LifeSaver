//https://developers.google.com/web/fundamentals/media/recording-audio/
//https://developer.mozilla.org/en-US/docs/Web/API/MediaStream_Recording_API
var player = document.getElementById('player');

var handleSuccess = function(stream) {
  var context = new AudioContext();
    var source = context.createMediaStreamSource(stream);
    var processor = context.createScriptProcessor(1024, 1, 1);

    source.connect(processor);
    processor.connect(context.destination);

    processor.onaudioprocess = function(e) {
      // Do something with the data, i.e Convert this to WAV
      console.log(e.inputBuffer);
    };
};

navigator.mediaDevices.getUserMedia({ audio: true, video: false })
    .then(handleSuccess);

    var chunks = [];

     mediaRecorder.onstop = function(e) {
       console.log("data available after MediaRecorder.stop() called.");

       var audio = document.createElement('audio');
       audio.controls = true;
       var blob = new Blob(chunks, { 'type' : 'audio/ogg; codecs=opus' });
       var audioURL = window.URL.createObjectURL(blob);
       audio.src = audioURL;
       console.log("recorder stopped");
     }

     mediaRecorder.ondataavailable = function(e) {
       chunks.push(e.data);
     }
