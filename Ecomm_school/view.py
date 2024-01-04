from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .form import userForm
from service.models import Service
from news.models import News
from serviceDataFilter.models import ServicesDataFilter
from django.core.paginator import Paginator
from courseenquiry.models import courseenquiry

def homePage(request):
    newsData=News.objects.all()    
    data={
        'title':'Home Page',
        'heading':'Welcome to our website',
        'list':['C','C++','django','php'],
        'numbers':[10,20,30,40,50,60,70],
        'student_details':[
            {'name':'visu','age':20},
            {'name':'Jane','age':12},        
            {'name':'divesh','age':25},        
        ],

        'newsData':newsData,
    }
    return render(request,'index.html',data)
def newsDetails(request,slug):
    newsDetails = News.objects.get(new_slug=slug)
    data={
        'newsDetails':newsDetails,
    }
    return render(request,'newsDetails.html',data)

def submitform(request):
    if request.method=='POST':
        finalresult=0
        data={}
    try:
        if request.method=="POST":

           n1=int(request.POST.get('num1'))
           n2=int(request.POST.get('num2'))
           finalresult=n1+n2
           data={
               'n1':n1,
               'n2':n2,
               'output':finalresult

           }
          
           return HttpResponse(finalresult)
        

    except:
        error='Please enter a value in form error......'
    return HttpResponse(error)
         
def about(request):
    # get data table from django method objects.all()
    # order_by Query ascending and (-)descending 
    # limitation query of slice [:limit_numberf]
    servicesData=Service.objects.all().order_by('id')[:3]
    if request.method=="GET":
        output=request.GET.get('output')
    data={
        'output':output,        
        'servicesData':servicesData
    }  
    #data send django to html page              
    return render( request,'about.html',data)
def course(request):
    return render( request,'course.html')
def saveEnquiry(request):
      message=''
      if request.method == 'POST':
         name = request.POST.get('name')
         email = request.POST.get('email')
         phone = request.POST.get('phone')
         website = request.POST.get('website')
         message = request.POST.get('message')         
         en=courseenquiry(name=name ,email=email ,phone=phone ,websiteLink=website ,message=message)
         en.save()
         message="Your Message has been sent Successfully"
        
      return render( request,'course.html',{'message':message})
def servicesData(request):
    servicesFilter=ServicesDataFilter.objects.all()
    paginator=Paginator(servicesFilter,2)
    page_number=request.GET.get('page')
    servicesPageInfo=paginator.get_page(page_number)
    totalpage=servicesPageInfo.paginator.num_pages
    # if request.method == "GET":
    #    st = request.GET.get("servicename")
    #    if st!=None:
    #     servicesFilter=ServicesDataFilter.objects.filter( servicesDataFilter_title__icontains=st)
    data={
        "servicesFilter":servicesPageInfo,
        "lastpage":totalpage,
        "totalpagelist":[n+1 for n in range(totalpage)]
        }
    return render( request,'servicesData.html',data)
def user(request):
    return render(request,'user.html')
def main(request):
    return render(request,'main.html')

def signup(request):
    finalresult=0
    fn=userForm()
    data={'forms':fn}
    # try and except use for error handle 
    try:
        # data Sent by POST method goes through HTTP header so security depends on http protocol
        if request.method=="POST":

           n1=int(request.POST.get('num1'))
           n2=int(request.POST.get('num2'))
           finalresult=n1+n2
           data={
               'forms':fn,
               'output':finalresult,
               
           }
           url='/about/?output={}'.format(finalresult)
           return redirect(url)
    except:
        pass    
    return render(request,'signup.html',data)

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def calculator(request):
    result=''
    data={}
    try:
        if request.method == "POST":
            num1 = eval(request.POST['num1'])
            num2 = eval(request.POST['num2'])
            opr  = request.POST['opr']
            if opr=='+':
               result=num1 + num2
            elif opr=='-':
               result=num1 - num2
            elif opr=='*':
               result=num1 * num2
            elif opr=='/':
               result=num1 / num2
               
            data={
                'n1':num1,
                'n2':num2,
                'opr':opr,         
                'result':result,
             }

    except:
          result='Invalid opr.....' 
    return render(request,"calculator.html",data)

def marksheet(request):
    div=''
    t=''
    p=''
    if request.method=="POST":
       if request.POST.get('subject1')=="":
           return render(request,'marksheet.html',{'error':True})
       elif request.POST.get('subject2')=="":
           return render(request,'marksheet.html',{'error':True})
       elif request.POST.get('subject3')=="":
           return render(request,'marksheet.html',{'error':True})
       elif request.POST.get('subject4')=="":
           return render(request,'marksheet.html',{'error':True})
       elif request.POST.get('subject5')=="":
           return render(request,'marksheet.html',{'error':True})
            
       s1=eval(request.POST.get('subject1')) 
       s2=eval(request.POST.get('subject2')) 
       s3=eval(request.POST.get('subject3')) 
       s4=eval(request.POST.get('subject4')) 
       s5=eval(request.POST.get('subject5')) 
       t = s1+s2+s3+s4+s5
       p = (t*100)/500
       if p>=80:
            div = 'First division' 
       elif p>=60:
            div = 'Second division'
       elif p>=40:
            div = 'Third division'
       elif p>=30:
            div = 'Fourth divsion'
       else:
            div = 'Fail'
       data={
           'total':t,
           'percentage':p,
           'division':div,          
       }  
 
       return render(request,'marksheet.html',data)            
    return render(request,'marksheet.html')            

def evenodd(request):
    res=''
    context={}
    try:
        if request.method=="POST":                
           n1=eval(request.POST.get('num1'))
           if n1%2==0:
            res='Even Number'
        else:
            res='Odd Number'
    except:
        error='Please enter a number'
        context={'res':res,
                 'error':error
                 }
        
    return render(request,'evenodd.html',context)

  