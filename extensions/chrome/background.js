chrome.notifications.onClicked.addListener(function(notificationId) {
  chrome.notifications.clear(notificationId, function(success){});

  chrome.tabs.create({ url: lastRecommendation }, function(tab){});

  console.log('notification click listener', arguments);
});

var recNoteId = '',
    opt = {
      type: 'basic',
      iconUrl: 'icon.jpg',
      title: 'A wild recommendation has appeared!',
      message: 'You got a recommendation. Click me brah!',
      isClickable: true
    },
    reqListener,
    lastRecommendation;

reqListener = function() {
  if (this.responseText != '') {
    lastRecommendation = this.responseText;

    chrome.notifications.clear(recNoteId, function(){});
    chrome.notifications.create(recNoteId, opt, function(notificationId) {
      recNoteId = notificationId;
    });
  }
}

chrome.history.onVisited.addListener(function(result) {
	var reqToSend = new XMLHttpRequest(),
	    reqToGet = new XMLHttpRequest(),
	    fd = new FormData();

	fd.append('url', result.url);
	fd.append('visit_at', result.lastVisitTime);
	fd.append('title', result.title);
	fd.append('visit_count', result.visitCount);

	chrome.identity.getProfileUserInfo(function (userInfo) {
	  fd.append('browser_id', userInfo.id);
	  fd.append('browser_type', "chrome");
    reqToSend.open("POST", "http://10.104.92.195:3000/visits", true);
    reqToSend.send(fd);
	});

	reqToGet.onload = reqListener;
	reqToGet.open("GET", "http://10.104.92.195:3000/recommendation", true);
  reqToGet.send();
});

chrome.runtime.onInstalled.addListener(function(details) {
  if (details.reason == "install") {
    console.log("This is a first install!");
    chrome.history.search({text: "", maxResults: 2147483647}, function(historyItems) {
      var urlSet = {},
          uniqueUrls;

      for (var i = 0; i < historyItems.length; i++) {
        urlSet[historyItems[i].url] = true;
      }

      uniqueUrls = Object.keys(urlSet);

      for (var j = 0; j < uniqueUrls.length; j++) {
        (function(url) {
          chrome.history.getVisits({url: url}, function(visitItems) {
            for (var i = 0; i < visitItems.length; i++) {
              (function(visitTime) {
                var req = new XMLHttpRequest(),
                    fd = new FormData();

                fd.append('url', url);
                fd.append('visit_at', visitTime);

                chrome.identity.getProfileUserInfo(function(userInfo) {
                  fd.append('browser_id', userInfo.id);
                  fd.append('browser_type', "chrome");

                  req.open("POST", "http://10.104.92.195:3000/visits", true);
                  req.send(fd);
                });
              })(visitItems[i].visitTime);

            }
          });
        })(uniqueUrls[j]);
      }
    });
  }
});
