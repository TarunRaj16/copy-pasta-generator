

function send(){

	 
	 var oldThemeUnsplit = document.getElementById("oldThemes").value;
	 var oldThemeArray = oldThemeUnsplit.split(" ");
	 
	 var newThemeUnsplit = document.getElementById("newThemes").value;
	 var newThemeArray = newThemeUnsplit.split(" ");
	 
	 document.getElementById("oldThemes").style.backgroundColor='green';
	 document.getElementById("newThemes").style.backgroundColor='green';

	 var togetherArray = [oldThemeArray,newThemeArray];
	 var jsonstring = JSON.stringify(togetherArray);
	 alert("JSON STRING: " + jsonstring);
	 sendToServer(jsonstring);
	 
	 
	 }
	 

var wsUri = "ws://localhost:3001/"; 
var output;  

function init() { 

	ws = new WebSocket(ws://localhost:3001/); 

	if("WebSocket" in window) {
            ws.onopen = function (event) {
					onOpen(event);
            }

            ws.onmessage = function (message) {
                onMessage(message);    
            }
        }
 
}  
 
 function onOpen(evt) { 
	alert("CONNECTED"); 
 } 
 
 function onMessage(evt) { 
	alert("Receiving Message"); 
 }  
  
 function sendToServer(message) { 
 
	alert("Sending Message");
	ws.send(message); 
 
 }  
 


	 

