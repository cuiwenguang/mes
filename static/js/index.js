$(function () {
    $('#sideMenu li').click(function () {
        $('#sideMenu li').removeClass("active");
        $(this).addClass("active")
        var url =$(this.firstElementChild).attr('href').slice(1);
        $.get(url, function (data) {
            $(".side-body").html(data);
            var script = document.createElement("script");
            script.type = "text/javascript";
            script.src = "/static/js/page/"+url+".js";
            document.getElementsByTagName("body")[0].appendChild(script)
        });
    })
})

