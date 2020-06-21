from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import serializers
from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from api import models, serializer
from django.forms.models import model_to_dict


class DrfCategory(APIView):
    pass


class DrfCategoryView(APIView):
    def get(self, request, *args, **kwargs):
        """
        获取所有文章列表
        """
        pk = kwargs.get('pk')
        if not pk:

            data = models.Category.objects.all().values('id', 'name')
            data_list = list(data)

            return Response(data_list)
        category_object = models.Category.objects.filter(id=pk).first()
        data = model_to_dict(category_object)
        return Response(data)

    def post(self, request, *args, **kwargs):
        """
        增加一条分类信息
        """
        # name = request.POST.get('name')
        print(request.body)
        print(request.data)
        models.Category.objects.create(**request.data)
        return Response('成功')

    def delete(self, request, *args, **kwargs):
        """
        删除一条分类信息
        """
        pk = kwargs.get('pk')
        if not pk:
            return Response('请选择删除的 id')
        data = models.Category.objects.filter(id=pk).delete()
        if data[0] == 0:
            return Response('删除--无此数据')
        return Response('删除成功')

    def put(self, request, *args, **kwargs):
        """
        更新一条分类信息
        """
        pk = kwargs.get('pk')
        if not pk:
            return Response('请选择删除的 id')
        data = models.Category.objects.filter(id=pk).update(**request.data)
        print(data)
        if data == 0:
            return Response('更新--无此数据')
        return Response('更新成功')


class NewCategorySerializer(serializers.ModelSerializer):
    """
    序列化
    """
    class Meta:
        model = models.Category
        # fields = "__all__"
        fields = ['id', 'name']


class NewCategoryView(ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView):

    queryset = models.Category.objects.all()
    serializer_class = NewCategorySerializer


class NewCategoryView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print(pk)
        if not pk:
            queryset = models.Category.objects.all()
            ser = NewCategorySerializer(instance=queryset, many=True)
            return Response(ser.data)
        else:
            model_object = models.Category.objects.filter(id=pk).first()
            ser = NewCategorySerializer(instance=model_object, many=False)
            return Response(ser.data)

    def post(self, request, *args, **kwargs):
        ser = NewCategorySerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        category_object = models.Category.objects.filter(id=pk).first()
        ser = NewCategorySerializer(
            instance=category_object, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def delete(self, request, *args, **kwargs):
        """
        删除一条分类信息
        """
        pk = kwargs.get('pk')
        if not pk:
            return Response('请选择删除的 id')
        data = models.Category.objects.filter(id=pk).delete()
        if data[0] == 0:
            return Response('删除--无此数据')
        return Response('删除成功')


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            queryset = models.Article.objects.all()
            ser = serializer.ArticleSerializer(instance=queryset, many=True)
            return Response(ser.data)
        article_object = models.Article.objects.filter(id=pk).first()
        ser = serializer.ArticleSerializer(
            instance=article_object, many=False)  # 单条记录
        return Response(ser.data)

    def post(self, request, *args, **kwargs):
        ser = serializer.ArticleSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    # put为全部字段更新
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        article_object = models.Article.objects.filter(id=pk).first()
        ser = serializer.ArticleSerializer(
            instance=article_object, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        article_object = models.Article.objects.filter(id=pk).first()
        ser = serializer.ArticleSerializer(
            instance=article_object, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def delete(self, request, *args, **kwargs):
        """
        删除一条分类信息
        """
        pk = kwargs.get('pk')
        if not pk:
            return Response('请选择删除的 id')
        data = models.Article.objects.filter(id=pk).delete()
        if data[0] == 0:
            return Response('删除--无此数据')
        return Response('删除成功')


class NewArticleView(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            queryset = models.Article.objects.all()
            ser = serializer.NewArticleSerializer(instance=queryset, many=True)
            return Response(ser.data)
        article_object = models.Article.objects.filter(id=pk).first()
        ser = serializer.NewArticleSerializer(
            instance=article_object, many=False)
        return Response(ser.data)

    def post(self, request, *args, **kwargs):
        ser = serializer.FormNewArticleSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def put(self, request, *args, **kwargs):
        """全部更新"""
        pk = kwargs.get('pk')
        article_object = models.Article.objects.filter(id=pk).first()
        ser = serializer.FormNewArticleSerializer(
            instance=article_object, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def patch(self, request, *args, **kwargs):
        """局部"""
        pk = kwargs.get('pk')
        article_object = models.Article.objects.filter(id=pk).first()
        ser = serializer.FormNewArticleSerializer(
            instance=article_object, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        models.Article.objects.filter(id=pk).delete()
        return Response('删除成功')
