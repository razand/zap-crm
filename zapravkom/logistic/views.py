from django.shortcuts import render
from django.utils import timezone
from .forms import TaskForm, CartridgeForm, ClientForm, PrinterForm, EmployeeForm, ServiceTaskForm, DetailsClientForm, RequestItemForm, UserMessageForm, FeedbackForm
from .models import Task, Cartridge, Client, Printer, Employee, ServiceTask, EmployeeTask, DetailsClient, RequestItem, UserMessage, Feedback
from .serializers import TaskSerializer, CartridgeSerializer, ClientSerializer, PrinterSerializer, EmployeeSerializer, ServiceTaskSerializer, EmployeeTaskSerializer, DetailsClientSerializer, UserMessageSerializer, RequestItemSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.

class TaskView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    def get_queryset(self):
        qs = Client.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(phone__icontains=query)|
                           Q(name__icontains=query)|
                           Q(adress__icontains=query)|
                           Q(commentary__icontains=query)).distinct()
        return qs

class PrinterView(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CartridgeView(viewsets.ModelViewSet):
    queryset = Cartridge.objects.all()
    serializer_class = CartridgeSerializer

class ServiceTaskView(viewsets.ModelViewSet):
    queryset = ServiceTask.objects.all()
    serializer_class = ServiceTaskSerializer

class EmployeeTaskView(viewsets.ModelViewSet):
    queryset = EmployeeTask.objects.all()
    serializer_class = EmployeeTaskSerializer

class DetailsClientView(viewsets.ModelViewSet):
    queryset = DetailsClient.objects.all()
    serializer_class = DetailsClientSerializer
class UserMessageView(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer
class RequestItemView(viewsets.ModelViewSet):
    queryset = RequestItem.objects.all()
    serializer_class = RequestItemSerializer
def login(request):
    context = {'login':False}
    return render(request,"login.html",context)

def main(request):
    date = timezone.now()
    title = "Главная страница"
    counters = {}
    counters["clients_count"] = len(Client.objects.all())
    counters["task_count"] = len(Client.objects.all())
    counters["cartridge_count"] = len(Cartridge.objects.all())
    counters["printer_count"] = len(Printer.objects.all())
    counters["servicetask_count"] = len(ServiceTask.objects.all())
    counters["today_task_count"] = len(Task.objects.filter(date__lte=timezone.now()))
    form_feedback = FeedbackForm(request.POST or None)
    if form_feedback.is_valid():
        form_feedback.save()
        return HttpResponseRedirect("/logistic/")
    feedback_list = Feedback.objects.all()
    context = {'date':date,'title':title,'counters':counters,'form':form_feedback,'list':feedback_list}
    return render(request, "index.html", context)

def search(request):
    if request.method == POST:
        search = request.POST['search']
        model = request.POST['model']
    else:
        respond = ''
        context = {'respond':respond}
        return render(request,"search.html",context)
    if model == 'help':
        respond = {'1. name>phone>commentary>adress':'Client',
                  '2. inn>adress>nickname>comment':'DetailsClient',
                  '3. date=today process=notdone':'Task',
                  '3.1. process=notdone':'TaskNotClose',
                  '3.2. date=today':'TaskToday',
                  '4. close=false':'ServiceTask',
                  '5. name':'Employee',
                  '6. done=false':'EmployeeTask',
                  '7. codename>simplename':'Cartridge',
                  '8. name':'Printer'}
        context = {'respond':respond}
        return render(request,"search.html",context)

    if model == 'Client':
        respond = Client.objects.filter(name__icontains=search)
        if not respond:
            respond = Client.objects.filter(phone__icontains=search)
            if not respond:
                respond = Client.objects.filter(commentary__icontains=search)
                if not respond:
                    respond = Client.objects.filter(adress__icontain=search)
        context = {'respond':respond}
        return render(request,"search.html",context)

    if model == 'DetailsClient':
        respond = DetailsClient.objects.filter(inn__icontains=search)
        if not respond:
            respond = DetailsClient.objects.filter(adress__icontains=search)
            if not respond:
                respond = DetailsClient.objects.filter(nickname__icontains=search)
                if not respond:
                    respond = DetailsClient.objects.filter(comment__icontain=search)
        context={'respond':respond}
        return render(request,"search.html",context)

    if model == 'Task':
        respond0 = Task.objects.filter(date__lte=timezone.now())
        respond = respond0.filter(process=NOT_DONE)
        context={'respond':respond}
        return render(request,"search.html",context)

    if model == 'TaskNotClose':
        respond = Task.objects.filter(process=NOT_DONE)
        context={'respond':respond}
        return render(request,"search.html",context)

    if model == 'TaskToday':
        respond = Task.objects.filter(date__lte=timezone.now())
        context={'respond':respond}
        return render(request,"search.html",context)

    if model == 'ServiceTask':
        respond = ServiceTask.objects.filter(close=False)

        context={'respond':respond}
        return render(request,"search.html",context)

    if model == 'Employee':
        respond = Client.objects.filter(firstname__icontains=search)

        context={'respond':respond}
        return render(request,"search.html",context)

    if model == 'EmployeeTask':
        respond = Client.objects.filter(done=False)

        context={'respond':respond}
        return render(request,"search.html",context)

    if model == 'Cartridge':
        respond = Client.objects.filter(code_name__icontains=search)
        if not respond:
            respond = Client.objects.filter(simple_name__icontains=search)

        context={'respond':respond}
        return render(request,"search.html",context)

    if model == 'Printer':
        respond = Client.objects.filter(name__icontains=search)

        context={'respond':respond}
        return render(request,"search.html",context)

    respond = {}
    context = {'respond':respond}
    return render(request,"search.html",context)
def profile(request):
    context = {}
    return render(request, "profile.html", context)
def client_list(request):
    client_list = Client.objects.all().order_by('id')
    form_client = ClientForm(request.POST or None)
    if form_client.is_valid():
        form_client.save()
        return HttpResponseRedirect("/logistic/client_list/")
    context = {'list':client_list,'form':form_client}
    return render(request,"client_list.html",context)
def detailsclient(request):
    return render(request,"search.html",context)
def task(request):
    task_list = Task.objects.all().order_by('id')
    form_task = TaskForm(request.POST or None)
    if form_task.is_valid():
        form_task.save()
        return HttpResponseRedirect("/logistic/task/")
    context = {'list':task_list,'form':form_task}
    return render(request,"task_list.html",context)
def servicetask(request):
    servicetask_list = ServiceTask.objects.filter(close=False).order_by('id')
    form_servicetask = ServiceTaskForm(request.POST or None)
    if form_servicetask.is_valid():
        form_servicetask.save()
        return HttpResponseRedirect("/logistic/servicetask/")
    context = {'list':servicetask_list,'form':form_servicetask}
    return render(request,"servicetask_list.html",context)
def cartridge(request):
    return render(request,"search.html",context)
def printer(request):
    return render(request,"search.html",context)
def employeetask(request):
    employeetask_list = Task.objects.all().order_by('id')
    form_employeetask = TaskForm(request.POST or None)
    if form_employeetask.is_valid():
        form_employeetask.save()
        return HttpResponseRedirect("/logistic/servicetask/")
    context = {'list':employeetask_list,'form':form_employeetask}
    return render(request,"task_list.html",context)
def requestitem(request):
    requestitem_list = RequestItem.objects.filter(done=False).order_by('id')
    form_requestitem = RequestItemForm(request.POST or None)
    if form_requestitem.is_valid():
        form_requestitem.save()
        return HttpResponseRedirect("/logistic/requestitem/")
    context = {'list':requestitem_list,'form':form_requestitem}
    return render(request,"order_list.html",context)
def delivery1(request):
    task_v = Task.objects.filter(employee=1,process='Не сделано').order_by('id')
    context = {'list':task_v}
    return render(request,"vladislav_task.html",context)

def delivery2(request):
    task_d = Task.objects.filter(employee=2,process='Не сделано').order_by('id')
    context = {'list':task_d}
    return render(request,"denis_task.html",context)
