$(document).ready(function(){
  $.get('/api/user', function(data){
    $('#email').append(data['user_email']);
    $('#name').append(data['user_name']);
    $('#age').append(data['age']);
    $('#weight').append(data['weight']);
    $('#height').append(data['height']);
  });

  $('#search-bar').keypress(function(event){
   if (event.keyCode == 13)
   {
       event.preventDefault();
       search(event);
   }
   });
});


function search(event){
    var query = $('#search-bar').val();
    query = '{"query": "' + query + '"}'
    $('#search-bar').replaceWith('<input id="search-bar" class="input-xxlarge" type="text" placeholder="search"></input>');
    $.ajax({
    url: '/api/search',
    dataType: 'json',
    type: 'GET',
    data: query,
    success: function(data) {
      window.location.replace("query_results.html");
    }
  });
}
