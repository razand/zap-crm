from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

#Пользователь
class User(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	name = models.CharField('nickname',max_length=10,blank=False)
	def __str__(self):
		return self.user
#user messages
class UserMessage(models.Model):
	id = models.AutoField("id",primary_key=True,blank=False)
	message = models.CharField("Message",max_length=400,blank=True)
	to_user = models.ForeignKey(User, models.PROTECT,related_name="to_user")
	from_user = models.ForeignKey(User, models.PROTECT,related_name="from_user")
	onread = models.BooleanField("OnRead",default=False)
	def __str__(self):
		return '%s %s' % (self.from_user, self.message)
#клиент
class Client(models.Model):
	id = models.AutoField("ID", primary_key=True, blank = False)
	dateoflisted = models.DateField("Дата регистрации клиента",default=timezone.now, blank=False)
	name = models.CharField("Название или имя", max_length=50, blank=False)
	phone = models.CharField("Контакты", max_length=300, blank=False)
	adress = models.CharField("Адрес", max_length=300, blank=False)
	#------
	PHYSIC = 'PH'
	COMPANY = 'CO'
	NOT_SELECTED = 'NO'
	#------
	organisation = models.CharField("Физическое лицо или организация", max_length=20,
									  choices = ((PHYSIC, 'физическое_лицо'),(COMPANY,'компания'),(NOT_SELECTED,'неизвестно')),
									  default = NOT_SELECTED)
	commentary = models.CharField("Комментарий", max_length=300, blank=False)
	def publish(self):
		self.dateoflisted = timezone.now()
		self.save()
	def __str__(self):
		return '%s' % (self.name)

# сотрудник
class Employee(models.Model):
	id = models.AutoField(primary_key=True,blank=False)
	firstname = models.CharField("Имя",max_length=20,blank=False)
	middlename = models.CharField("Отчество",max_length=20,blank=False)
	lastname = models.CharField("Фамилия",max_length=20,blank=False)
	phone = models.CharField("Телефон",max_length=100,blank=False)
	#------
	COURIER = 'CO'
	MANAGER = 'MA'
	ENGINEER = 'EN'
	#------
	function = models.CharField("Должность",choices=((COURIER,'курьер'),(MANAGER,'менеджер'),(ENGINEER, 'инженер')), max_length=10, blank=False)
	def __str__(self):
		return '%s %s' % (self.firstname, self.lastname)

# картридж
class Cartridge(models.Model):
	id = models.AutoField(primary_key=True, blank=False)
	code_name = models.CharField("Кодовое название",max_length=20, blank=False)
	simple_name = models.CharField("Бытовое название",max_length=200,blank=True)
	resourse = models.IntegerField(default=0)
	#------
	CART = 'CART'
	DRUM = 'DRUM'
	TONER = 'TONER'
	#------
	part = models.CharField("Тип",choices=((CART,'картридж'),(DRUM,'драм'),(TONER,'туба')),max_length=10)
	#------
	CYAN = 'CYAN'
	MAGENTA = 'MAGENTA'
	YELLOW = 'YELLOW'
	BLACK = 'BLACK'
	#------
	color = models.CharField("Цвет",choices=((CYAN,'cyan'),(MAGENTA,'magenta'),(YELLOW,'yellow'),(BLACK,'black')),max_length=10)
	price = models.IntegerField("Цена",default=0)
	comment = models.CharField("commentary",max_length=100,blank=True)
	def __str__(self):
		return '%s' % (self.code_name)

# принтер
class Printer(models.Model):
	id = models.AutoField(primary_key=True, blank=False)
	name = models.CharField("Название", max_length=20, blank=False)
	compatibility = models.ManyToManyField(Cartridge)
	comment = models.CharField("commentary",max_length=100,blank=True)
	def __str__(self):
		return self.name

# заявка v.1
class Task(models.Model):
	id = models.AutoField("ID", primary_key=True, blank = False)
	#------
	DONE = 'Сделано'
	NOT_DONE = 'Не сделано'
	#------
	process = models.CharField("Статус исполнения", max_length=15,choices = ((DONE, 'Выполнено'), (NOT_DONE, 'Не выполнено')),
					default = NOT_DONE, blank = False)
	client = models.ForeignKey(Client, models.PROTECT,verbose_name="Клиент")
	date = models.DateField(default=timezone.now, blank=False) #~
	description = models.CharField("Адрес", max_length=300) #~
	working_time_1 = models.CharField("Рабочее время. С:",max_length=15, help_text="Со скольки")
	working_time_2 = models.CharField("Рабочее время. ДО:",max_length=15, help_text="До скольки") #~
	cashsumm = models.IntegerField("Сумма денег", help_text="Сумма денег которую надо получить от клиента, если оплата не по безналу") #~
	#------
	GET_ = 'Забрать'
	SET_ = 'Отдать'
	NO_ = 'Самовывоз'
	#------
	get_set = models.CharField("Отдать\забрать",
		max_length=7, choices = ((GET_, 'Забрать'),(SET_, 'Отдать'),(NO_,'Самовывоз')),
		default=NO_) #~
	employee = models.ForeignKey(Employee, models.PROTECT,verbose_name="Исполнитель") #~
	replace = models.ForeignKey(Cartridge, models.PROTECT,verbose_name="Подменка")
	CASH = 'Нал'
	CASHLESS = 'Безнал'
	NO_MONEY = 'Без оплаты'
	PAYMENT_METHOD_SELECTOR = ((CASH, 'Нал'), (CASHLESS, 'Безнал'),
							   (NO_MONEY, 'Без оплаты'),)
	payment_method = models.CharField("Нал\Безнал", max_length=11,
									  choices = PAYMENT_METHOD_SELECTOR,
									  default = NO_MONEY) #~
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

# Реквизиты
class DetailsClient(models.Model):
	inn = models.BigIntegerField("INN",primary_key=True,unique=True)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	nickname = models.CharField('Псевдоним',max_length=50,blank=False)
	name = models.CharField('Юридическое название',max_length=50,blank=False)
	kpp = models.IntegerField('КПП',blank=False)
	adress = models.CharField('Юр.адрес',max_length=200,blank=False)
	rs = models.BigIntegerField('РС',blank=False)
	ks = models.BigIntegerField('КС',blank=False)
	bik = models.BigIntegerField('БИК',blank=False)
	comment = models.CharField("commentary",max_length=200,blank=True)
	def __str__(self):
		return '%s %s %s %s' % (self.inn, self.nickname, self.name, self.comment)

# Задача для конкретного сотрудника
class EmployeeTask(models.Model):
	id = models.AutoField("id",primary_key=True)
	text = models.CharField("Сообщение",max_length=400,blank=False)
	date = models.DateField("Дата",default=timezone.now,blank=False)
	employee = models.ForeignKey(Employee, models.PROTECT)
	done = models.BooleanField("Выполнено",default=False)
	def publish(self):
		self.date = timezone.now()
		self.save()
	def __str__(self):
		return '%s %s %s %s' % (self.text, self.date, self.employee, self.done)
class RequestItem(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.CharField("Что купить",max_length=300,blank=False)
	date = models.DateField("Дата",default=timezone.now)
	urls = models.CharField("Где купить",max_length=300, default="",blank=True)
	P1 = 'Не срочно'
	P2 = 'Средняя'
	P3 = 'Срочно'
	#------
	priority = models.CharField("Срочность",max_length=10,
		choices = ((P1,'Не срочно'),(P2,'Средняя'),(P3,'Срочно')),
		default=P2)
	done = models.BooleanField(default=False,blank=False)
	def __str__(self):
		return '%s %s' % (self.text, self.priority)

class Feedback(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.CharField("Отзыв:",max_length=300,blank=False)
	date = models.DateField("Дата",default=timezone.now)
	def __str__(self):
		return '%s %s' % (self.text, self.date)
