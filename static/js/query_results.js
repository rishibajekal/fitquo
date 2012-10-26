$(document).ready(function(){
  $.getJSON('/api/search', function(data) {
    $.each(data, function(email, name) {
      $('#query-results').append('<li>' + 'username:' + name + 'email:' + email + '</li>');
    });
  });
});