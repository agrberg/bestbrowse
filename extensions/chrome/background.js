chrome.history.onVisited.addListener(function(result) {
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
