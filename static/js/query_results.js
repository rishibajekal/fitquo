$(document).ready(function(){
  $.getJSON('ajax/search', function(data) {
    $.each(data, function(email, name) {
      $('#query-results').push('<li>' + 'username:' name + 'email:' + email + '</li>');
    });
  });
});