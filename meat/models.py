import datetime

from django.db import models
from django.contrib.auth.models import User, Group


class Module(models.Model):
    """应用模块"""
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=50)
    icon = models.CharField(max_length=20)
    parent_id = models.IntegerField(default=0)


class AccessModule(models.Model):
    """用户组可以访问的模块"""
    module_id = models.ForeignKey(Module, related_name="modules",
                                  on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)


class Dictionary(models.Model):
    """数据字典"""
    item_key = models.CharField(max_length=50)  # 数据键
    item_val = models.CharField(max_length=50)  # 数据值
    item_type = models.CharField(max_length=20) # 字典类型


class SystemConfig(models.Model):
    """系统参数配置表"""
    pay_type = models.IntegerField(default=1) # 结算方式 0 活体结算； 1 酮体结算； 2 两者都可以
    live_buy_price = models.FloatField(default=0)  # 活体默认收购价格
    live_tare = models.FloatField(default=0)  # 活体默认皮重
    live_weigh_number = models.IntegerField(default=5)  # 活体默认每次可称重数量
    ketobody_weigh_number = models.IntegerField(default=5)  # 酮体默认每次可称重数量
    ketobody_buy_price = models.FloatField(default=0)  # 酮体默认收购价格
    ketobody_tare = models.FloatField(default=0)  # 酮体默认皮重
    unit_of_weight = models.CharField(max_length=10, default="KG")  # 重量计量单位
    unit_of_number = models.CharField(max_length=10, default="只(头)")  # 数量计量单位


class Customer(models.Model):
    id_card = models.CharField(max_length=20)
    cust_name = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)

    def to_dict(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])


class CollectInfo(models.Model):
    """收购信息表"""
    sg_no = models.CharField(max_length=50)  # 收购批次
    pay_type = models.IntegerField(default=1)  # 结算方式
    sg_price = models.FloatField(default=0)  # 收购单价
    sg_datetime = models.DateTimeField(auto_now=True)  # 收购时间
    tzq_datetime = models.DateTimeField(null=True, blank=True)  # 屠宰前时间
    tt_datetime = models.DateTimeField(null=True, blank=True)  # 酮体称重时间
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)  # 客户账号
    cz_weight = models.FloatField(default=0)  # 收购称重重量
    cz_weight2 = models.FloatField(default=0)  # 待宰前称重重量
    cz_weight3 = models.FloatField(default=0)  # 屠宰后称重量
    cz_number = models.IntegerField(default=0)  # 收购数量
    cz_number2 = models.IntegerField(default=0)  # 待宰前称重数量
    cz_number3 = models.IntegerField(default=0)  # 屠宰后称重量
    sg_source = models.CharField(max_length=100, default='')  # 收购来源
    c_type = models.CharField(max_length=20)  # 品种
    c_standard = models.CharField(max_length=20)  # 规格
    c_level = models.CharField(max_length=20)  # 等级
    state = models.IntegerField(default=1)  # 数据状态，备用
    flow_step = models.IntegerField(default=0)  # 流程状态，改数据到哪一步，0.活体称重；1. 屠宰前称重；2. 酮体称重;
    user = models.ForeignKey(User, related_name='user', null=True, on_delete=models.SET_NULL)  # 收购操作员
    user2 = models.ForeignKey(User, related_name='user2', null=True, on_delete=models.SET_NULL)  # 屠宰前称重操作员
    user3 = models.ForeignKey(User, related_name='user3', null=True, on_delete=models.SET_NULL)  # 酮体称重操作员

    def to_dict(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        for attr in fields:
            if isinstance(getattr(self, attr), datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr), datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            elif isinstance(getattr(self, attr), Customer):
                d[attr] = getattr(self, attr).to_dict()
            elif isinstance(getattr(self, attr), User):
                d[attr] = getattr(self,attr).username
            else:
                d[attr] = getattr(self, attr)
        return d


class RawLib(models.Model):
    """原料集冻库"""
    datetime_at = models.DateTimeField(auto_now_add=True)
    sc_no = models.CharField(max_length=50)
    sg_no = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)  # 客户账号
    ps_weight = models.FloatField(default=0)
    level = models.IntegerField(default=0)
    chfx = models.CharField(max_length=20)


class ProductInfo(models.Model):
    p_no = models.CharField(max_length=50)
    p_name = models.CharField(max_length=50)
    pack_spec_num = models.IntegerField(default=1)  # 包装规格 1包多少个
    pack_spec_weight = models.FloatField(default=0)  # 包装规格，1包多重


class ProductLib(models.Model):
    product = models.ForeignKey(ProductInfo, on_delete=models.SET_NULL)
    update_at = models.DateTimeField(auto_now_add=True)
    number = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    warning_number = models.FloatField(default=1) # 库存预警


class TransInfo(models.Model):
    """产品交易明细"""
    product = models.ForeignKey(ProductInfo, on_delete=models.SET_NULL)
    create_at = models.DateTimeField(auto_now_add=True)  # 交易时间
    direction = models.IntegerField() # 0:入库， 1：出库
    number = models.FloatField()  # 数量
    weight = models.FloatField()  # 重量
    sc_no = models.CharField(max_length=50)  # 生产批次
