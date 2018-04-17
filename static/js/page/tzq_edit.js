var totalWeight = 0;
var no = 0
var count = 0;
var totalNumber = 0;

$(function () {
    $("#sg_no").blur(function () {
        if (this.value == "") return
        $.get("/get_sg/"+ this.value, function (data) {
            if(data.code == 200){
                initData(data.data);
            }else {
                alert("没有找到收购信息，检查收购批次好是否正确");
            }
        })
    })

    $("#table1").bootstrapTable({});
    isPay();
    $("#pay_type").change(isPay);

    setInterval(function () {
       dt = new Date();
       if(document.activeElement.id=="cz_datetime"){
           return
       }
        $("#tzq_datetime").val(dt.pattern("yyyy-MM-dd hh:mm:ss"));
    },1000);
});

function isPay() {
    pay_type = parseInt($("#pay_type").val())
    if (pay_type == 0){
        $(".jiesuan").show();
    } else {
        $(".jiesuan").hide();
    }
}

$("#btnSave").click(function () {
   if(parseFloat($("#mz_weight").val())<parseFloat($("#pz_weight").val())){
       try{
           win.messageBox("称重数据似乎不正确，检查是否传感器是否连接正常");
       }catch (err){
           alert("称重数据似乎不正确，检查是否传感器是否连接正常");
       }
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
   $("#cz_weight2").val(totalWeight);
   totalNumber += parseInt($("#cur_number").val());
   $("#lblNumber").text(totalNumber);
   $("#cz_number2").val(totalNumber);
   $("#jz_weight").val(0);
   $("#mz_weight").val(0);
});

function delRow(index) {
   $("#table1").bootstrapTable('checkBy',{field:"no", values:[index]});
   var curRow = $("#table1").bootstrapTable('getSelections')[0];
   totalWeight -= parseFloat(curRow.jz_weight);
   $("#lblWeight").text(totalWeight);
   $("#cz_weight2").val(totalWeight);
   totalNumber -= parseFloat(curRow.cur_number);
   $("#lblNumber").text(totalNumber);
   $("#cz_number2").val(totalNumber);
   $("#lblCount").text(--count);
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

    $("#cz_number").val("");
    $("#cz_weight").val("");
    $("#id_card").val("");
    $("#cust_name").val("");
    $("#mobile").val("");
    $("#address").val("");
    $("#sg_source").val("");
    $("#sg_datetime").val("")
    $("#table1").bootstrapTable('removeAll');
}

$("#btnSubmit").click(function (isPrint) {
    if(parseInt($("#cz_number2").val())<parseInt($("#cz_number").val()) ||
       parseInt($("#cz_weight2").val()) == 0){
        alert("核对收购数量和称重数据是否正确");
    }
    $.post("/post_tzq",
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

})

function initData(sg) {
    $("#pay_type").val(sg.pay_type);
    isPay();
    $("#cz_number").val(sg.cz_number);
    $("#cz_weight").val(sg.cz_weight);
    $("#id_card").val(sg.customer.id_card);
    $("#cust_name").val(sg.customer.cust_name);
    $("#mobile").val(sg.customer.mobile);
    $("#address").val(sg.customer.address);
    $("#sg_source").val(sg.sg_source);
    $("#c_standard").val(sg.c_standard);
    $("#c_type").val(sg.c_type);
    $("#sg_datetime").val(sg.sg_datetime)
}