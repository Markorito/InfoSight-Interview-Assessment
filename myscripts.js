$(function(){
  $('#submitUpload').on('click', function(){
      var file = document.getElementById("drop-zone__input").files[0];
      var form = new FormData();
      form.append("file", file);
  
      var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://127.0.0.1/",
        "method": "POST",
        "processData": false,
        "contentType": false,
        "mimeType": "multipart/form-data",
        "data": form
      };
  
      $.ajax(settings).done(function (response) {
        console.log(response);
      });
    });
  });