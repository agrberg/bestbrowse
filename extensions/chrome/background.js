chrome.history.onVisited.addListener(function(result) {
    console.log("URL:  " + result.url);
    console.log("Title:  " + result.title);
    console.log("Last visit time:  " + result.lastVisitTime);
    console.log("Visit count:  " + result.visitCount);
}); 
