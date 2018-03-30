from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
