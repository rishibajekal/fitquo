$(document).ready(function() {
    $.getJSON('/api/feed', function(data){
        $.each(data, function(index){
            var question = data[index];
            $('#questions').append("<p><h4>Q:</h4> <h4><a href='/api/question/" +
                question["question_id"] + "'><large class='lead' id ='name'>" +
                question["content"] + "</large></a></h4>");
        });
    });
});