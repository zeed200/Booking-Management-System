from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date
# Create your models here.

class Firm(models.Model):
    f_logo = models.ImageField(null=False,verbose_name='شعار الموسسه')
    f_name_ar = models.CharField(max_length=100,null=False,verbose_name='اسم الموسسه ar')
    f_name_en = models.CharField(max_length=100,null=False,verbose_name=' اسم الموسسه en')
    f_address_ar = models.CharField(max_length=100,null=False,verbose_name='العنوان ar')
    f_address_en = models.CharField(max_length=100,null=False,verbose_name='العنوان en')
    f_phon_ar = models.IntegerField(null=False,verbose_name='الرقم')
    f_phon_en = models.IntegerField(null=False,verbose_name='الرقم')

    def __str__(self): 
         return self.f_name_ar
    
    class Meta:
         verbose_name_plural = 'الموسسه'
         verbose_name = 'البيانات'

class Branch(models.Model):
    bra_name = models.CharField(max_length=20,null=False,verbose_name='اسم الفرع')
    bra_address = models.CharField(max_length=20,null=False,verbose_name='عنوان الفرع')
    bra_add_datetime = models.DateTimeField(default=datetime.now,verbose_name='تاريخ ووقت الأضافه')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user',verbose_name=' المستخدم')

    def __str__(self): 
         return self.bra_name
    
    class Meta:
         verbose_name_plural = 'الفروع'
         verbose_name = 'فرع'


class Towers(models.Model):
     Branch = models.ForeignKey(Branch,on_delete=models.CASCADE,verbose_name='الفرع')
     tow_name = models.CharField(max_length=20,null=False,verbose_name='اسم البرج')
     tow_floornumber = models.IntegerField(null=False,verbose_name='عدد الطوابق')
     tow_add_datetime = models.DateTimeField(default=datetime.now,verbose_name='تاريخ ووقت الأضافه')
     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name=' المستخدم')

     def __str__(self): 
         return self.tow_name
     
     class Meta:
         verbose_name_plural = 'البرج'
         verbose_name = 'برج'


class Apartmint_chalit(models.Model):
     towers = models.ForeignKey(Towers,on_delete=models.CASCADE,verbose_name='البرج')
     apa_cha_status = models.BooleanField(null=True,verbose_name='الحاله')

     def __str__(self): 
         return 'LOCATION IN {SELF.Towers.tow_name}'
     
     class Meta:
         verbose_name_plural = 'الشقق والشاليهات'
         verbose_name = 'شقه او شاليه'

              
class Apartments(Apartmint_chalit):
     apa_name = models.CharField(max_length=20,null=False,verbose_name='اسم الشقه')
     apa_floor = models.CharField(max_length=20,null=True,verbose_name='الطابق')
     apa_price = models.DecimalField(max_digits=10,decimal_places=2,null=False,verbose_name='السعر')
     apa_discrip = models.TextField(max_length=50,null=True,verbose_name='الوصف')
     apa_status = models.BooleanField(null=True,verbose_name='الحاله')
     apa_add_datetime = models.DateTimeField(default=datetime.now,verbose_name='تاريخ ووقت الأضافه')
     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم')

     def __str__(self): 
         return self.apa_name
     
     class Meta:
         verbose_name_plural = 'الشقق'
         verbose_name = 'شقه'
     

class Chalets(Apartmint_chalit):
     cha_name = models.CharField(max_length=20,null=False,verbose_name='اسم الشاليه')
     cha_floor = models.CharField(max_length=20,null=True,verbose_name='الطابق')
     cha_discrip = models.TextField(max_length=50,null=True,verbose_name='الوصف')
     cha_status = models.BooleanField(default=True)
     cha_add_datetime = models.DateTimeField(default=datetime.now,verbose_name='تاريخ ووقت الأضافه')
     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم')

     def __str__(self): 
         return self.cha_name
     
     class Meta:
         verbose_name_plural = 'الشاليهات'
         verbose_name = 'شاليه'
     

class Bunch(models.Model): 
     bun_name = models.CharField(max_length=50,null=False,verbose_name='اسم الباقه')
     bun_people_number = models.IntegerField(null=True,verbose_name='عدد الأشخاص')
     bun_entrytime = models.TimeField(null=True,verbose_name='وقت الدخول')
     bun_exittime = models.TimeField(null=True,verbose_name='وقت الخروج')
     bun_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='السعر')
     addpeo_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='سعر الاأشخاص الأضافيين')
     bun_childprice = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='سعر الأطفال') 
     bun_add_datetime = models.DateTimeField(default=datetime.now,verbose_name='تاريخ ووقت الأضافه')
     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم')

     def __str__(self): 
         return self.bun_name
     
     class Meta:
         verbose_name_plural = 'الباقات'
         verbose_name = 'باقه'
     

class People(models.Model):
     status = [
         ('enter','تم الدخول'),
         ('notenter','لم يتم الدخول'),
              ]

     reservecha = models.ForeignKey('Reservecha',on_delete=models.CASCADE,verbose_name='اسم الحجز')
     peo_name = models.CharField(max_length=50,null=False,verbose_name='الأسم')
     peo_age = models.IntegerField(null=False,verbose_name='العمر')
     peo_card_number = models.IntegerField(null=True,verbose_name='رقم البطاقه')
     peo_add_datetime = models.DateTimeField(default=datetime.now,verbose_name='تاريخ ووقت الأضافه')
     st_people = models.CharField(max_length=20, choices=status, null=True, verbose_name='الحاله',default= 'notenter')
     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم',default='abdalrahman')

     def __str__(self): 
         return self.peo_name
     
     class Meta:
         verbose_name_plural = 'الأشخاص'
         verbose_name = 'شخص'
     
class Customers(models.Model):
     cus_name = models.CharField(max_length=50,null=False,verbose_name='اسم العميل')
     cus_card_id = models.IntegerField(null=False,verbose_name='رقم البطاقه')
     cus_phone_number = models.IntegerField(null=False,verbose_name='رقم التلفون')
     cus_address = models.CharField(max_length=20,null=True,verbose_name='العنوان')
     cus_age = models.IntegerField(null=True,verbose_name='العمر')
     cus_gender = models.CharField(max_length=10,null=True,verbose_name='الجنس')
     cus_add_datetime = models.DateTimeField(default=datetime.now,verbose_name='تاريخ ووقت الأضافه')
     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم')

     def __str__(self): 
         return self.cus_name
     
     class Meta:
         verbose_name_plural = 'العملاء'
         verbose_name = 'عميل'
     


class Reservecha(models.Model):
     
     status = [
         ('sure','مؤكد'),
         ('notsure','غير مؤكد'),
         ('cancel','ملغي'),
         ('done','منتهي'),
     ]

     chalits = models.ForeignKey(Chalets,on_delete=models.CASCADE,verbose_name='الشاليه')
     bunch = models.ForeignKey(Bunch,on_delete=models.CASCADE,verbose_name='نوع الباقه')
     customers = models.ForeignKey(Customers,on_delete=models.CASCADE,verbose_name='اسم العميل')
     res_cha_date = models.DateField(null=False,verbose_name='تاريخ الحجز', default=datetime.now)
     login_time = models.TimeField(null=False,verbose_name='وقت الدخول')
     exit_time = models.TimeField(null=False,verbose_name='وقت الخروج')
     res_cha_price = models.DecimalField(max_digits=10,decimal_places=2,null=False,verbose_name='السعر')
     add_datetime = models.DateTimeField(default=datetime.now,verbose_name='تاريخ ووقت الأضافه')
     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم',default='abdalrahman')
     st_book = models.CharField(max_length=20, choices=status, null=True, verbose_name='الحاله',default= 'notsure')
     def __str__(self): 
         return self.customers.cus_name
     
     
         
     class Meta:
         verbose_name_plural = 'حجز شاليه'
         verbose_name = 'حجز '


class Check(models.Model):
     reservecha = models.ForeignKey(Reservecha,on_delete=models.CASCADE,verbose_name='اسم الحجز')
     che_status = models.BooleanField(verbose_name='الحاله')
     che_date = models.DateField(null=False,verbose_name='التاريخ')
     che_add_datetime = models.DateTimeField(default=datetime.now,verbose_name='تاريخ ووقت الأضافه') 
     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم')

     def __str__(self): 
         return self.reservecha.customers.cus_name
     
     class Meta:
         verbose_name_plural = 'الفحص'
         verbose_name = 'فحص'
     

class Content(models.Model):
     chalit = models.ForeignKey(Chalets,on_delete=models.CASCADE,null=True,verbose_name=' الشاليهات')
     con_name = models.CharField(max_length=50,null=False,verbose_name='المحتوى')
     con_price = models.DecimalField(max_digits=10,decimal_places=2,null=False,verbose_name='السعر')
     con_add_datetime = models.DateTimeField(default=datetime.now,verbose_name='تاريخ ووقت الأضافه') 
     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم')

     def __str__(self): 
         return self.con_name
     
     class Meta:
         verbose_name_plural = 'المحتويات'
         verbose_name = 'المحتوى'
         
     

class Fund(models.Model):
     fun_name = models.CharField(max_length=30,null=False,verbose_name='اسم الصندوق')
     fun_add_datetime = models.DateTimeField(default=datetime.now,verbose_name='تاريخ ووقت الأضافه')
     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم')

     def __str__(self): 
         return self.fun_name
     
     class Meta:
         verbose_name_plural = 'الصندوق'
         verbose_name = 'صندوق'
     

     

class Mortgage(models.Model):
     fund = models.ForeignKey(Fund,on_delete=models.CASCADE,verbose_name='الصندوق')
     reservecha = models.ForeignKey(Reservecha,on_delete=models.CASCADE, null=True, verbose_name='رقم الحجز')
     mor_date = models.DateField(null=True,verbose_name='التاريخ')
     mor_type = models.CharField(max_length=50,null=False,verbose_name='نوع الرهن')
     mor_notice = models.TextField(null=True,verbose_name='ملاحظات')
     mor_amaunt = models.DecimalField(max_digits=10,decimal_places=2,null=True,verbose_name='المبلغ', default=0.00)
     mor_status = models.BooleanField(verbose_name='الحاله', null=True, default=False)
     mor_add_datetme = models.DateTimeField(default=datetime.now,verbose_name='تاريخ ووقت الأضافه')
     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم')

     def __str__(self): 
         return self.reservecha.customers.cus_name
     
     class Meta:
         verbose_name_plural = 'الرهونات'
         verbose_name = 'رهن'
     

class Reserveape(models.Model):
     
     status = [
         ('sure','مؤكد'),
         ('notsure','غير مؤكد'),
         ('cancel','ملغي'),
         ('done','منتهي'),
     ]
     
     apartments = models.ForeignKey(Apartments,null=True,on_delete=models.CASCADE,verbose_name='الشقه')
     customers = models.ForeignKey(Customers,null=True,on_delete=models.CASCADE,verbose_name='اسم العميل')
     login_date = models.DateField(null=True,verbose_name='تاريخ الدخول')
     exit_date = models.DateField(null=True,verbose_name='تاريخ الخروج')
     res_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,verbose_name='السعر')
     res_notice = models.TextField(null=True,verbose_name='ملاحظات')
     add_datetme = models.DateTimeField(default=datetime.now,verbose_name='تاريخ ووقت الأضافه')
     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم',default='abdalrahman')
     st_book = models.CharField(max_length=20, choices=status, null=True, verbose_name='الحاله', default= 'notsure')
     

     def __str__(self): 
         return self.customers.cus_name

     
              
     class Meta:
         verbose_name_plural = 'حجز شقه'
         verbose_name = 'حجز '

class Resapa_date(models.Model):
    apartments = models.ForeignKey(Apartments,on_delete=models.CASCADE,verbose_name='الشقه')
    res_date = models.CharField(null=True,max_length=50 , verbose_name='التواريخ المحجوزه')

    def __str__(self): 
         return self.apartments.apa_name
    
    class Meta:
         verbose_name_plural = 'التواريخ المحجوزه'
         verbose_name = 'تاريخ '

class Operation(models.Model):
     fund = models.ForeignKey(Fund,on_delete=models.CASCADE,verbose_name='الصندوق')
     customers = models.ForeignKey(Customers,on_delete=models.CASCADE,verbose_name='اسم العميل', null=True,blank=True)
     reservecha = models.ForeignKey(Reservecha,on_delete=models.CASCADE,verbose_name='الشاليه',null=True,blank=True)
     reserveape = models.ForeignKey(Reserveape,on_delete=models.CASCADE,verbose_name='الشقه',null=True,blank=True)
     pay_notice = models.TextField(null=True,verbose_name='ملاحظات')
     f_or = models.CharField(max_length=100,null=True,verbose_name='لأجل')
     recipient_name = models.CharField(max_length=100,null=True,verbose_name='اسم المستلم')
     pay_amountoutside = models.DecimalField(max_digits=10,decimal_places=2,null=True,verbose_name='المبلغ المنصرف',default=0.00)
     pay_amountinside = models.DecimalField(max_digits=10,decimal_places=2,null=True,verbose_name='المبلغ الوارد',default=0.00)
     pay_date  = models.DateField(default=datetime.now,verbose_name='التاريخ')
     add_datetme = models.DateTimeField(default=datetime.now,verbose_name='تاريخ ووقت الأضافه')
     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم', default='abdalrahman')

     def __str__(self): 
         return self.fund.fun_name
     
     class Meta:
         verbose_name_plural = 'العمليات'
         verbose_name = 'عمليه'
     


class Checkdetail(models.Model):
     content = models.ForeignKey(Content,on_delete=models.CASCADE,verbose_name='المحتوى')
     check1 = models.ForeignKey(Check,on_delete=models.CASCADE,verbose_name='الفحص')
     con_status = models.BooleanField(verbose_name='حاله المحتوى')  

     def __str__(self): 
         return self.con_status
     
     class Meta: 
       verbose_name_plural = 'تفاصيل الجرد'
       verbose_name = 'تفاصيل'
