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
  var topics = ["#aerobics", "#bodybuilding", "#cardio", "#diet", "#weightloss", "#kick", "#plyo", "#rehab", "#yoga"];
  var topic_name = ["Aerobics", "Bodybuilding", "Cardio", "Diet and Nutrition", "Weight Loss", "Kickboxing", "Plyometrics", "Rehabilitation", "Yoga"];
  var interests = [];
  var j = 0;
  for(var i=0; i < topics.length; i++)
  {
    if($(topics[i]).is(':checked'))
    {
      interests[j] = topic_name[i];
      j+=1;
    }
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
