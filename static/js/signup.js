$(document).ready(function() {
  validate_email("email");
  validate_number("age");
  validate_number("weight");
  $('#signup-button').click(function(event) {
    if (is_valid_form()) {
      signup(event);
    }
    else {
      alert("Please ensure the form is filled out correctly.");
    }
  });

});

function signup(event) {
  var user_email = $('#email').val();
  var user_age = parseInt($('#age').val(), 10);
  var user_weight = parseInt($('#weight').val(), 10);
  var user_height = (12 * parseInt($('#height-feet').val(), 10)) + parseInt($('#height-inches').val(), 10);


  var new_user = '{"email": "' + user_email +
                '", "age": ' + user_age +
                ', "weight": ' + user_weight +
                ',"height": ' + user_height + '}';

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

function is_valid_form() {
  var email = "email";
  var age = "age";
  var weight = "weight";
  var is_valid = !($("#"+email+"-group").hasClass("error") ||
                $("#"+age+"-group").hasClass("error") ||
                $("#"+weight+"-group").hasClass("error")) &&
              $("#"+email).val().length !== 0 &&
              $("#"+age).val().length !== 0 &&
              $("#"+weight).val().length !== 0;
  return is_valid;
}

function validate_number(id) {
  $("#"+id).keyup(function(){
    if(is_number($("#"+id).val())){
      $("#"+id+"-group").removeClass("error");
      $("#"+id+"-help").addClass("hidden");
    } else{
      $("#"+id+"-group").addClass("error");
      $("#"+id+"-help").removeClass("hidden");
    }
  });
}

function validate_email(id) {
  $("#"+id).keyup(function(){
    if(is_email($("#"+id).val())){
      $("#"+id+"-group").removeClass("error");
      $("#"+id+"-help").addClass("hidden");
    } else{
      $("#"+id+"-group").addClass("error");
      $("#"+id+"-help").removeClass("hidden");
    }
  });
}

function is_number(number) {
  var regex = /^\d{0,3}$/;
  return regex.test(number);
}

function is_email(email) {
  var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}