$(document).ready(function(){
  $.get('/api/user', function(data){
    $('#email').append(data['user_email']);
    $('#name').append(data['user_name']);
    $('#age').append(data['age']);
    $('#weight').append(data['weight']);
    $('#height').append(data['height']);
  });

  // REMOVE ME FOR REAL CODE (USE SOME FOR LOGOUT)
  $('#delete-profile').click(function(event) {
    $.get('/api/delete', function(data){
      window.location.replace("/");
    });
  });

});