function signup(event){
  var user_email = $('#email').val();
  var user_age = $('#age').val();
  var user_height = $('#height').val();
  var user_weight = $('#weight').val();

  var new_user = '{"email": "' + user_email +
                '", "age": "' + user_age +
                '", "weight": "' + user_weight +
                '","height": "' + user_height + '"}';
  $.ajax({
        url: '/api/signup',
        dataType: 'json',
        type: 'POST',
        data: new_user,
        success: function(data) {
            window.location.replace("/profile");
        }
    });
}


$('#signup-button').bind('click', function(event) {
    signup(event);
});