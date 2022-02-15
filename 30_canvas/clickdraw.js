

// clickdraw.js



var c = document.getElementById('slate');

var ctx = c.getContext("2d");

var mode = "rect";

// e means event
function toggleMode(e) {
  console.log("toggleing..............");

}


function drawRect(e) {
  var
  console.log("draw rect");
}

function drawCircle(e) {
  console.log("drawCircle");
}


function draw(e) {
    e.
}


function wipeCanvas(e) {

}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", draw);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", );
