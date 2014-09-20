

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
var websocket;

function init() { 

testWebSocket(); 

}  

function testWebSocket() { 

websocket = new WebSocket(wsUri); 
websocket.onopen = function(evt) { onOpen(evt) }; 
websocket.onclose = function(evt) { onClose(evt) };
websocket.onmessage = function(evt) { onMessage(evt) }; 
websocket.onerror = function(evt) { onError(evt) }; 
 
}  
 
 function onOpen(evt) { 
alert("CONNECTED"); 
 sendToServer("WebSocket rocks"); } 

 function onClose(evt) { 
 alert("DISCONNECTED"); }  
 
 function onMessage(evt) { 
 
 alert('<span style="color: blue;">RESPONSE: ' + evt.data+'</span>'); 
 websocket.close(); 
 }  
 
 function onError(evt) { alert('<span style="color: red;">ERROR:</span> ' + evt.data); }  
 
 function sendToServer(message) { writeToScreen("SENT: " + message);  websocket.send(message); }  
 


	 

