$(function () {
    $("#table1").bootstrapTable({
        "url": "get_sgdata"
    });
})

function custFormatter(value) {
    return value.cust_name;
}