var totalWeight = 0;
var count = 0;
var totalNumber = 0;

$(function () {
    $("#table1").bootstrapTable({});
});

$("#btnSave").click(function () {
   $("#table1").bootstrapTable('insertRow',{
      index: 0,
       row:{
          no:++count,
         cur_number: $("#cur_number").val(),
         mz_weight: $("#mz_weight").val(),
         pz_weight: $("#pz_weight").val(),
         jz_weight: $("#jz_weight").val(),
         opt: "<buttn type='button' onclick='delRow("+count+")'>删除</buttn>"
       }
   });
   totalWeight += parseFloat($("#jz_weight").val());
   $("#lblWeight").text(totalWeight)
   totalNumber += parseInt($("#cur_number").val());
   $("#lblNumber").text(totalNumber);
   $("#lblCount").text(count);
});

function delRow(index) {
    $("#table1").bootstrapTable('remove', {field:"no", values:[index]});
}