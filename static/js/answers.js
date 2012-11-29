$(document).ready(function() {
    var question_id = $("#question_id").html();
    $.getJSON('/api/question/' + question_id, function(data) {
      console.log(data[0]);
      $('#question').append(data[0]["content"]);
      for (var i = 0; i < data.length; i++) {
        $('#answers').append(data[1][i]["content"]);
      }
    });
});
