$("form#skyForm").submit(function(event){
  event.preventDefault();
  var json = $(this).serializeJSON();
  $.ajax({
    type: "POST",
    contentType: 'application/json;charset=UTF-8',
    url: "http://localhost:5000/form",
    data: json,
    success: function(response){
      if (response){
        alert('Success');
      }else{
        aler('Failed');
      }
    }
  });
  console.log(json);
});

$('#addBtn').on('click',function(){

  $('#formTable tr:last').after('<tr><td><input class="form-control" type="text" name="people[][firstname]" value="" placeholder="Please enter First Name"/></td><td><input class="form-control" type="text" name="people[][surname]" value="" placeholder="Please enter Surname"/></td></tr>');

});
