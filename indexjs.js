

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
	 
	 
function startServerConnection() {

	if("WebSocket" in window) {
	
	
		alert("Connecting to Server");
		var ws = new WebSocket("ws://localhost:3001/");
		
	ws.onmessage = function (evt) 
     { 
        var received_msg = evt.data;
        alert("Message is received...");
     };

	} else {
	
	alert("WebSockets is not supported");
	
	}


}

function sendToServer(arrayPar){

	if("WebSocket" in window) {
	
		var ws = new WebSocket("ws://localhost:3001/");
		ws.send(arrayPar);
        alert("Message is sent...");
		
	} else {
	
	alert("WebSockets is not supported");
	
	}

}

	 

