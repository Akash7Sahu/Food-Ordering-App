from django.shortcuts import render,redirect
from zappyapp.forms import SignupForm
from zappyapp.models import Item,Cart,Ordernow
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.views.generic import View,TemplateView,ListView,DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.models import User

from django.http import JsonResponse

def CheckUser(request):
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    u=request.GET.get('user')
    print("Username>>>>>>>>",u)
    data = {
        'is_taken': User.objects.filter(username__iexact=u).exists()
        }
    print(data)
    return JsonResponse(data)

# Create your views here.
def index(request):
	return render(request,'zappyapp/index.html')

'''def signup(request):
    sform=Signupform(request.POST or None)
    if sform.is_valid():
        new_user = authenticate(username=sform.cleaned_data['username'],password=sform.cleaned_data['password1'])
        login(request, new_user)
        return HttpResponseRedirect(reverse('home'))
    return render(request,'zappyapp/signup.html',{'sform':sform})'''

def login(request):
	return render(request,'zappyapp/login.html')

def signup(request):
	if request.method=='GET':
		sform=SignupForm()
		return render(request,"zappyapp/signup.html",{'sform':sform})
	if request.method=='POST':
		sform=SignupForm(request.POST)
		if sform.is_valid():
			user=sform.save()
			user.set_password(user.password)
			user.save()
			sform=SignupForm()
			subject='Django Email subject'
			message='Thank you for registering to Zappy'
			email_from=settings.EMAIL_HOST_USER
			recipient_list=[user.email,]
			send_mail(subject,message,email_from,recipient_list)
			mydict={'msg':'Registration Success...','sform':sform}
		return HttpResponseRedirect(reverse('home'))
	return render(request,"zappyapp/signup.html",context=mydict)


class item_list(ListView):
	model=Item


def addcart(request):
	user=request.user
	pname=request.POST.get('qname')
	pid=request.POST.get('qid')
	pic=request.POST.get('qpic')
	quan=request.POST.get('quantity')
	price=request.POST.get('qprice')
	Total=float(quan)*float(price)
	Cart.objects.get_or_create(pid=pid,quantity=quan,price=price,user=user,total=Total,name=pname,pic=pic)
	msg='Items Added Successfully'
	mydict={'msg':msg}
	return render(request,'zappyapp/item_list.html',context=mydict)

def viewcart(request):
	cart=Cart.objects.all()
	return render(request,'zappyapp/cart.html',{'cart':cart})

def updatecart(request):
    up_pid=request.POST.get('pid')
    up_quantity=request.POST.get('quant')
    up_price=request.POST.get('price')
    up_total=float(up_quantity)*float(up_price)
    Cart.objects.filter(pid=up_pid).update(quantity=up_quantity,price=up_price,total=up_total)
    cart=Cart.objects.all()
    return render(request,'zappyapp/cart.html',{'cart':cart})

def order_list(request):
	order=Cart.objects.all()
	for c in order:
		name=c.name
		price=c.price
		quantity=c.quantity
		Total=c.total
		Ordernow.objects.get_or_create(Quantity=quantity,price=price,Total=Total,name=name)
		c.delete()
	order=Ordernow.objects.all()
	return render(request,'zappyapp/order.html',{'order':order})

def ItemDelete(request,k):
	c=Cart.objects.get(id=k)
	c.delete()
	return render(request,'zappyapp/item_list.html',{'del':'Item Deleted Successfully'})


def email(request):
	subject='Django Email subject'
	message='Thank you for registering to Zappy'
	email_from=settings.EMAIL_HOST_USER
	recipient_list=['nitingour99@gmail.com',]
	send_mail(subject,message,email_from,recipient_list)
	return redirect('')
