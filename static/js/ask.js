$(document).ready(function() {

  $('#question-button').click(function(event) {
    if (is_valid_form()) {
      $('#invalid-form').addClass('hidden');
      sendquestion(event);
    }
    else {
      $('#invalid-form').removeClass('hidden');
    }
  });
});

function sendquestion(event) {
  var content = $('#question').val();
  var timestamp = new Date().toISOString();
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

  var new_question = {
    "question": {
      "content": content,
      "timestamp": timestamp,
      "interests": interests
    },
    "_xsrf": getCookie("_xsrf")
  };

  $.ajax({
    url: '/api/ask',
    type: 'POST',
    contentType: 'application/json',
    dataType: 'json',
    data: JSON.stringify(new_question),
    success: function(data) {
      if (data.success == "true") {
        window.location.replace("/feed");
      }
      else {
        $('#dont-spam').removeClass('hidden');
      }
    }
  });
}

function is_valid_form() {
  var value = $("#question").val();
  return value.length !== 0 && value.length < 1000 && value !== " ";
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
