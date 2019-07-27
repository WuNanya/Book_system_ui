"""Book_system_ui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views
urlpatterns = [
    # 出版社相关的对应关系
    path('publisher_list/', views.publisher_list),
    path('add_publisher/', views.add_publisher),
    path('delete_publisher/', views.delete_publisher),
    path('edit_publisher/', views.edit_publisher),
    # 书相关的对应关系
    path('book_list/', views.book_list),
    path('add_book/', views.add_book),  # 添加书籍
    path('delete_book/', views.delete_book),  # 删除书籍
    path('edit_book/', views.edit_book),  # 编辑书籍
    # 作者相关的对应关系
    path('author_list/', views.author_list),  # 展示作者
    path('add_author/', views.add_author),  # 添加作者
    path('delete_author/', views.delete_author),  # 删除作者
    path('edit_author/', views.edit_author),  # 编辑作者
]
