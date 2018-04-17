$(function () {
    $("#table1").bootstrapTable({
        "url": "/get_ttcz"
    });
})

function custFormatter(value) {
    return value.cust_name;
}