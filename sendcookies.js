//Only needed for testing with node//
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
//---------------------------------//

var testcookie="test"
var xhttp = new XMLHttpRequest();
var url = "http://127.0.0.1:1234";

xhttp.open('GET', url,  true);
xhttp.withCredentials = true;
xhttp.setRequestHeader('session', testcookie);
xhttp.send();

xhttp.onreadystatechange = function () {
   if (xhttp.readyState === 4) {
         console.log(xhttp.status);
 }};

