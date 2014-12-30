chrome.history.onVisited.addListener(function(result) {
  // Post data to server
	var req = new XMLHttpRequest();
	var fd = new FormData();

	fd.append('url', result.url);
	fd.append('visit_at', result.lastVisitTime);
	fd.append('title', result.title);
	fd.append('visit_count', result.visitCount);

	chrome.identity.getProfileUserInfo(function (userInfo) {
	  fd.append('browser_id', userInfo.id);
	  fd.append('browser_type', "chrome");
	  req.open("POST", "http://10.104.92.195:3000/visits", true);
      req.send(fd);
	});

	var opt = {
	  iconUrl: 'https://prchecker-innovalist.netdna-ssl.com/wp-content/uploads/2013/06/using-social-media-to-increase-website-traffic-image.png',
	  type: 'list',
	  title: 'Hi User!',
	  message: 'Primary message to display',
	  priority: 1,
	  items: [{ title: 'for redirection click here', message: ''}]
};

chrome.notifications.create('notify1', opt, function(id) { console.log("Last error:", chrome.runtime.lastError); });
});
