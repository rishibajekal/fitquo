$(document).ready(function(){
  $.get('/api/user', function(data){
    data = $.parseJSON(data);
    $('#email').append(data['email']);
    $('#name').append(data['name']);
    $('#age').append(data['age']);
    $('#weight').append(data['weight']);
    $('#height').append(data['height']);
  });
});