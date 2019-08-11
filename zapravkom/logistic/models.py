from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


#user messages
class UserMessage(models.Model):
	id = models.AutoField("id",primary_key=True )
	message = models.CharField("Message",max_length=400,blank=True)
	to_user = models.ForeignKey(User, models.PROTECT,related_name="to_user")
	from_user = models.ForeignKey(User, models.PROTECT,related_name="from_user")
	onread = models.BooleanField("OnRead",default=False)
	def __str__(self):
		return '%s %s' % (self.from_user, self.message)
# Реквизиты
class DetailsClient(models.Model):
	id = models.AutoField("id",primary_key=True )
	inn = models.BigIntegerField("INN",unique=True)
	nickname = models.CharField('Псевдоним',max_length=50 )
	name = models.CharField('Юридическое название',max_length=50 )
	kpp = models.IntegerField('КПП' )
	adress = models.CharField('Юр.адрес',max_length=200 )
	rs = models.BigIntegerField('РС' )
	ks = models.BigIntegerField('КС' )
	bik = models.BigIntegerField('БИК' )
	comment = models.CharField("commentary",max_length=200,blank=True)
	def __str__(self):
		return '%s' % (self.nickname)


#клиент
class Client(models.Model):
	id = models.AutoField("ID", primary_key=True, blank = False)
	dateoflisted = models.DateField("Дата регистрации клиента",default=timezone.now )
	name = models.CharField("Название или имя", max_length=50,blank=True)
	phone = models.CharField("Контакты", max_length=300,blank=True)
	adress = models.CharField("Адрес", max_length=300,blank=True)
	detailsclient = models.ForeignKey(DetailsClient, models.PROTECT,default=1)
	#------
	PHYSIC = 'PH'
	COMPANY = 'CO'
	NOT_SELECTED = 'NO'
	#------
	organisation = models.CharField("Физическое лицо или организация", max_length=20,
									  choices = ((PHYSIC, 'физическое_лицо'),(COMPANY,'компания'),(NOT_SELECTED,'неизвестно')),
									  default = NOT_SELECTED)
	commentary = models.CharField("Комментарий", max_length=300 ,blank=True)
	def publish(self):
		self.dateoflisted = timezone.now()
		self.save()
	def __str__(self):
		return '%s' % (self.name)

# сотрудник
class Employee(models.Model):
	id = models.AutoField(primary_key=True )
	firstname = models.CharField("Имя",max_length=20 ,blank=True)
	middlename = models.CharField("Отчество",max_length=20 ,blank=True)
	lastname = models.CharField("Фамилия",max_length=20 ,blank=True)
	phone = models.CharField("Телефон",max_length=100 ,blank=True)
	#------
	COURIER = 'CO'
	MANAGER = 'MA'
	ENGINEER = 'EN'
	#------
	function = models.CharField("Должность",choices=((COURIER,'курьер'),(MANAGER,'менеджер'),(ENGINEER, 'инженер')), max_length=10 )
	def __str__(self):
		return '%s %s' % (self.firstname, self.lastname)

# картридж
class Cartridge(models.Model):
	id = models.AutoField(primary_key=True )
	code_name = models.CharField("Кодовое название",max_length=20 ,blank=True)
	simple_name = models.CharField("Бытовое название",max_length=200,blank=True)
	resourse = models.IntegerField(default=0,blank=True)
	#------
	CART = 'CART'
	DRUM = 'DRUM'
	TONER = 'TONER'
	#------
	part = models.CharField("Тип",choices=((CART,'картридж'),(DRUM,'драм'),(TONER,'туба')),max_length=10,blank=True)
	#------
	CYAN = 'CYAN'
	MAGENTA = 'MAGENTA'
	YELLOW = 'YELLOW'
	BLACK = 'BLACK'
	#------
	color = models.CharField("Цвет",choices=((CYAN,'cyan'),(MAGENTA,'magenta'),(YELLOW,'yellow'),(BLACK,'black')),max_length=10,blank=True)
	price = models.IntegerField("Цена",default=0,blank=True)
	comment = models.CharField("commentary",max_length=100,blank=True)
	def __str__(self):
		return '%s' % (self.code_name)

# принтер
class Printer(models.Model):
	id = models.AutoField(primary_key=True,blank=False)
	name = models.CharField("Название", max_length=20 ,blank=True)
	compatibility = models.ManyToManyField(Cartridge,blank=True)
	comment = models.CharField("commentary",max_length=100,blank=True)
	def __str__(self):
		return self.name

# заявка v.1
class Task(models.Model):
	id = models.AutoField("ID", primary_key=True)
	#------
	DONE = 'Сделано'
	NOT_DONE = 'Не сделано'
	#------
	process = models.CharField("Статус исполнения", max_length=15,choices = ((DONE, 'Выполнено'), (NOT_DONE, 'Не выполнено')),
					default = NOT_DONE,blank=True)
	client = models.ForeignKey(Client, models.PROTECT,verbose_name="Клиент",default=1)
	date = models.DateField(default=timezone.now ,blank=True) #~
	description = models.CharField("Адрес", max_length=300,blank=True) #~
	working_time_1 = models.CharField("Рабочее время. С:",max_length=15, help_text="Со скольки",blank=True)
	working_time_2 = models.CharField("Рабочее время. ДО:",max_length=15, help_text="До скольки",blank=True) #~
	cashsumm = models.IntegerField("Сумма денег", help_text="Сумма денег которую надо получить от клиента, если оплата не по безналу",blank=True,default=0) #~
	#------
	GET_ = 'Забрать'
	SET_ = 'Отдать'
	NO_ = 'Самовывоз'
	#------
	get_set = models.CharField("Отдать\забрать",
		max_length=9, choices = ((GET_, 'Забрать'),(SET_, 'Отдать'),(NO_,'Самовывоз')),
		default=NO_,blank=True) #~
	employee = models.ForeignKey(Employee, models.PROTECT,verbose_name="Исполнитель",blank=True,default=6) #~
	replace = models.ForeignKey(Cartridge, models.PROTECT,verbose_name="Подменка",blank=True,default=7)
	CASH = 'Нал'
	CASHLESS = 'Безнал'
	NO_MONEY = 'Без оплаты'
	PAYMENT_METHOD_SELECTOR = ((CASH, 'Нал'), (CASHLESS, 'Безнал'),
							   (NO_MONEY, 'Без оплаты'),)
	payment_method = models.CharField("Нал\Безнал", max_length=11,
									  choices = PAYMENT_METHOD_SELECTOR,
									  default = NO_MONEY,blank=True) #~
	comment = models.CharField("Коментарий",max_length=200,blank=True)
	def publish(self):
		self.date = timezone.now()
		self.save()
	def __str__(self):
		return '%s' % (self.client)

# Единица сервисной работы
class ServiceTask(models.Model):
	id = models.AutoField("ID",primary_key=True)
	task = models.ForeignKey(Task, models.PROTECT)
	cart = models.ForeignKey(Cartridge, models.PROTECT)
	date = models.DateField(default=timezone.now)
	opc = models.BooleanField('фотобарабан',default = False)
	pcr = models.BooleanField('ролик заряда',default = False)
	mag = models.BooleanField('магнит',default = False)
	doc = models.BooleanField('дозирующее',default = False)
	wip = models.BooleanField('ракель',default = False)
	chip = models.BooleanField('чип',default = False)
	fill = models.BooleanField('заправка',default = False)
	new = models.BooleanField('надо новый',default = False)
	trash = models.BooleanField('списать',default = False)
	comment = models.CharField('коментарий',default=' ',max_length=150,blank=True)
	close = models.BooleanField('финиш',default=False)
	def publish(self):
		self.date = timezone.now()
		self.save()
	def __str__(self):
		return '%s %s %s %s' % (self.id, self.task, self.cart, self.comment)


# Задача для конкретного сотрудника
class EmployeeTask(models.Model):
	id = models.AutoField("id",primary_key=True)
	text = models.CharField("Сообщение",max_length=400 )
	date = models.DateField("Дата",default=timezone.now )
	employee = models.ForeignKey(Employee, models.PROTECT)
	done = models.BooleanField("Выполнено",default=False)
	def publish(self):
		self.date = timezone.now()
		self.save()
	def __str__(self):
		return '%s %s %s %s' % (self.text, self.date, self.employee, self.done)
class RequestItem(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.CharField("Что купить",max_length=300 )
	date = models.DateField("Дата",default=timezone.now)
	urls = models.CharField("Где купить",max_length=300, default="",blank=True)
	P1 = 'Не срочно'
	P2 = 'Средняя'
	P3 = 'Срочно'
	#------
	priority = models.CharField("Срочность",max_length=10,
		choices = ((P1,'Не срочно'),(P2,'Средняя'),(P3,'Срочно')),
		default=P2)
	done = models.BooleanField(default=False )
	def __str__(self):
		return '%s %s' % (self.text, self.priority)

class Feedback(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.CharField(max_length=300)
	date = models.DateField("Дата",default=timezone.now)
	def __str__(self):
		return '%s %s' % (self.text, self.date)
