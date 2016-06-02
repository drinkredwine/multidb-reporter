var rootURL = "query";

function drawChart(data){

}

function doQuery(query) {
    console.log('doQuery');
    $.ajax({
        type: 'POST',
        "crossDomain": true,
        contentType: 'application/json',
        url: rootURL,
        dataType: "json",
        data: queryToJSON(query),
        success: function(data) {
            console.log(' success: ' + data);
            drawChart(data);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log('failed');
        }
    });
};


function queryToJSON(query) {
    return JSON.stringify({
        "queryType": "SQL",
        "query": query
    });
};
