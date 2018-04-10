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



'''
class Customer(models.Model):
    cust_name = models.CharField(max_length=20)
    id_card = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)


class CollectInfo(models.Model):
    collect_no = models.CharField(max_length=50)  # 交易流水号
    creat_at = models.DateTimeField()  # 收购时间
    batch_number = models.CharField(max_length=20)  # 收购批次
    customer = models.ForeignKey(Customer, on_delete=None)  # 客户账号
    collect_weight = models.FloatField(default=0)  # 收购称重重量
    wait_weight = models.FloatField(default=0)  # 待宰前称重重量
    butcher_weight = models.FloatField(default=0)  # 屠宰后称重量
    collect_number = models.IntegerField(default=0)  # 收购数量
    standard = models.CharField(max_length=20)  # 产品规格
    c_type = models.CharField(max_length=20)  # 品种
    user = models.ForeignKey(User, on_delete=None)


class CollectInfo(models.Model):
    collect_no = models.CharField(max_length=50) # 交易流水号
    creat_at = models.DateTimeField()  # 收购时间
    batch_number = models.CharField(max_length=20) # 收购批次
    customer = models.ForeignKey(Customer, on_delete=None) # 客户账号
    collect_weight = models.FloatField(default=0)  # 称重重量
    collect_number = models.IntegerField(default=0)  # 收购数量
    standard = models.CharField(max_length=20) # 产品规格
    c_type = models.CharField(max_length=20) # 品种
    user = models.ForeignKey(User, on_delete=None)


class ButcheringInfo(models.Model):
    collect_no = models.CharField(max_length=50)  # 交易流水号
    creat_at = models.DateTimeField()  # 收购时间
    batch_number = models.CharField(max_length=20)  # 收购批次
    customer = models.ForeignKey(Customer, on_delete=None)  # 客户账号
    collect_weight = models.FloatField(default=0)  # 称重数量
    collect_number = models.IntegerField(default=0)  # 收购数量
    standard = models.CharField(max_length=20)  # 产品规格
    c_type = models.CharField(max_length=20)  # 品种
    user = models.ForeignKey(User, on_delete=None)


class ButcheredInfo(models.Model):
    collect_no = models.CharField(max_length=50)  # 交易流水号
    creat_at = models.DateTimeField()  # 收购时间
    batch_number = models.CharField(max_length=20)  # 收购批次
    customer = models.ForeignKey(Customer, on_delete=None)  # 客户账号
    collect_weight = models.FloatField(default=0)  # 称重数量
    collect_number = models.IntegerField(default=0)  # 收购数量
    standard = models.CharField(max_length=20)  # 产品规格
    c_type = models.CharField(max_length=20)  # 品种
    level = models.CharField(max_length=20) # 等级
    user = models.ForeignKey(User, on_delete=None)
    ps_weight = models.FloatField(default=0)  #排酸重量

'''
