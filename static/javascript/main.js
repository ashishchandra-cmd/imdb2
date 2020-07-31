$(function() {
             $('#id_search').keyup(function(){
                $.ajax({
                          url:'http://127.0.0.1:8000/search_title/',
                          type:'POST',
                          data:{ 'search_title':$('#id_search').val()

                              },
                          success:searchSucess,
                          dataType:'html'
                          ,
                          failure: function(){
                             alert('not ok');
                          },
                });

             });
         });

function searchSucess(data) {
    $('#id_search_result').html(data);

}