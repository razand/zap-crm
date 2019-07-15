from django.urls import path, include
from . import views
from rest_framework import routers
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


taskrouter = routers.DefaultRouter()
taskrouter.register('a', views.TaskView)
cartridgerouter = routers.DefaultRouter()
cartridgerouter.register('a', views.CartridgeView)
clientrouter = routers.DefaultRouter()
clientrouter.register('a', views.ClientView)
printerrouter = routers.DefaultRouter()
printerrouter.register('a', views.PrinterView)
employeerouter = routers.DefaultRouter()
employeerouter.register('a', views.EmployeeView)
employeetaskrouter = routers.DefaultRouter()
employeetaskrouter.register('a', views.EmployeeTaskView)
servicetaskrouter = routers.DefaultRouter()
servicetaskrouter.register('a', views.ServiceTaskView)
detailclientrouter = routers.DefaultRouter()
detailclientrouter.register('a', views.DetailsClientView)
requestitemrouter = routers.DefaultRouter()
requestitemrouter.register('a', views.RequestItemView)
usermessagerouter = routers.DefaultRouter()
usermessagerouter.register('a', views.UserMessageView)

urlpatterns = [
    path('', views.main, name = 'main'),
    path('api/task/',include(taskrouter.urls)),
    path('api/cartridge/',include(cartridgerouter.urls)),
    path('api/client/',include(clientrouter.urls)),
    path('api/printer/',include(printerrouter.urls)),
    path('api/employee/',include(employeerouter.urls)),
    path('api/employeetask/',include(employeetaskrouter.urls)),
    path('api/servicetask/',include(servicetaskrouter.urls)),
    path('api/detailclient/',include(detailclientrouter.urls)),
    path('api/usermessage/',include(detailclientrouter.urls)),
    path('api/requestitem/',include(detailclientrouter.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('profile/',views.profile,name="profile"),
    path('search/',views.search,name='search'),
    path('client_list/',views.client_list,name='client_list'),
    path('detailsclient/',views.detailsclient,name='add new details for client'),
    path('task/',views.task,name='add new task'),
    path('requestitem/',views.requestitem,name='add bying request'),
    path('delivery/1',views.delivery1,name='vladislav'),
    path('delivery/2',views.delivery2,name='denis'),
    path('servicetask/',views.servicetask,name='add new service task'),
    path('cartridge/',views.cartridge,name='add new cartridge'),
    path('printer/',views.printer,name='add new printer'),
    path('employeetask/',views.employeetask,name='add new employee task')
]
