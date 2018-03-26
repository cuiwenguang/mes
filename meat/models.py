from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    '''收购对象：农牧民账户信息'''
    cust_name = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)


class CollectInfo(models.Model):
    '''收购称重环节数据'''
    collect_no = models.CharField(max_length=50) # 交易流水号
    creat_at = models.DateTimeField()  # 收购时间
    batch_number = models.CharField(max_length=20) # 收购批次
    customer = models.ForeignKey(Customer) # 客户账号
    collect_weight = models.FloatField(default=0)  # 称重数量
    collect_number = models.IntegerField(default=0)  # 收购数量
    standard = models.CharField(max_length=20) # 产品规格
    c_type = models.CharField(max_length=20) # 品种
    user = models.ForeignKey(User)


class ButcheringInfo(models.Model):
    '''待宰称重环节'''
    collect_no = models.CharField(max_length=50)  # 交易流水号
    creat_at = models.DateTimeField()  # 收购时间
    batch_number = models.CharField(max_length=20)  # 收购批次
    customer = models.ForeignKey(Customer)  # 客户账号
    collect_weight = models.FloatField(default=0)  # 称重数量
    collect_number = models.IntegerField(default=0)  # 收购数量
    standard = models.CharField(max_length=20)  # 产品规格
    c_type = models.CharField(max_length=20)  # 品种
    user = models.ForeignKey(User)


class ButcheredInfo(models.Model):
    '''屠宰称重环节'''
    collect_no = models.CharField(max_length=50)  # 交易流水号
    creat_at = models.DateTimeField()  # 收购时间
    batch_number = models.CharField(max_length=20)  # 收购批次
    customer = models.ForeignKey(Customer)  # 客户账号
    collect_weight = models.FloatField(default=0)  # 称重数量
    collect_number = models.IntegerField(default=0)  # 收购数量
    standard = models.CharField(max_length=20)  # 产品规格
    c_type = models.CharField(max_length=20)  # 品种
    level = models.CharField(max_length=20) # 等级
    user = models.ForeignKey(User)

