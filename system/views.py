from django.shortcuts import render, redirect , get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .form import *
from django.http import JsonResponse, HttpResponse
from datetime import date, timedelta
from django.core.serializers import json
from django.contrib.auth.decorators import login_required
from django import template
from django.contrib.auth.models import Group
from django.shortcuts import render , get_object_or_404
import qrcode
from io import BytesIO
import base64






# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user.groups.filter(name="acc"):
               return redirect('acc')
            elif user.groups.filter(name="res"):
                 return redirect('donebookings')
            elif user.groups.filter(name="ser"):
                 return redirect('services')
            else:
                return redirect('index')
        else:
            messages.error(request, 'Username or password invalid')

        return redirect('login')  

    else:  
      return render(request, 'pages/login.html')



def index(request):
    user = request.user
    group = user.groups.all()
    apart_mint = {
        'apart': Apartments.objects.all(),
        'chali': Chalets.objects.all(),
        'gr':group,
        'u':user,
    }
    return render(request, 'pages/index.html', apart_mint)

def acc(request):
    user = request.user
    group = user.groups.all()
    apart_mint = {
        'gr':group,
        'u':user,
    }
    return render(request, 'pages/accounts/acc.html', apart_mint)

def expenses(request):
    user = request.user
    group = user.groups.all()
    inc = {
        'form': ac(),
        'gr':group,
        'u':user,
    }
    if request.method == 'POST':
       fund = int (request.POST.get('fund'))
       pay_date = request.POST.get('pay_date')
       pay_amountoutside = request.POST.get('pay_amountoutside')
       user = User.objects.get(username='abdalrahman')
       recipient_name = request.POST.get('recipient_name')
       f_or = request.POST.get('f_or')
       pay_notice = request.POST.get('pay_notice')
       opera = Operation(
           fund_id = fund,
           pay_notice = pay_notice,
           pay_amountoutside = pay_amountoutside,
           pay_date = pay_date,
           recipient_name = recipient_name,
           f_or = f_or,
           user = user 
       )
       opera.save()
       return redirect('acc')
    return render(request, 'pages/accounts/expenses.html', inc)

def income(request):
    user = request.user
    group = user.groups.all()
    inc = {
        'form': ac(),
        'gr':group,
        'u':user,
    }
    if request.method == 'POST':
       fund = int (request.POST.get('fund'))
       pay_date = request.POST.get('pay_date')
       pay_amountinside = request.POST.get('pay_amountinside')
       reservecha = request.POST.get('reservecha')
       reserveape = request.POST.get('reserveape')
       user = int (request.POST.get('user'))
       customers = int (request.POST.get('customers'))
       pay_notice = request.POST.get('pay_notice')
       opera = Operation(
           fund_id = fund,
           customers_id = customers,
           reservecha_id = reservecha,
           reserveape_id = reserveape,
           pay_notice = pay_notice,
           pay_amountinside = pay_amountinside,
           pay_date = pay_date,
           user_id = user 
       )
       opera.save()
       return redirect('bills')
   
        
        
    return render(request, 'pages/accounts/income.html', inc)

def cuscha(request):
    idresch = request.GET.get('idresch')
    idr = Reservecha.objects.get(id=idresch)
    data = {
       'cname':idr.customers.id,
       'cename':idr.customers.cus_name
    }
    return JsonResponse(data)

def cusapa(request):
    idresap = request.GET.get('idresap')
    idr = Reserveape.objects.get(id=idresap)
    data = {
       'cname':idr.customers.id
    }
    return JsonResponse(data)

def mortgaga(request):
    user = request.user
    group = user.groups.all()
    if request.method == 'POST':
      fund = Fund.objects.get(id=3)
      reservecha = int(request.POST.get('reservecha'))
      mor_date = request.POST.get('mor_date' )
      mor_type = request.POST.get('mor_type')
      mor_amaunt = request.POST.get('mor_amaunt')
      mor_notice = request.POST.get('mor_notice')
      user = User.objects.get(username='abdalrahman')
      mor_data = Mortgage(fund=fund,
                           reservecha_id =reservecha ,
                           mor_date=mor_date,
                           mor_type=mor_type,
                           mor_amaunt=mor_amaunt,
                           mor_notice=mor_notice,
                           user=user)
      
      mor_data.save()  
      return redirect('mor')
    co = {
        'form':mo(),
        'gr':group,
        'u':user,
    }
    return render(request, 'pages/accounts/mortgaga.html', co)

def client(request):
    user = request.user
    group = user.groups.all()
    custo_mers = {
        'custo': Customers.objects.all(),
        'gr':group,
        'u':user,
        
    }
    return render(request, 'pages/client/client.html', custo_mers)


def clientdata(request):
    user = request.user
    group = user.groups.all()
    if request.method == 'POST':
      cli_fullname = request.POST.get('cli_fullname')
      cli_phone = request.POST.get('cli_phone')
      cli_address = request.POST.get('cli_address' )
      nationality = request.POST.get('nationality')
      cli_age = request.POST.get('cli_age')
      cli_id_number = request.POST.get('cli_id_number')
      user = User.objects.get(username='abdalrahman')
      cli_data = Customers(cus_name=cli_fullname,
                           cus_card_id=cli_id_number ,
                           cus_phone_number=cli_phone,
                           cus_address=cli_address,
                           cus_age=cli_age,
                           cus_gender=nationality,
                           user=user)
      
      cli_data.save()  
      return redirect('index')                                 
    return render(request, 'pages/client/clientdata.html', {'gr':group, 'u':user,})

def st_mor(request, id):
    Mortgage.objects.filter(id=id).update(mor_status=True)
    messages.success(request, "تم التسليم") 
    return redirect('mor')
     
     

def apdateclientdataa(request, id):
    user = request.user
    group = user.groups.all()
    query = Customers.objects.get(id=id)
    context = {'object':query,
               'gr':group, 'u':user,}
    if request.method == 'POST':
      cli_fullname = request.POST.get('cli_fullname')
      cli_phone = request.POST.get('cli_phone')
      cli_address = request.POST.get('cli_address')
      nationality = request.POST.get('nationality')
      cli_age = request.POST.get('cli_age')
      cli_id_number = request.POST.get('cli_id_number')

      query.cus_name = cli_fullname
      query.cus_phone_number = cli_phone
      query.cus_address = cli_address
      query.cus_gender = nationality
      query.cus_age = cli_age
      query.cus_card_id = cli_id_number 
      query.save()
      return redirect('client')  
    return render(request, 'pages/client/apdateclientdataa.html', context)

def services(request):
    user = request.user
    group = user.groups.all()
    return render(request, 'pages/service/services.html',{'gr':group, 'u':user,})

def done_tasks(request):
    user = request.user
    group = user.groups.all()
    context = {
        'chali': Chalets.objects.all(),
        'gr':group, 'u':user,
    }
    return render(request, 'pages/service/done_tasks.html', context)

def tasks(request):
    user = request.user
    group = user.groups.all()
    context = {
        'chali': Chalets.objects.all(),
        'gr':group, 'u':user,
    }
    return render(request, 'pages/service/tasks.html', context)

def contents(request, id):
    user = request.user
    group = user.groups.all()
    context = {
        'con': Content.objects.all().filter(chalit=id),
        'gr':group, 'u':user,
    }
    return render(request, 'pages/service/contents.html', context)

def apartment_book(request, id):
    user = request.user
    group = user.groups.all()
    apa_cus = {
        'apacus': Customers.objects.all(),
        'bookap': Apartments.objects.get(id=id),
        'form': apbook({'apartments':id}),
        'gr':group, 'u':user,
    }
    if request.method == 'POST':
        log_date = request.POST.get('login_date')
        exi_date = request.POST.get('exit_date')
        ld = datetime.strptime(log_date, "%Y-%m-%d").date()
        ed = datetime.strptime(exi_date, "%Y-%m-%d").date()
        da_list = ran(ld, ed)    
        for date in da_list:       
           da_save = Resapa_date(
               apartments=Apartments.objects.get(id=id),
               res_date=date 
           )
           da_save.save()  
        addbook = apbook(request.POST)
        if addbook.is_valid():
            addbook.save()
            return redirect('index')       
    return render(request, 'pages/booking/apartment_book.html', apa_cus)

def validateresapa(request):        
    resdate = request.GET.get('resdate')  
    apaid = request.GET.get('apaid') 
    today = date.today() 
    valid_resdate = Resapa_date.objects.filter(res_date=resdate,apartments=apaid).exists()   
    data = {'valid_resdate':valid_resdate,
            'today':today}  
    return JsonResponse(data)  


##########

def ran(oo,yy):
    cur = oo
    while cur <= yy:
        yield cur
        cur +=  timedelta(days=1)


today = date.today()
Reservecha.objects.filter(res_cha_date__lt=today).update(st_book='done')
Reserveape.objects.filter(exit_date__lt=today).update(st_book='done')
    
   
##########    
    
def chalih_book(request, id):
    user = request.user
    group = user.groups.all()
    cha_cus = {    
        'bookch': Chalets.objects.get(id=id),
        'bunc' : Bunch.objects.all(),   
        'form': chbook({'chalits':id }), 
        'gr':group, 'u':user,    
    }
    if request.method == 'POST':
        addbook = chbook(request.POST)
        if addbook.is_valid():
            addbook.save()
            return redirect('chalih_bookings')

    return render(request, 'pages/booking/chalih_book.html', cha_cus)

def validate(request):
    idbunch = request.GET.get('idbunch')
    idb = Bunch.objects.get(id=idbunch)
    data = {'pr':idb.bun_price,
            'en':idb.bun_entrytime,
            'ex':idb.bun_exittime,
            }
    return JsonResponse(data)

def validaterescha(request):        
    resdate = request.GET.get('resdate')
    chaid = request.GET.get('chaid')
    today = date.today()    
    valid_resdate = Reservecha.objects.filter(res_cha_date=resdate,chalits=chaid).exists()   
    data = {'valid_resdate':valid_resdate,
            'today':today}  
    return JsonResponse(data)   



def chalih_people(request, id):
    user = request.user
    group = user.groups.all()
    bun = Reservecha.objects.get(id=id)
    peo = People.objects.filter(reservecha=id).count()
    peo_bun_num = bun.bunch.bun_people_number
    chpe = {
        'bookch': Reservecha.objects.get(id=id),
        'form':Peoplech({'reservecha':id }),
        'peo':People.objects.all().filter(reservecha=id),
        'gr':group, 'u':user,  
    }
    if request.method == 'POST':
        addpeo = Peoplech(request.POST)
        if addpeo.is_valid():
            if peo_bun_num != peo:
               addpeo.save()
            
        
    return render(request, 'pages/booking/chalih_people.html', chpe)

def donebookings(request):
    user = request.user
    group = user.groups.all()
    return render(request, 'pages/doneBookings/donebookings.html',{'gr':group, 'u':user,})

def chalih_bookings(request):
    user = request.user
    group = user.groups.all()
    today = datetime.today().date()
    cha = {
       'resch': Reservecha.objects.filter(res_cha_date__gte=today).order_by('-id'),
        'gr':group, 'u':user,
    }
    return render(request, 'pages/doneBookings/chalih_bookings.html', cha)

def apartment_bookings(request):
    user = request.user
    group = user.groups.all()
    today = datetime.today().date()
    apa = {
        'resapa':Reserveape.objects.filter(exit_date__gte=today).order_by('-id'),
        'gr':group, 'u':user,
    }
    return render(request, 'pages/doneBookings/apartment_bookings.html', apa)

def apdate_apartment_book(request, id):
    user = request.user
    group = user.groups.all()
    book_id = Reserveape.objects.get(id=id)
    if request.method == 'POST':
        book_save = apbook(request.POST, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('apartment_bookings')
    else:
        book_save = apbook(instance=book_id)
    total = Operation.objects.filter(reserveape=id)
    
    context = {
        'form': book_save,
        'sum': total,
        'gr':group, 'u':user,
    }            
    return render(request, 'pages/doneBookings/apdate_apartment_book.html', context)

def apdate_chalih_book(request, id):
    user = request.user
    group = user.groups.all()
    book_id = Reservecha.objects.get(id=id)
    if request.method == 'POST':
        book_save = chbook(request.POST, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('chalih_bookings')
    else:
        book_save = chbook(instance=book_id)
    context = {
        'form': book_save,
        'gr':group, 'u':user,
    }            
    return render(request, 'pages/doneBookings/apdate_chalih_book.html', context)

def get_dates(request):
    apid = request.GET.get('apid')
    idc= str ( Reserveape.objects.filter(apartments=apid).values('login_date','exit_date'))
    lll = idc.maketrans(",","-",")} {'gin_date': datetime.date(QuryS[<>]")
    today = date.today()
    mm = Reserveape.objects.filter(login_date=today,apartments=apid).exists()
    data = {'da':idc.translate(lll),
             'xx':mm,
             'apid':apid}
    return JsonResponse(data)
    
    

def bill(request, id):
    context = {
        'bill': Firm.objects.get(),
        'con': Operation.objects.get(id=id),
    }
    return render(request, 'pages/report/bill.html', context)

def reports(request):
    user = request.user
    group = user.groups.all()
    return render(request, 'pages/report/reports.html', {'gr':group, 'u':user,})

def bills(request):
    user = request.user
    group = user.groups.all()
    context = {
        'ta_bill': Operation.objects.all().filter(pay_amountinside__gt = 1).order_by('-id'),
        't_bill': Operation.objects.all().filter(pay_amountoutside__gt = 1).order_by('-id'),
        'gr':group, 'u':user,
    }
    return render(request, 'pages/report/bills.html', context)

def out(request, id):
    context = {
        'b': Firm.objects.get(),
        'c': Operation.objects.get(id=id),
    }
    return render(request, 'pages/report/out.html', context)

def report(request):
    user = request.user
    group = user.groups.all()
    if request.method == 'POST':
      r_fund = request.POST.get('r_fund')
      re_type = request.POST.get('re_type')
      s_date = request.POST.get('s_date')
      e_date = request.POST.get('e_date')
      r_cus = request.POST.get('r_cus')
      global repoacc 
      global repocus_c 
      global repocusname_c
      global repocus_a
      global reserve_c
      global reserve_a
      if re_type == "ac":
         repoacc =  Operation.objects.all().filter(fund=r_fund)   
         return redirect('acc_records')  
      elif re_type == "cl":     
           repocusname_c =  Customers.objects.get(id=r_cus) 
           repocus_c =  Reservecha.objects.all().filter(customers=r_cus)    
           repocus_a =  Reserveape.objects.all().filter(customers=r_cus)
           if Reservecha.objects.filter(customers=r_cus).exists() or Reserveape.objects.filter(customers=r_cus).exists():
              return redirect('customer_record')
           else:
              return HttpResponse("Not found")
      else:    
         reserve_c = Reservecha.objects.all()
         reserve_a = Reserveape.objects.all()
         return redirect('rent_records')
      
    context = {
        'cus':Customers.objects.all(),
        'gr':group, 'u':user,
    }
    return render(request, 'pages/report/report.html', context)

def acc_records(request):
    context = {
        'repo':repoacc,
    }
    return render(request, 'pages/report/acc_records.html', context)

def customer_record(request):
    
    context = {
        'repo_c':repocus_c,
        'name':repocusname_c,
        'repo_a':repocus_a,
      }
     
    return render(request, 'pages/report/customer_record.html', context)

def rent_records(request):
    context = {
        'reserve_c':reserve_c,
        'reserve_a':reserve_a,
      }
    return render(request, 'pages/report/rent_records.html', context)

def book_cha(request):
    user = request.user
    group = user.groups.all()
    context ={
        'form': chbook(), 
        'gr':group, 'u':user,
    }
    return render(request, 'pages/booking/book_cha.html', context)

def daterescha(request):
    resdate = request.GET.get('resdate')
    not_equal = Reservecha.objects.filter(res_cha_date=resdate).values('chalits')
    data ={'eq':str(not_equal)}
    return JsonResponse(data)

def book_apa(request):
    user = request.user
    group = user.groups.all()
    con = {
        'form': apbook(),
        'gr':group, 'u':user,
    }
    return render(request, 'pages/doneBookings/book_apa.html', con)

def validate_card (request):
    apid = request.GET.get('apid')
    today = date.today()
    mm = Resapa_date.objects.filter(res_date=today,apartments=apid).exists() 
    data = {'xx':mm,
             'apid':apid}  
    return JsonResponse(data)  

def validate_card2 (request):
    chid = request.GET.get('chid')
    today = date.today()
    nn = Reservecha.objects.filter(res_cha_date=today,chalits=chid).exists() 
    data = {'zz':nn,
             'chid':chid}  
    return JsonResponse(data) 

def print_card(request, id):
    reservation = get_object_or_404(Reservecha, id=id)
    people = People.objects.filter(reservecha=reservation)
    # توليد الباركود لكل شخص
    barcodes = []
    for person in people:
        person_id = person.id  # جلب معرف الشخص
        person_name = person.peo_name
        person_identity = person.peo_card_number
        person_age = person.peo_age
        data = f"{person_id}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        # حفظ QR Code كصورة في الذاكرة
        img = qr.make_image(fill='black', back_color='white')
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        # تحويل الصورة إلى base64
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        barcodes.append({
            'name': person_name,
            'barcode': image_base64,
        })
    context = {
        'barcodes': barcodes,
    }
    return render(request, 'pages/doneBookings/print_card.html', context)

def check_people(request):
    user = request.user
    group = user.groups.all()
    today = date.today()
    rescha = Reservecha.objects.filter(res_cha_date=today)
    context = {
        'rescha': rescha,
        'gr':group, 'u':user,
    }
    return render(request, 'pages/service/check_people.html', context)

def entering_people(request, booking_id):
    booking = get_object_or_404(Reservecha, id=booking_id)
    peo = People.objects.filter(reservecha=booking, st_people='enter')
    user = request.user
    group = user.groups.all()
    context = {
        'booking': booking,
        'peo': peo,
        'gr': group,
        'u': user,
    }
    return render(request, 'pages/service/entering_people.html', context)


def save_person(request):
    personId = request.GET.get('personId')
    rid = request.GET.get('rid')
    People.objects.filter(id=personId,reservecha=rid).update(st_people='enter')
    chick = People.objects.filter(id=personId,reservecha=rid).exists()
    data = {'ch':chick}
    return JsonResponse(data)

def settings(request):
    user = request.user
    group = user.groups.all()
    return render(request, 'pages/settings.html',{ 'gr': group,'u': user,})

def mor(request):
    user = request.user
    group = user.groups.all()
    today = date.today()
    context ={
        'mor':Mortgage.objects.all().filter(mor_date__gte=today, mor_status=False),
        'gr': group,'u': user,
    }
    return render(request, 'pages/accounts/mor.html', context)
    