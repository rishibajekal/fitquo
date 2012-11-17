$(document).ready(function(){
  $.get('/api/user', function(data){
    $('#email').append(data['user_email']);
    $('#name').append(data['user_name']);
    $('#age').append(data['age']);
    $('#weight').append(data['weight'] + " lbs");
    var feet = Math.floor(data['height'] / 12);
    var inches = data['height'] % 12;
    $('#height').append(feet + " feet, " + inches + " inches");
  });
});
