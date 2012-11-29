$(document).ready(function() {
    var question_id = $("#question_id").html();
    $.getJSON('/api/question/' + question_id, function(data) {
      $('#question').append(data[0]["content"]);
      if (data[1].length > 0) {
        for (var i = 0; i < data.length; i++) {
          $('#answers').append(data[1][i]["content"]);
        }
      }
    });
});
