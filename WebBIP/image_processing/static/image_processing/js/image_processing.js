Dropzone.options.dropZoneForm = { 

   paramName: "image",
   acceptedFiles: '.png, .jpg, .jpeg, .tiff, .JPG, .JPEG',
   dictDefaultMessage: "Drag and Drop images here to upload",
   parallelUploads: 1,

  // The setting up of the dropzone
   init: function() {
      var myDropzone = this;

      this.on("complete", function(file) {
         setTimeout(() => {
            myDropzone.removeFile(file);
         }, 5000);
        
      });

      this.on("success", function(file) {

         let data = JSON.parse(file.xhr.responseText);
         
         if ($("#img_list" ).length) {
            let img_html = '<li class="list-group-item" href="#" id="' + data.name + '" data-pk="'+ data.pk +'">' + data.name + '</li>';
            $( "#img_list" ).append( img_html );
         } else {
            let img_html = '<div class="card-body p-0"><ul class="list-group rounded-0 m-0" id="img_list">'
            + '<li class="list-group-item" href="#" id="' + data.name + '" data-pk="'+ data.pk +'">' + data.name + '</li>'
            + '</ul></div>';

            $( "#card_img_list" ).html( img_html );
            $( "#original" ).html('<p class="text-center">Select an image</p>');
         }
      });
   }
 
}

function sendData(method, pk, filters={}) {
  $.ajax({
      type: 'POST',
      url: ".",
      data: { "method": method,
              "pk": pk,
              "filters": filters,
              csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()},
      beforeSend: function(){
      },
      complete:function(){
      },
      success: function (data) {
         let img_html = '<img src="' + data.img_path + "?t=" + new Date().getTime() + '" class="img-fluid" alt="">';
         $( "#" + data.id ).html( img_html );
      }
   });
}

function getFilters() {

  let filters = {
      "contrast": $("#contrast").val()/1,
      "brightness": $("#brightness").val()/1,
      "rotate90": $("#rotate90").prop('checked'),
      "rotate180": $("#rotate180").prop('checked'),
      "fliph": $("#fliph").prop('checked'),
      "flipv": $("#flipv").prop('checked'),
   }

   return filters;
}

$(document).on('click','.list-group-item',function(e) {
   e.preventDefault();
   e.stopPropagation();

   let pk = $(this).data('pk');
   let name = $(this).attr("id"); //e.target.id 

   sendData("selected", pk);

   
   sendData("processing", pk, getFilters());

   $('.active').removeClass('active');
   $(this).toggleClass('active');

});

$("#contrast").on("change", function() { 
        
   var contrast = this.value/1;
   console.log(contrast);

   if ($(".active").length){
      let pk = $(".active").data('pk');
      let name = $(".active").attr("id");

      sendData("processing", pk, getFilters());
   }      
});

$("#brightness").on("change", function() { 
        
   var brightness = this.value/1;
   console.log(brightness);

   if ($(".active").length){
      let pk = $(".active").data('pk');
      let name = $(".active").attr("id");

      sendData("processing", pk, getFilters());
   }    
});


$("#rotate90, #rotate180, #fliph, #flipv").on("click", function() { 
        
   if( $(this).data('checked') ) {
        $(this).prop('checked', false);
        $(this).data('checked', false);
    } else {
        $(this).data('checked', true);
    }

    $(':radio[name=' + this.name + ']').not(this).data('checked', false);

    if ($(".active").length){
      let pk = $(".active").data('pk');
      let name = $(".active").attr("id");

      sendData("processing", pk, getFilters());
   }
     
});







