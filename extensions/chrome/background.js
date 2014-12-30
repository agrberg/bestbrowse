chrome.history.onVisited.addListener(function(result) {

	var req = new XMLHttpRequest();
	var fd = new FormData();
 
	fd.append('url', result.url);
	fd.append('visit_at', result.lastVisitTime);
	fd.append('title', result.title);
	fd.append('visit_count', result.visitCount);
 
	req.open("POST", "http://10.104.92.195:3000/visits", true);
	req.send(fd);



    console.log("ID:  " + result.id);
    console.log("URL:  " + result.url);
    console.log("Title:  " + result.title);
    console.log("Last visit time:  " + result.lastVisitTime);
    console.log("Visit count:  " + result.visitCount);
    console.log("Typed count:  " + result.typedCount);

    chrome.history.getVisits({url: result.url}, function(visitItems) {
        console.log("Number of visits to this URL:  " + visitItems.length);
        console.log("Listing visits to this URL:");
        var index;
        for (index = 0; index < visitItems.length; index ++) {
            visit = visitItems[index]
            console.log("");
            console.log("URL ID:  " + visit.id);
            console.log("Visit ID:  " + visit.visitId);
            console.log("Visit time:  " + visit.visitTime);
            console.log("Referring visit ID:  " + visit.referringVisitId);
            console.log("Transition:  " + visit.transition);
        }
    });
});
