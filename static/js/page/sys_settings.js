$(function () {
    $("#configForm").bootstrapValidator({
        message: "无效的值",
        feedbackIcons: {/*input状态样式图片*/
                 valid: 'glyphicon glyphicon-ok',
                 invalid: 'glyphicon glyphicon-remove',
                 validating: 'glyphicon glyphicon-refresh'
             },
        excuded: "disabled",
        fields:{
            /**
            'pay_type': {
                message: "至少选择一种结算方式",
                validators: {
                    choice: {
                        min:1,
                        max:2,
                        message: "至少选择一种结算方式"
                    }
                }
            },*/
            'unit_of_weight': {
                message: "重量计量单位输入不正确",
                validators: {
                    notEmpty: {
                        message: "重量计量单位不能为空"
                    }
                }
            },

            'unit_of_number': {
                message: "数量计量单位输入不正确",
                validators: {
                    notEmpty: {
                        message: "数量计量单位不能为空"
                    }
                }
            },
            'live_tare': {
                message: "活体默认皮重输入值不正确",
                validators: {
                    notEmpty: {
                        message: "活体默认皮重不能为空"
                    },
                    numeric: {
                        message: "活体默认皮重只能输入数字"
                    }
                }
            },
            'live_buy_price': {
                message: "活体收购默认单价输入值不正确",
                validators: {
                    notEmpty: {
                        message: "活体收购默认单价不能为空"
                    },
                    numeric: {
                        message: "活体收购默认单价只能输入数字"
                    }
                }
            },
            'live_weigh_number': {
                message: "活体默认每次可称重数量输入值不正确",
                validators: {
                    notEmpty: {
                        message: "活体默认每次可称重数量不能为空"
                    },
                    digits: {
                        message: "活体默认每次可称重数量只能输入整数"
                    }
                }
            },
            'ketobody_buy_price': {
                message: "酮体默认收购单价输入值不正确",
                validators: {
                    notEmpty: {
                        message: "酮体默认收购单价不能为空"
                    },
                    numeric: {
                        message: "酮体默认收购单价只能输入整数"
                    }
                }
            },
            'ketobody_tare': {
                message: "酮体默认皮重输入值不正确",
                validators: {
                    notEmpty: {
                        message: "酮体默认皮重不能为空"
                    },
                    numeric: {
                        message: "酮体默认皮重只能输入整数"
                    }
                }
            },
            'ketobody_weigh_number': {
                message: "酮体默认每次可称重数量输入值不正确",
                validators: {
                    notEmpty: {
                        message: "酮体默认每次可称重数量不能为空"
                    },
                    digits: {
                        message: "酮体默认每次可称重数量只能输入整数"
                    }
                }
            }
        }
    });
});

$("#btnSave").click(function () {
    $("#configForm").bootstrapValidator('validate');
    if ($("#configForm").data('bootstrapValidator').isValid()) {
        $.post("post_config",
            $("#configForm").serialize(),
            function (data) {
                $("#alertContainer").html('');
                if(data.code == 200){
                    $('<div class="alert alert-success" role="alert">' +
                        '<strong>'+data.message+'</strong>' +
                    '</div>').appendTo("#alertContainer").show(300).delay(1000).hide(300);
                    $("#configForm").data('bootstrapValidator').resetForm();
                } else {
                    $('<div class="alert alert-warning" role="alert">' +
                        '<strong>'+data.message+'</strong>' +
                    '</div>').appendTo("#alertContainer").show(300).delay(1000).hide(300);
                }
            });
    }
})