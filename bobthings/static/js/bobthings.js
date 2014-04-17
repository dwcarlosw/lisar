window.onload=getStuff;
window.addEventListener( 'load', doFirst, false );

function doFirst(){
//    initPlayer();
//    initCanvas();
//    initDragAndDrop();
//    initSavingData();

    window.addEventListener("scroll", on_scroll, false );
    footer = document.getElementById("footer");
    footer_arrow = document.getElementById("footer_arrow");
    footer_arrow.addEventListener("mouseover", on_mouseover_arrow, false );
    footer.addEventListener("mouseleave", on_mouseleave_footer, false);

    lan_as = document.getElementsByClassName("lan_a");
    for(var l=0; l<lan_as.length; l++){
        lan_a.addEventListener("click", on_choose_language, false)
    }


    display();
}

function on_mousemove( e ){

    canvas.clearRect( 0, 0, 600, 400 );
    var xPos = e.clientX;
    var yPos = e.clientY;
    canvas.fillRect( xPos, yPos, 20, 20 );
}

function on_scroll(e){
    var doc = document.documentElement, body = document.body;
    var top = (doc && doc.scrollTop  || body && body.scrollTop  || 0);
    var div_header = document.getElementById("div_header");
    var div_header_style = window.getComputedStyle(div_header);
    var header_top = div_header_style.getPropertyValue("top");

    if ( top > 0 && header_top == "0px" ){
        div_header.style.top = "-46px";
    }
    else if( top == 0 && header_top == "-46px" ){
        div_header.style.top = "0px";
    }

}

function on_dragStart(e){
    var code = rightbox.innerHTML;
    e.dataTransfer.setData('Text', code);
}

function on_dragEnd(e){
    pic = e.target;
    pic.style.visibility = 'hidden';
}

function on_dragEnter(e){
    e.preventDefault();
    leftbox.style.background='SkyBlue';
    leftbox.style.border='3px solid red';
}

function on_dragLeave(e){
    e.preventDefault();
    leftbox.style.background='White';
    leftbox.style.border='3px solid blue';
}

function on_drop(e){
    e.preventDefault();
    leftbox.innerHTML = e.dataTransfer.getData( 'Text' );
}

function on_choose_language(e){
    var s = String(document.URL);
    var surl = s.split("//")[1];
    var surll = surl.split("/");
//    alert(surll);

    var lan = e.innerText;
    if ( lan == "English" ) surll[1] = "en";
    else if ( lan == "Chinese Simplifed" ) surll[1] = "zh-cn";
    else if ( lan == "France" ) surll[1] = "fr";

    var new_url = "http://";
    for(var i=0; i<surll.length; ++i){
        if( surll[i].length != 0 )
            new_url += surll[i] + "/";
    }

    window.location = new_url;
//    alert(new_url);
}

function getStuff(){
    var list = document.querySelectorAll("#menu_item");
    for(var i=0; i<list.length; ++i){
        list[i].onlick=talk;
    }
}

function initPlayer(){
    barSize=600;
    myMovie=document.getElementById('myMovie');
    playButton=document.getElementById('playButton');
    bar=document.getElementById('defaultBar');
    progressBar=document.getElementById('progressBar');

    playButton.addEventListener('click', playOrPause, false);
    bar.addEventListener('click', clickedBar, false);

}

function initCanvas(){
    var eleCanvas = document.getElementById('canvas');
    canvas = eleCanvas.getContext('2d');
//    var g = canvas.createLinearGradient( 0, 0, 100, 100 );
//    g.addColorStop( .0, "blue" );
//    g.addColorStop( .5, "green" );
//    g.addColorStop( 1, "red" );
//    canvas.fillStyle = g;
//    canvas.fillRect( 0, 0, 100, 100 );

//    canvas.beginPath();
//    canvas.moveTo( 50, 50 );
//    canvas.lineTo( 70, 250 );
//    canvas.lineTo( 300, 200);
//    canvas.closePath();
//    canvas.stroke();

//    canvas.shadowOffsetX = 4;
//    canvas.shadowOffsetY = 4;
//    canvas.shadowBlur = 6;
//    canvas.shadowColor = 'rgba(0,0,255,.5)';
//    canvas.font="bold 36px Tahoma";
//    canvas.textAligh="end";
//    canvas.fillText( "omgwtfbbq?", 300, 100 );


//    canvas.font = "bold 22px Tahoma";
//    canvas.textAlign = "start";
//    canvas.fillText("start", 10, 20);
//
//    canvas.translate( 100, 150 );
//    canvas.fillText("after translate", 0, 0);
//
//    canvas.rotate( 1 );
//    canvas.fillText("after rotate", 0, 0);
//
//    canvas.scale( 1.5, 4 );
//    canvas.fillText("after scaling", 0, 20);

}

function initDragAndDrop(){
    window.addEventListener("mousemove", on_mousemove, false );

    mypic = document.getElementById('facepic');
    mypic.addEventListener('dragstart', on_dragStart, false);
    mypic.addEventListener('dragend', on_dragEnd, false);
    leftbox = document.getElementById('leftbox');
    leftbox.addEventListener('dragenter',on_dragEnter, false);
    leftbox.addEventListener( 'dragleave', on_dragLeave, false );
    leftbox.addEventListener( 'dragover', function(e){e.preventDefault();}, false );
    leftbox.addEventListener( 'drop', on_drop, false );
}

function initSavingData(){
    var button = document.getElementById("button");
    button.addEventListener( 'click', on_clickButton, false );
}

function on_clickButton(e){
    var one = document.getElementById("one").value;
    var two = document.getElementById("two").value;
    sessionStorage.setItem(one, two);

    display();

    document.getElementById("one").value = "";
    document.getElementById("two").value = "";
}
function display(){
    var rightbox2 = document.getElementById("rightbox2");
    rightbox2.innerHTML = "";

    for(var x=0; x<sessionStorage.length; x++){
        var a = sessionStorage.key(x);
        var b = sessionStorage.getItem(a);
        rightbox2.innerHTML += a + " - " + "<br />";
    }
}

function playOrPause(){
    if(!myMovie.paused && !myMovie.ended){
        myMovie.pause();
        playButton.innerHTML='Play';
        window.clearInterval(updateBar);
    }else{
        myMovie.play();
        playButton.innerHTML='Pause';
        updateBar=setInterval(update, 500);
    }
}

function update(){
    if( !myMovie.ended ){
        var size = parseInt(myMovie.currentTime*barSize/myMovie.duration)
        progressBar.style.width=size+'px';
    }else{
        progressBar.style.width='0px';
        playButton.innerHTML='Play';
        window.clearInterval(updateBar);
    }
}

function clickedBar(e){
    if(!myMovie.paused && !myMovie.ended){
        var mouseX= e.pageX-bar.offsetLeft;
        var newtime = mouseX*myMovie.duration/barSize;
        myMovie.currentTime=newtime;
        progressBar.style.width=mouseX+'X';
    }
}

function showDate(id)
{
    document.getElementById(id).innerHTML = Date();
}

function talk(){
    alert("hi there!");
}

function on_mouseover_arrow(e){
    footer_arrow.style.bottom = "-20px";
    footer_arrow.style.background = "rgba(0,0,0,0.5)";

    footer.style.bottom = "0px";
    footer.style.background = "rgba(0,0,0,0.7)";

}

function on_mouseleave_footer(e){

    footer_arrow.style.bottom = "0px";
    footer_arrow.style.background = "rgba(0,0,0,0.25)";

    footer.style.bottom = "-40px";
}




