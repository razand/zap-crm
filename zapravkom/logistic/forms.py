from django import forms
from .models import Task, Client, Printer, Cartridge, Employee, ServiceTask, EmployeeTask, DetailsClient, RequestItem, UserMessage, Feedback
from django.forms import ModelForm, Select, Textarea, TextInput, NumberInput, RadioSelect

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['description']
		widgets = {'description':Textarea(attrs={'type':'hidden'})}
'''
fields = ['description', 'working_time_1', 'working_time_2',
		 		  'cashsumm', 'get_set', 'employee',
				  'replace', 'payment_method', 'comment','client']
		widgets = {
			'description': Textarea(attrs={'class':'form-control-sm mb-2','rows':2}),
			'working_time_1': TextInput(attrs={'class':'form-control-sm','type':'time','min':'8:00','max':'19:00','class':'worktime'}),
			'working_time_2': TextInput(attrs={'class':'form-control-sm','type':'time','min':'8:00','max':'19:00','class':'worktime'}),
			'cashsumm': NumberInput(attrs={'class':'form-control-sm','min':'50','step':'10'}),
			'get_set': Select(attrs={'class':'form-control-sm'}),
			'employee': Select(attrs={'class':'form-control-sm'}),
			'replace': Select(attrs={'class':'form-control-sm'}),
			'client': Select(attrs={'class':'form-control-sm','value':'1'}),
			'payment_method': Select(attrs={'class':'form-control-sm'})
		}
'''
class ServiceTaskForm(ModelForm):
	class Meta:
		model = ServiceTask
		fields = ['task','cart']
#'detailsclient'
class ClientForm(ModelForm):
	class Meta:
		model = Client
		fields = [ 'name', 'phone', 'adress', 'organisation', 'commentary',]

class DetailsClientForm(ModelForm):
	class Meta:
		model = DetailsClient
		fields = ['inn','nickname','name','kpp','adress','rs','ks','bik','comment']

class PrinterForm(ModelForm):
	class Meta:
		model = Printer
		fields = ['name', 'compatibility']

class CartridgeForm(ModelForm):
	class Meta:
		model = Cartridge
		fields = ['code_name', 'simple_name', 'resourse', 'part', 'color']

class EmployeeForm(ModelForm):
	class Meta:
		model = Employee
		fields = ['firstname', 'middlename', 'lastname', 'phone', 'function']

class EmployeeTaskForm(ModelForm):
	class Meta:
		model = EmployeeTask
		fields = ['text','employee','done']

class RequestItemForm(ModelForm):
	class Meta:
		model = RequestItem
		fields = ['text','urls','priority']

class UserMessageForm(ModelForm):
	class Meta:
		model = UserMessage
		fields = ['message','to_user']

class FeedbackForm(ModelForm):
	class Meta:
		model = Feedback
		fields = ['text']
