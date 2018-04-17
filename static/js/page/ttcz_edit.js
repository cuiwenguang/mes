var totalWeight = 0;
var no = 0
var count = 0;
var totalNumber = 0;

$(function () {
    $("#formSG").bootstrapValidator({
        message: "提交的收购数据格式不对",
        feedbackIcons: {/*input状态样式图片*/
                 valid: 'glyphicon glyphicon-ok',
                 invalid: 'glyphicon glyphicon-remove',
                 validating: 'glyphicon glyphicon-refresh'
             },
        excuded: "disabled",
        fields:{
            'id_card': {
                message: "身份证号格式不正确",
                validators: {
                    notEmpty: {
                        message: "身份证号码不能为空"
                    },
                    regexp: {
                        regexp: "^(^[1-9]\\d{7}((0\\d)|(1[0-2]))(([0|1|2]\\d)|3[0-1])\\d{3}$)|(^[1-9]\\d{5}[1-9]\\d{3}((0\\d)|(1[0-2]))(([0|1|2]\\d)|3[0-1])((\\d{4})|\\d{3}[Xx])$)$",
                        message: "身份证号码格式不正确"
                    }
                },
            },
            'cust_name': {
                message: "姓名格式不对",
                validators: {
                    notEmpty: {
                        message: "姓名不能为空"
                    }
                }
            }
        }
    });

    $("#table1").bootstrapTable({});
    isPay();
    $("#pay_type").change(isPay);

    setInterval(function () {
       dt = new Date();
       if(document.activeElement.id=="cz_datetime"){
           return
       }
        $("#sg_datetime").val(dt.pattern("yyyy-MM-dd hh:mm:ss"));
    },1000);
});

function isPay() {
    pay_type = parseInt($("#pay_type").val())
    if (pay_type == 1){
        $("#sg_no").attr('disabled', 'disabled');
        $("#sg_no").val('');
        $(".jiesuan").show();
    } else {
        $("#sg_no").removeAttr('disabled');
        $(".jiesuan").hide();
    }
}

$("#btnSave").click(function () {
   if(parseFloat($("#mz_weight").val())<parseFloat($("#pz_weight").val())){
       alert("称重数据似乎不正确，检查是否传感器是否连接正常");
       return;
   }
   $("#lblCount").text(++count);
   $("#table1").bootstrapTable('insertRow',{
      index: 0,
       row:{
          no:++no,
         cur_number: $("#cur_number").val(),
         mz_weight: $("#mz_weight").val(),
         pz_weight: $("#pz_weight").val(),
         jz_weight: $("#jz_weight").val(),
         opt: "<buttn type='button' onclick='delRow("+count+")'>删除</buttn>"
       }
   });
   totalWeight += parseFloat($("#jz_weight").val());
   $("#lblWeight").text(totalWeight);
   $("#cz_weight").val(totalWeight);
   totalNumber += parseInt($("#cur_number").val());
   $("#lblNumber").text(totalNumber);
   $("#cz_number").val(totalNumber);
   var tp = parseFloat($("#sg_price").val()) * totalWeight;
   $("#total_price").val(tp.toFixed(2));
   $("#jz_weight").val(0);
   $("#mz_weight").val(0);
});

function delRow(index) {
   $("#table1").bootstrapTable('checkBy',{field:"no", values:[index]});
   var curRow = $("#table1").bootstrapTable('getSelections')[0];
   totalWeight -= parseFloat(curRow.jz_weight);
   $("#lblWeight").text(totalWeight);
    $("#cz_weight").val(totalWeight);
   totalNumber -= parseFloat(curRow.cur_number);
   $("#lblNumber").text(totalNumber);
   $("#cz_number").val(totalNumber);
   $("#lblCount").text(--count);
   var tp = parseFloat($("#sg_price").val()) * totalWeight;
   $("#total_price").val(tp.toFixed(2));
   $("#table1").bootstrapTable('remove', {field:"no", values:[index]});
}

function restToWait() {
    $("#table1").bootstrapTable('removeAll');
    totalWeight = 0;
   $("#lblWeight").text(totalWeight);
   $("#cz_weight").val(totalWeight);
   totalNumber = 0;
   count = 0;
   no = 0;
   $("#lblNumber").text(totalNumber);
   $("#cz_number").val(totalNumber);
   $("#lblCount").text(count);
   $("#total_price").val(0);
}

$("#btnSubmit").click(function (isPrint) {
    $("#formSG").bootstrapValidator('validate');
    if ($("#formSG").data('bootstrapValidator').isValid()) {
        if($("#cz_weight").val()=="0" || $("#cz_number").val()=="0"){
            try{
                 win.messageBox("没有任何称重数据，无法提交");
            } catch(err) {
                alert("没有任何称重数据，无法提交");
            }

            return
        }
        $.post("/post_ttcz",
            $("#formSG").serialize(),
            function (data) {
                $("#alertContainer").html('');
                if(data.code == 200){
                    $('<div class="alert alert-success" role="alert">' +
                        '<strong>'+data.message+'</strong>' +
                    '</div>').appendTo("#alertContainer").show(300).delay(1000).hide(300);
                    $("#formSG").data('bootstrapValidator').resetForm();
                    restToWait();

                } else {
                    $('<div class="alert alert-warning" role="alert">' +
                        '<strong>'+data.message+'</strong>' +
                    '</div>').appendTo("#alertContainer").show(300).delay(1000).hide(300);
                }
            });
    }
})
