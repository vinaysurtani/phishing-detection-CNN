// Purpose - This file contains all the logic relevant to the extension such as getting the URL, calling the server
// side clientServer.php which then calls the core logic.

const transfer=()=>{	
	var tablink;
	chrome.tabs.getSelected(null,function(tab) {
	   	tablink = tab.url;
		$("#p1").text("The URL being tested is - "+tablink);

		//var xhr=new XMLHttpRequest();
		params="url="+tablink;
        // alert(params);
		var markup = "url="+tablink+"&html="+document.documentElement.innerHTML;
		fetch("http://localhost:8080/Malicious-Web-Content-Detection-Using-Machine-Learning-master/clientServer.php", {
			method: 'POST',
			headers: new Headers({
			  "Content-Type": "application/x-www-form-urlencoded \r\n",
			}),
			body: markup,
		  })
		.then((response)=>{
			console.log(response.clone().text())
			return response.text()})
		.then((data)=>{
			console.log(data)
			$("#div1").text(data.split(" ").pop())
			return data.split(" ").pop();
		  });
	});
}


$(document).ready(function(){
    $("button").click(function(){	
		var val = transfer();
    });
});

chrome.tabs.getSelected(null,function(tab) {
   	var tablink = tab.url;
	$("#p1").text("The URL being tested is - "+tablink);
});
