$(document).ready(function() {
    $.getJSON('/api/feed', function(data){
        $.each(data, function(index){
            var question = data[index];
            $('#questions').prepend("<p><h4>Question:</h4> <h4><a href='answers/" +
                question["question_id"] + "'><large class='lead' id ='name'>" +
                question["content"] + "</large></a></h4>");
        });
    });
});
