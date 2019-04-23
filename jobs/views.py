from django.shortcuts import render

from .models import Job, Resume, Skills, Project, About, Education, Contact
def home(request):
    jobs = Job.objects
    skill = Skills.objects
    proj = Project.objects
    abt = About.objects
    edu = Education.objects
    cont = Contact.objects
    return render(request,'jobs/home.html',{'jobs': jobs,'skill': skill, 'abt': abt , 'proj': proj,'edu': edu,'cont':cont})

def resume(request):
    res = Resume.objects
    return render(request,'jobs/resume.html',{'res':res})

def info(request):


    return render(request,'jobs/home.html',{})

def blog(request):
    return render(request,'blog/allblogs.html',{})
