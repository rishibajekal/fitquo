$(document).ready(function() {
    $.getJSON('/api/recommend', function(data){
        $.each(data, function(index){
            var trainer = data[index];
            $('#trainers').append("<h4>" + (index + 1) + ".) </h4><h4><large class='lead' id='name'>" + trainer["trainer_name"] +
                "</large></h4><h5><large class='lead' id='email'>" + trainer["trainer_email"] + "</large></h5><hr>");
        });
    });
});
