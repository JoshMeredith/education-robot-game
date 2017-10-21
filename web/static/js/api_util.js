// We handle both updates in the one function so we only need to
// make one API call. codename is required, other arguments may be undefined.
// Asynchronous, doesn't return.
function updateBestScore(codename, codeScore, executionScore) {
    var req = new XMLHttpRequest();

    req.open("POST", "/update_score");
    req.setRequestHeader("Content-Type", "application/json");

    var data = {
        'codename': codename,
        'code_score': codeScore,
        'execution_score': executionScore
    };

    req.onreadystatechange = function() {
        if (req.readyState === 4) {
            if (req.status !== 200) {
                // console.log("Request failed with status " + req.status);
                return;
            }
            var response = JSON.parse(req.responseText);
            // console.log(response);
        }
    };
    req.send(JSON.stringify(data));
}
