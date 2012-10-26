$(document).ready(function() {

  validate_number("age");
  validate_number("weight");

  $('#signup-button').click(function(event) {
    if (is_valid_form()) {
      $('#invalid-form').addClass('hidden');
      signup(event);
    }
    else {
      $('#invalid-form').removeClass('hidden');
    }
  });
});

function signup(event) {
  var user_age = parseInt($('#age').val(), 10);
  var user_weight = parseInt($('#weight').val(), 10);
  var user_height = (12 * parseInt($('#height-feet').val(), 10)) + parseInt($('#height-inches').val(), 10);


  var new_user = '{"age": ' + user_age +
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
  var age = "age";
  var weight = "weight";
  var is_valid = !($("#"+age+"-group").hasClass("error") ||
                   $("#"+weight+"-group").hasClass("error")) &&
                   $("#"+age).val().length !== 0 &&
                   $("#"+weight).val().length !== 0;
  return is_valid;
}

function validate_number(id) {
  $("#"+id).keyup(function(){
    if($("#"+id).val() !== "" && is_number($("#"+id).val())){
      $("#"+id+"-group").removeClass("error");
      $("#"+id+"-group").addClass("success");
      $("#"+id+"-help").addClass("hidden");
    } else{
      $("#"+id+"-group").removeClass("success");
      $("#"+id+"-group").addClass("error");
      $("#"+id+"-help").removeClass("hidden");
    }
  });
}

function is_number(number) {
  var regex = /^\d{2,3}$/;
  return regex.test(number);
}
