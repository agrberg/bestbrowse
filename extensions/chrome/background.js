chrome.history.onVisited.addListener(function(result) {
	var reqToSend = new XMLHttpRequest(),
	reqToGet = new XMLHttpRequest(),
	fd = new FormData(),
    opt = {};

	fd.append('url', result.url);
	fd.append('visit_at', result.lastVisitTime);
	fd.append('title', result.title);
	fd.append('visit_count', result.visitCount);

	chrome.identity.getProfileUserInfo(function (userInfo) {
	  fd.append('browser_id', userInfo.id);
	  fd.append('browser_type', "chrome");
	});

	reqToSend.open("POST", "http://10.104.92.195:3000/visits", true);
    reqToSend.send(fd);
	
	reqToGet.onload = reqListener;
	reqToGet.open("GET", "http://10.104.92.195:3000/recommendation", true);
    reqToGet.send();	
});
	
function reqListener () {
  if (this.responseText != ""){
    opt = {
      iconUrl: 'icon.jpg',
      type: 'list',
      title: 'A wild recommendation has appeared!',
      message: 'Primary message to display',
      priority: 1,
      items: [{ title: 'Check out your recco', message: ''}]
	};
    chrome.notifications.create('notify1', opt, function(id) {});
    chrome.notifications.onClicked.addListener(function (notification){
      var properties = {
        url:this.responseText
      };
      chrome.tabs.create(properties, function (tab) {}); 
    }); 
    console.log(this.responseText);
  }
}	
