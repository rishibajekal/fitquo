$(document).ready(function() {
  $('#search-button').click(function(event) {
    if (is_valid_form()) {
      $('#invalid-form').addClass('hidden');
      $("#search-results").empty();
      sendsearch(event);
      var position = $("#search-results").position();
      scroll(0, position.top);
    }
    else {
      $('#invalid-form').removeClass('hidden');
    }
  });
});

function sendsearch(event) {
  var content = $('#search').val();
  var timestamp = new Date().toISOString();
  var topics = ["#aerobics", "#bodybuilding", "#cardio", "#diet", "#weightloss", "#kick", "#plyo", "#rehab", "#yoga"];
  var topic_name = ["Aerobics", "Bodybuilding", "Cardio", "Diet and Nutrition", "Weight Loss", "Kickboxing", "Plyometrics", "Rehabilitation", "Yoga"];
  var interests = [];
  var advanced = "no";
  var j = 0;
  for(var i=0; i < topics.length; i++)
  {
    if($(topics[i]).is(':checked'))
    {
      interests[j] = topic_name[i];
      j+=1;
    }
  }

  if($("#advanced").is(':checked'))
  {
    advanced = "yes";
  }

  var new_search = {
    "search": {
      "content": content,
      "timestamp": timestamp,
      "interests": interests,
      "advanced": advanced
    },
    "_xsrf": getCookie("_xsrf")
  };

  $.ajax({
    url: '/api/search',
    type: 'POST',
    contentType: 'application/json',
    dataType: 'json',
    data: JSON.stringify(new_search),
    success: function(data) {
      for(var i=0; i < data.length; i++)
      {
        var result = data[i];
        $("#search-results").append("<p><h4><a href='answers/" +
                result["id"] + "'><large class='lead' id ='name'>" +
                result["content"] + "</large></a></h4><hr>");
      }
      $("#search-results").prepend("<p><h2>Search Results:</h2></p>");
    }
  });
}

function is_valid_form() {
  var value = $("#search").val();
  return value.length !== 0 && value.length < 1000 && value !== " ";
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
