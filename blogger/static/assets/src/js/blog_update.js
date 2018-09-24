var Delta = Quill.import('delta');
 var quill = new Quill('#editor-container', {
     modules: {
       syntax: true,
       toolbar: '#toolbar-container'
     },
     placeholder: 'Compose an epic...',
     theme: 'snow'
   });
// Store accumulated changes
 var change = new Delta();
 quill.on('text-change', function(delta) {
   change = change.compose(delta);
 });

 // Save periodically
 setInterval(function() {
   if (change.length() > 0) {
     console.log('Saving changes', change);
     /*
     Send partial changes
     $.post('/your-endpoint', {
       partial: JSON.stringify(change)
     });

     Send entire document
     $.post('/your-endpoint', {
       doc: JSON.stringify(quill.getContents())
     });
     */
     change = new Delta();
   }
 }, 5*1000);

 // Check for unsaved data
 window.onbeforeunload = function() {
   if (change.length() > 0) {
     return 'There are unsaved changes. Are you sure you want to leave?';
   }
 }

$("#btn-update-blog").click(function(e){
    $("#alert-modal").modal("show");
    $("#btn-update").data("blog_id", $(this).attr("content"));
})

$("#btn-update").click(function(e){
    var blog_id = $(this).data("blog_id");
    content = quill.root.innerHTML;
    console.log(content);
    var formdata = new FormData($(".modal-body .container form")[0])
    formdata.append('content', content);
    console.log(formdata);
    $.ajax({
        type: "POST",
        url: "/blog/edit/"+blog_id,
        data: formdata,
        dataType: "json",
        processData: false,
        contentType: false,
    }).done(function(data){
        console.log("success", data);
        $("#publish-modal").modal('hide');
        window.location.href = data.redirect_url;
    })
    .fail(function(data){
        console.log("failure", data);
        $("#publish-modal").modal('hide');
    })
})

