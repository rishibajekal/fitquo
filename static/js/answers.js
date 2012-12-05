$(document).ready(function() {
    var question_id = $("#question_id").html();
    var client_type = $("#client_type").html();

    $.getJSON('/api/question/' + question_id, function(data) {
      var question = data[0];
      var quest_html = "<div class='question'><h4><large class='lead' id='name'>" + question["content"] + "</large></h4>"+
                "<h4 class='pull-right'><span class='muted'>posted </span><time class='timeago' datetime=" +
                question['posted_at'] + "></time><span class='muted'> by </span><a href='#'>" +
                question["user_name"] + "</a></h4></div><br>";
      $('#question').append(quest_html);
      if (data[1].length > 0) {
        for (var i = 0; i < data[1].length; i++) {
          var html = "<h3 id='answer" + (i + 1) + "'>" + data[1][i]["content"];
          if (client_type === "trainer") {
            html += "<span class='pull-right close delete' id='" + data[1][i]["answer_id"] + "'>DELETE</span></h3>";
          }
          html += "<hr>";
          $('#answers').append(html);
        }
      }
      $("time.timeago").timeago();
    });

    $('.delete').live('click', function(event) {
      var id = $(this).attr('id');
      var data = {
        "id": id,
        "_xsrf": getCookie("_xsrf")
      };
      $.ajax({
        url: '/api/delete_answer',
        type: 'POST',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(data),
        success: function(data) {
          window.location.reload();
        }
      });
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
