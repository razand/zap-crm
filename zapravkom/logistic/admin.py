from django.contrib import admin
from .models import Client, Task, Employee, Cartridge, Printer, ServiceTask, DetailsClient, EmployeeTask
# Register your models here.
admin.site.register(Client)
admin.site.register(Task)
admin.site.register(Employee)
admin.site.register(Cartridge)
admin.site.register(Printer)
admin.site.register(ServiceTask)
admin.site.register(EmployeeTask)
admin.site.register(DetailsClient)
