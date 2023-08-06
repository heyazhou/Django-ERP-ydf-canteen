from django.contrib import admin


class AdminSite(admin.AdminSite):
    site_header = '广水卷烟厂职工食堂物资管理系统'
    site_title = '操作'
    index_title = '系统首页'
