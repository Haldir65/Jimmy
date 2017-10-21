
window.onload = function () {
logCurrentTime()
console.log('now the frame is loaded')
}

function logCurrentTime() {
var time =  new Date().getTime()
console.log(time)
}

let jq=jQuery.noConflict()

let canlog = true// switch for log

var currentIndex = 0

jq(document).ready(function(){
addlistener()

});

function addlistener() {
jq('#next').click(function () {
currentIndex = currentIndex+1;
if(currentIndex>=50){
currentIndex=1
}
let image_src= "http://127.0.0.1:10089/img/"+currentIndex;
jq('#main_img').attr('src',image_src).width('auto').height('auto')

})

jq('#prev').click(function () {
currentIndex=currentIndex-1;
if(currentIndex<=0){
currentIndex=50
}
let image_src= "http://127.0.0.1:10089/img/"+currentIndex;
jq('#main_img').attr('src',image_src).width('auto').height('auto')
})
}

function colorfulog(msg) {
if (canlog) {
console.log("%c "+msg,"background-image:-webkit-gradient( linear, left top,right top, color-stop(0, #00a419),color-stop(0.15, #f44336), color-stop(0.29, #ff4300),color-stop(0.3, #AA00FF),color-stop(0.4, #8BC34A), color-stop(0.45, #607D8B),color-stop(0.6, #4096EE), color-stop(0.75, #D50000),color-stop(0.9, #4096EE), color-stop(1, #FF1A00));color:transparent;-webkit-background-clip:text;font-size:13px;");
}
}
