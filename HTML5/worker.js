function stopOperation() {
        test();
        var endTime = new Date().getTime() + 5000;
        while(new Date().getTime() < endTime){}
}

onmessage = function(event) {
    var rcvdata = event.data;
    stopOperation();
    var senddata = rcvdata + '백 그라운드에서 동작합니다.';
    this.postMessage(senddata);
}