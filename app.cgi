#!C:/PythonXX/python.exe
import os
import sys

# 设置Django项目的路径
# sys.path.insert(0, 'C:/path/to/your/django/project')
sys.path.insert(0, 'G:/CanteenManagement/Django-ERP-ydf-canteen')

# 设置Django环境变量
os.environ['DJANGO_SETTINGS_MODULE'] = 'mis.settings'

# 引入wfastcgi并启动Django应用
import wfastcgi
wfastcgi.enable()
