// onmessage = function(event) {
//     var dataPoint = { x : Math.random() * chartcanvas.width, y : Math.random() * chartcanvas.height };
//     //var dataPoint = event.data;
//     this.postMessage(senddata);
// 
onmessage = function(event) {
    var dataPoint = { x: Math.random() * event.data.x, y: Math.random() * event.data.y };
    // Use event.data.width and event.data.height to get canvas dimensions
    this.postMessage(dataPoint);
}