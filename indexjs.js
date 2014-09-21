
var ws = new WebSocket("ws://localhost:3001/");

function init(){ 

    $(".loader").hide();
    if("WebSocket" in window) {
        ws.onopen = function (event) {
	    onOpen(event);
        }

        ws.onmessage = function (message) {
            onMessage(message);
	    console.log(message.data);
	    var myTarget = document.getElementById("text_div");
	    myTarget.innerHTML = message.data;
	    var textBox = document.getElementById('text_box');
	    textBox.value = message.data;
	    var loading_box = document.getElementById("fancyloader");
	    $(".loader").hide();
        }
    }
    
}  

function onOpen(evt) { 
    // alert("CONNECTED"); 
} 

function onMessage(evt) { 
    // alert("Receiving Message");
    $(".loader").hide();
}  

function sendToServer(message) { 
    
    // alert("Sending Message");
    ws.send(message); 
    
}  



function send(){
    var loading_box = document.getElementById("fancyloader");
    $(".loader").show();
    var oldThemeUnsplit = document.getElementById("oldThemes").value;
    var oldThemeArray = oldThemeUnsplit.split(" ");
    
    var newThemeUnsplit = document.getElementById("newThemes").value;
    var newThemeArray = newThemeUnsplit.split(" ");
    
    document.getElementById("oldThemes").style.backgroundColor='green';
    document.getElementById("newThemes").style.backgroundColor='green';

    var togetherArray = [oldThemeArray,newThemeArray];
    var jsonstring = JSON.stringify(togetherArray);
    // alert("JSON STRING: " + jsonstring);
    sendToServer(jsonstring);
    
    
}




