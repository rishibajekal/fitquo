$(document).ready(function() {
    $.getJSON('/api/feed', function(data){
        $.each(data, function(index){
            var question = data[index];
            $('#questions').prepend("<div><h4><a href='answers/" +
                question["question_id"] + "'><large class='lead' id ='name'>" +
                question["content"] + "</large></a></h4><h4 class='pull-right'>"  + question["author"] + "</h4>posted <time class='timeago muted' datetime=" + question['posted_at' ]+
        "></time></div><hr>");
            $("time.timeago").timeago();
        });
    });
});
