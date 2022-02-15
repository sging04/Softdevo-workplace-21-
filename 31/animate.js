var c = document.getElementById("slate");
var stopButton = document.getElementById("stopButton");
var startButton = document.getElementById("startButton");

var ctx = c.getContext("2d");

ctx.fillStyle = "blue";

function clear(e) {
  ctx.clearRect(0,0,c.width, c.height);
}

var radius = 10;
var growing = true;

function drawDot(e) {
  clear(e);

  ctx.beginPath();
  ctx.arc(c.width / 2, c.height / 2, radius, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke();
}
