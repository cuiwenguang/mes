$(function () {
    $('#sideMenu li').click(function () {
        $('#sideMenu li').removeClass("active");
        $(this).addClass("active")
        var url =$(this.firstElementChild).attr('href').slice(1);
        $.get(url, function (data) {
            $(".side-body").html(data);
        })
    })
})

function loadScript(url, callback) {
    var script = document.createElement("script");
    script.type = "text/javascript";
    script.onload = function () {
        callback();
    }
    script.src = url;
    document.getElementsByTagName("body").appendChild(script)
}

$("#configForm").bootstrapValidator({
    message: "无效的值",
    feedbackIcons: {/*input状态样式图片*/
             valid: 'glyphicon glyphicon-ok',
             invalid: 'glyphicon glyphicon-remove',
             validating: 'glyphicon glyphicon-refresh'
         },
    fields:{
        sg_price: {
            message: "收购价格必须是非空的数字",
            validators: {
                notEmpty: {
                    message: "收购价格不能为空"
                },
                number: {
                    message: "收购价格必须是数字"
                },

            }
        }
    }
});