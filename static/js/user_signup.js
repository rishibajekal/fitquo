$(document).ready(function() {

  validate_number("age");
  validate_number("weight");

  $('#signup-button').click(function(event) {
    if (is_valid_form()) {
      $('#database-error').addClass('hidden');
      $('#invalid-form').addClass('hidden');
      signup(event);
    }
    else {
      $('#invalid-form').removeClass('hidden');
    }
  });
});

function signup(event) {
  var user_age = $('#age').val();
  var user_weight = $('#weight').val();
  var user_height_feet = $('#height-feet').val();
  var user_height_inches = $('#height-inches').val();
  var interests = [];
  var i =0;
  if($("#aerobic").is(':checked')){
    interests[i] = "Aerobics";
    i+=1;
  }
  if($("#body").is(':checked')){
    interests[i] = "BodyBuilding";
    i+=1;
  }
  if($("#cardio").is(':checked')){
    interests[i] = "Cardio";
    i+=1;
  }
  if($("#diet").is(':checked')){
    interests[i] = "Diet and Nutrition";
   i+=1;
  }
  if($("#weight").is(':checked')){
    interests[i] = "Weight Loss";
       i+=1;
  }
  if($("#kick").is(':checked')){
    interests[i] = "Kickboxing";
       i+=1;
  }
  if($("#plyo").is(':checked')){
    interests[i] = "Plyometrics";
       i+=1;
  }
  if($("#rehab").is(':checked')){
    interests[i] = "Rehabilitation";
       i+=1;
  }
  if($("#yoga").is(':checked')){
    interests[i] = "Yoga";
  }

  var post_data = {
    "user": {
      "age": parseInt(user_age, 10),
      "weight": parseInt(user_weight, 10),
      "height": 12 * parseInt(user_height_feet, 10) + parseInt(user_height_inches, 10),
      "interests": interests
    },
    "_xsrf": getCookie("_xsrf")
  };

  $.ajax({
    url: '/api/user_signup',
    type: 'POST',
    contentType: 'application/json',
    dataType: 'json',
    data: JSON.stringify(post_data),
    success: function(data) {
      if (data.success === "true") {
        window.location.replace("/profile");
      }
      else {
        $('#database-error').removeClass('hidden');
      }
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

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
