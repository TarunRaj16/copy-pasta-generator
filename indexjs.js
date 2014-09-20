

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
	 
function sendToServer(arrayPar) {

  if ("WebSocket" in window)
  {
     alert("WebSocket is supported by your Browser!");
     // Let us open a web socket
     var ws = new WebSocket("ws://localhost:3001/");
     ws.onopen = function()
     {
        // Web Socket is connected, send data using send()
        ws.send(arrayPar);
        alert("Message is sent...");
     };
     ws.onmessage = function (evt) 
     { 
        var received_msg = evt.data;
        alert("Message is received...");
     };
     ws.onclose = function()
     { 
        // websocket is closed.
        alert("Connection is closed..."); 
     };
  }
  else
  {
     // The browser doesn't support WebSocket
     alert("WebSocket NOT supported by your Browser!");
  }
  
  
	 document.getElementById("oldThemes").style.backgroundColor='white';
	 document.getElementById("newThemes").style.backgroundColor='white';

}

