function loadAPIClientInterfaces() {
  gapi.client.load('youtube', 'v3', function() {
    handleAPILoaded();
  });
}

// Search for a given string.
function search() {
  var q = $('#query').val();
  console.log(q);
  var request = gapi.client.youtube.search.list({
    q: q,
    part: 'snippet'
  });

  request.execute(function(response) {
    console.log(response);
    var str = JSON.stringify(response.result);
    console.log(str);
    $('#search-container').html('<pre>' + str + '</pre>');
  });
}