chrome.history.onVisited.addListener(function(result) {
  // Post data to server
	var req = new XMLHttpRequest();
	var fd = new FormData();

	fd.append('url', result.url);
	fd.append('visit_at', result.lastVisitTime);
	fd.append('title', result.title);
	fd.append('visit_count', result.visitCount);

    // Log to console
    console.log('url:  ' + result.url);
    console.log('visit_at:  ' + result.lastVisitTime);
    console.log('title:  ' + result.title);
    console.log('visit_count:  ' + result.visitCount);

	chrome.identity.getProfileUserInfo(function (userInfo) {
  	fd.append('email', userInfo.email);
  	fd.append('browser_id', userInfo.id);
  	fd.append('browser_type', "chrome");
	});

	var options = {
		type: 'list',
		title: 'I like you',
		message: 'Primary message to display',
		priority: 1,
		items: [{ title: 'SarayTitle', message: 'SarayMessege'}],
		iconUrl:'http://7-themes.com/data_images/out/33/6880819-puppy-wallpaper.jpg' 
	};
	
	chrome.notifications.create("", options , function (notificationsId) {});
		
	req.open("POST", "http://10.104.92.195:3000/visits", true);
	req.send(fd);
});
