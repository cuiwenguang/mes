var page = {};
var count = 0;
$(function () {
   page.table = $("#table1").bootstrapTable({
       data: [
            count++,
            $("#cur_number").val(),
            $("#mz_weight").val(),
            $("#pz_weight").val(),
            $("#jz_weight").val()
       ]
   });
});
