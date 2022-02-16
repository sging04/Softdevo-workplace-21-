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
var drawDot = (e) => {
  clear(e);

  //window.requestAnimationFrame(callback);
  // tells browser that you wish to perform animation
  ctx.beginPath();
  ctx.arc(c.width / 2, c.height / 2, radius, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke();
  radius += .5;
  requestID=  window.requestAnimationFrame(drawDot);

  }
var stopIt = (rID) => {
  window.cancelAnimationFrame(rID);
}

function grow(e){
  ctx.beginPath();
}
document.getElementById("startButton").addEventListener("click", drawDot);
document.getElementById("stopButton").addEventListener("click",  stopIt);
