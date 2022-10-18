from django.shortcuts import render,redirect
from Home.models import Employes, Company
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from django.core.files.storage import FileSystemStorage

from Home.form import ImageForm

#login to be implemented
def Homepage(request):
    
    return render(request,'index.html')
#dashboard when user login
def MainBoard(request):

    return render(request,"dashboard.html") 

#Add Employess
def Add_Customers(request):
    if request.method == 'POST':

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("dd")
            
            form.save()
            print("dds")
           
            print("ddss")

            img_obj = form.instance
            print("hh",img_obj)
            return redirect('CustomerTbl')
    else:
        form = ImageForm()
    return render(request, 'add_contact.html', {'form': form})   
#listing all employesss 
def ViewCustomers(request):
    print(request.method)  
    TblData={} 
    if request.method == "POST":    
        print(request.method)
        filterValue =request.POST.get('Ename')
        print("Ename",filterValue)
        emp = Employes.getCustomersByStatus(filterValue)
        print("filtdata",emp)
        TblData['user']=emp
        
        return render(request,"CustomersTbl.html",TblData)
    elif request.method == "GET":
        
        # users = paginator.page(paginator.num_pages)
        # print("users",users)
        Customers = Employes.showCustomers()
        # # user_list = User.objects.all()
        page = request.GET.get('page', 1)
        # print(page,"get meaya")
        paginator = Paginator(Customers, 5)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        
        
        # TblData['Customers']=Customers
        TblData['user']=users
        return render(request,"CustomersTbl.html",TblData)
#update employess on single click
def UpdateStatus(request):
    data={}
    
    
    if request.method == "POST":
        name = request.POST.get('name')
        city=request.POST.get('city')
        contactno=request.POST.get('contactno')
        status=request.POST.get('status')
        CustId = request.session['CustId']
        print("sa",name,status)
        print("post mr",CustId)
        # customer = CustomerRecord.getData(CustId)
        # print(customer)
        Customers = Employes.showCustomers()
        TblData={}
        TblData['user'] =Customers
        cust=Employes.objects.get(id=CustId)
        print("cus",cust.Status)
        cust.Status=status
        cust.save()
        return render(request,'CustomersTbl.html',TblData)    
    else:
        CustId=request.GET.get('custId')
        request.session['CustId']=CustId
        print('session',request.session['CustId'])
        customer = Employes.getData(CustId)
        print(customer)
        data['customer'] =customer
        print("id",CustId)
        print("customer",customer)
        print("else",request.method)
        return render(request,'UpdateData.html',data)