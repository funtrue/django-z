from django.db import models

class Demo_Model(models.Model):
    status_choices = (
        ("Yes", "使用中"),
        ("No", "未使用"),
    )
    demo_ip = models.CharField(max_length=64, verbose_name="ip", null=True, blank=True, help_text="ip")
    demo_app_name = models.CharField(max_length=32, verbose_name="应用名", null=True, blank=True, help_text="应用名")
    demo_status = models.CharField(choices=status_choices, max_length=32, verbose_name="状态", null=True, blank=True, help_text="状态")
    demo_describe = models.TextField(verbose_name="描述", null=True, blank=True, help_text="使用描述")
    demo_Duration = models.BooleanField(default=False, verbose_name="是否永久", help_text="是否永久")
    demo_allocation_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, help_text="创建时间")
    
    class Meta:
        ordering = ('demo_ip',)
        verbose_name = 'DemoData'
        verbose_name_plural = 'Demo数据管理'