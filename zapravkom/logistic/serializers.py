from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task, Cartridge, Client, Printer, Employee, ServiceTask, EmployeeTask, DetailsClient, UserMessage, RequestItem

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','process','client','date','description','working_time_1','working_time_2','cashsumm','get_set','employee','replace','payment_method','comment')

class CartridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartridge
        fields = ('id','code_name','simple_name','resourse','part','color','price','comment')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id','dateoflisted','name','phone','adress','organisation','commentary')

class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = ('id','name','compatibility','comment')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','firstname','middlename','lastname','phone','function')

class ServiceTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTask
        fields = ('id','task','cart','date','opc','pcr','mag','doc','wip','chip','fill','new','trash','comment','close')

class EmployeeTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTask
        fields = ('id','text','date','employee','done')

class DetailsClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailsClient
        fields = ('inn','client','nickname','name','kpp','adress','rs','ks','bik','comment')

class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields = ('id','message','to_user','from_user','onread')

class RequestItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestItem
        fields = ('id','text','date','urls','priority','done')
