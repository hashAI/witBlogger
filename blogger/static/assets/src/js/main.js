$(".btn-delete-blog").click(function(e){
    $("#alert-modal").modal("show");
    $("#btn-delete").data("blog_id", $(this).attr('content'));
})

$("#btn-delete").click(function(e){
   var blog_id = $(this).data("blog_id");
   var formdata = new FormData();
   formdata.append("blog_id", blog_id);
   $.ajax({
        type: "POST",
        url: "/blog/delete/",
        data: formdata,
        dataType: "json",
        processData: false,
        contentType: false,
    }).done(function(data){
        console.log("success", data);
        $("#alert-modal").modal('hide');
        window.location.href = data.redirect_url;
    })
    .fail(function(data){
        console.log("failure", data);
        $("#alert-modal").modal('hide');
    })
})

