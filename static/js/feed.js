$(document).ready(function() {
    $.getJSON('/api/feed', function(data){
        $.each(data, function(index){
            var question = data[index];
            $('#questions').prepend("<div class='question'><h4><a href='answers/" +
                question["question_id"] + "'><large class='lead' id='name'>" +
                question["content"] + "</large></a></h4>"+
                "<h4 class='pull-right'><span class='muted'>posted </span><time class='timeago' datetime=" +
                question['posted_at' ] + "></time><span class='muted'> by </span><a href='/profile/"+ question['user_id'] + "'>" +
                question["user_name"] + "</a></h4></div><br><hr>");
            $("time.timeago").timeago();
        });
    });
});
