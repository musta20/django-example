from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from fristpy_app.models import Topic,webpage,accessrecord,testUser
from fristpy_app.forms import newUser , UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate , login , logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def ulogout(req):
  logout(req)
  return HttpResponseRedirect(reverse(index))

def index(req):

    web_list =  accessrecord.objects.order_by('date')
    insetme = {'access_rec':web_list,'text':'hello worled','number':100}

    return render(req,'fristapp/index.html',context = insetme)

def ulogin(req):
  if req.method == 'POST':
    print("iam in post")
    username = req.POST.get('username')
    password = req.POST.get('password')

    user = authenticate(req, username = username,password=password)

    if user:
      if user.is_active:
        login(req,user)
        return HttpResponseRedirect(reverse(index))
      else:
        return HttpResponseRedirect("ACCOUNT NOT ACTIVE")
    else:
      print("SOME MUTHER FUCKER TRY TO LOGIN AND FAILE")
      print("Username: {} and password {}".format(username,password))
      return HttpResponseRedirect("Invaled Login Detail Supplied")
  else:
      print("not in post")
      return render(req,'fristapp/login.html',{})



def sinup(req):

    sindup=False
    if req.method == 'POST':
       userForm = UserForm(data = req.POST)
       UserInfoForm = UserProfileInfoForm(data = req.POST)

       if userForm.is_valid() and UserInfoForm.is_valid():
         user = userForm.save()
         user.set_password(user.password)
         user.save()
         profilr = userForm.save(commit = False)
         profilr.user = user
         sindup = True
         if 'profile_pic'in req.FILES:
           profilr.profile_pic = req.FILES['profile_pic']
           profilr.save()
       else:
             print(userForm.error,UserProfileInfoForm.error)
    else:
      userForm = UserForm()
      UserInfoForm = UserProfileInfoForm()

    return render(req ,'fristapp/sinup.html',{'sineduo':sindup,'UserForm':userForm,'UserProfileInfoForm':UserInfoForm})


def base(req):
  return render(req,'fristapp/base.html')
  
def other(req):
  return render(req,'fristapp/other.html')


def realtiv_url(req):
  return render(req,'fristapp/realtiv_url.html')



def forms_view(req):
  #  form =  forms.formname()
    form = newUser()
    if req.method =='POST':
            form =  newUser(req.POST)
            if form.is_valid():
                form.save(commit = True)
                print(' fuck yeah i just savedit !!!! MOTHER FUCKER')
                print(form.cleaned_data['name'])
                print(form.cleaned_data['email'])


    return render(req,'fristapp/forms.html',{'form':form})



