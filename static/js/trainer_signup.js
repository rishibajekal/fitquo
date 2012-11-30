$(document).ready(function() {

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
  var gym = $('#gym').val();
  var cert = $('#cert').val();

  var topics = ["#aerobics", "#bodybuilding", "#cardio", "#diet", "#weightloss", "#kick", "#plyo", "#rehab", "#yoga"];
  var topic_name = ["Aerobics", "Bodybuilding", "Cardio", "Diet and Nutrition", "Weight Loss", "Kickboxing", "Plyometrics", "Rehabilitation", "Yoga"];
  var specialties = [];
  var j =0;
  for(var i=0; i < topics.length; i++)
  {
    if($(topics[i]).is(':checked'))
    {
      specialties[j] = topic_name[i];
      j+=1;
    }
  }

  var post_data = {
    "trainer": {
      "gym": gym,
      "certification": cert,
      "specialties": specialties
    },
    "_xsrf": getCookie("_xsrf")
  };

  $.ajax({
    url: '/api/trainer_signup',
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
  var gym = "gym";
  var cert = "cert";
  var is_valid = !($("#"+gym+"-group").hasClass("error") ||
                   $("#"+cert+"-group").hasClass("error")) &&
                   $("#"+gym).val().length !== 0 &&
                   $("#"+cert).val().length !== 0;
  return is_valid;
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
