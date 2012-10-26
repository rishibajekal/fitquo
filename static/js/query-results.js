$(document).ready(function(){
  $.getJSON('/api/search', function(data) {
    $.each(data, function(id, name) {
      $('#query-results').append('<li>' + 'username:' + id + 'email:' + name + '</li>');
    });
  });
});