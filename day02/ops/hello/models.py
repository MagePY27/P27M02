from django.db import models
# Create your models here.


class Asset(models.Model):
    """资产信息表"""
    hostname = models.CharField(max_length=128)
    ip = models.GenericIPAddressField('管理IP', unique=True)
    tag = models.ManyToManyField('Tag')
    ssh_key = models.ManyToManyField('ssh_key')

    class Meta:
        verbose_name_plural = "资产表"

    def __str__(self):
        return self.hostname


class Tag(models.Model):
    """
    资产标签
    """
    name = models.CharField('标签', max_length=32, unique=True)

    class Meta:
        verbose_name_plural = "标签表"

    def __str__(self):
        return self.name


class ssh_key(models.Model):
    """
    ssh秘钥
    """
    name = models.CharField('ssh秘钥名', max_length=32, unique=True)
    ssh_rsa = models.CharField('ssh秘钥', max_length=2048)
    ssh_user_name = models.CharField('ssh登录用户名', max_length=32)
    ssh_password = models.CharField('ssh密码', max_length=32)

    class Meta:
        verbose_name_plural = "密码表"

    def __str__(self):
        return self.name

