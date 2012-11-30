$(document).ready(function() {
    var question_id = $("#question_id").html();
    $.getJSON('/api/question/' + question_id, function(data) {
      $('#question').append(data[0]["content"]);
      if (data[1].length > 0) {
        for (var i = 0; i < data[1].length; i++) {
          console.log(data[1][i]);
          $('#answers').append("<h3 id='answer" + (i+1) + "'>" + data[1][i]["content"] + "</h3>");
        }
      }
    });

    $('#answer-btn').click(function(event) {
      if (is_valid_form()) {
        $('#invalid-form').addClass('hidden');
        sendanswer(question_id);
      }
      else {
        $('#invalid-form').removeClass('hidden');
      }
    });

});

function sendanswer(question_id) {
  var content = $('#new_answer').val();
  var timestamp = new Date().toISOString();

  var new_question = {
    "answer": {
      "content": content,
      "timestamp": timestamp,
      "question_id": question_id
    },
    "_xsrf": getCookie("_xsrf")
  };

  $.ajax({
    url: '/api/answer',
    type: 'POST',
    contentType: 'application/json',
    dataType: 'json',
    data: JSON.stringify(new_question),
    success: function(data) {
      window.location.reload();
    }
  });
}

function is_valid_form() {
  var value = $("#new_answer").val();
  return value.length !== 0 && value.length < 1000 && value !== " ";
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
