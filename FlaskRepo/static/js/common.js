// import {colorfulog,logCurrentTime} from './util'

const portnum = 10089
let host = "http://127.0.0.1"
const colon = ":"


let currentIndex = 0

let autoScrollId = -1


let jq = jQuery.noConflict()

function logCurrentTime() {
    let time = new Date().getTime()
    console.log(time)
}

window.onload = function () {
    logCurrentTime()
}

window.onunload = function () {
    console.log('window unload')
}


jq(document).ready(function () {
    addlistener()
});

function addlistener() {
    jq('#next').click(function () {
        console.log('next')
        nextImage()
    })

    jq('#prev').click(function () {
        console.log('prev')
        prevImage()
    })

    jq('#autoScroll').click(function () {
        autoScroll()
    })

    jq('#cancelScroll').click(function () {
            cancelAutoScroll()
    })







    function nextImage() {
        currentIndex = currentIndex + 1;
        if (currentIndex >= 27) {
            currentIndex = 1
        }
        let image_src = host + colon+portnum + "/img/" + currentIndex;
        jq('#main_img').attr('src', image_src).width('300px').height('auto')

    }

    function prevImage() {
        currentIndex = currentIndex - 1;
        if (currentIndex <= 0) {
            currentIndex = 50
        }
        let image_src = host +colon+ portnum + "/img/" + currentIndex;
        jq('#main_img').attr('src', image_src).width('auto').height('auto')
    }

    function autoScroll() {
        autoScrollId = setInterval(function () {
            console.log("currentTime is" + new Date().getMilliseconds())
            nextImage()
        }, 500)
    }

    function cancelAutoScroll() {
        console.log(autoScrollId)
        if (autoScrollId >0) {
            clearInterval(autoScrollId)
            console.log('cancel auto scroll')
        }
    }


}


