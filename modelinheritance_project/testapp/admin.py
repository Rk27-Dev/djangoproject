from django.contrib import admin

# Register your models here.
from  testapp.models import contactinfo,student,teacher,contactinfo2,student2,teacher2,parent,child,subchild,emp,proxy_emp
admin.site.register(contactinfo)
admin.site.register(student)
admin.site.register(teacher)
# admin.site.register(contactinfo2)
# admin.site.register(student2)
# admin.site.register(teacher2)
admin.site.register(parent)
admin.site.register(child)
admin.site.register(subchild)
admin.site.register(proxy_emp)
admin.site.register(emp)