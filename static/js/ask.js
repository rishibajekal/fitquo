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

  var new_question = {
    "question": {
      "content": content,
      "timestamp": timestamp
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
      window.location.replace("/feed");
    }
  });
}

function is_valid_form() {
  return $("#question").val().length !== 0 && $("#question").val().length < 250 && $("#question").val() !== " ";
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
