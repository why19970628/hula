from rest_framework import serializers
from api import models


class ArticleSerializer(serializers.ModelSerializer):
    """
    序列化
    """
    # 2.添加一个category分类文本字段
    category_name = serializers.CharField(source='category.name', required=False)

    # 3 get_x1()
    x1 = serializers.SerializerMethodField()
    x2 = serializers.SerializerMethodField()
 
    # ststus 2.变为中文
    status_txt = serializers.CharField(source='get_status_display', required=False)

    class Meta:
        model = models.Article
        fields = ['id', 'title', 'summary', 'content', 'category',
                  'category_name', 'x1', 'status', 'status_txt', 'x2']  # category category_name可覆盖
        # fields = "__all__"
        # depth = 1  # 1. 关联表1级关联，2为2级，但不推荐，有多余数据

    def get_x1(self, obj):
        # obj为Article对象，将category.name返回给x1中
        return obj.category.name

     # ststus 3.变为中文
    def get_x2(self, obj):
        return obj.get_status_display()
