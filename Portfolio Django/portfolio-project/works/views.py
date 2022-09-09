from django.shortcuts import render, get_object_or_404
from .models import Job 


def home(request):
    jobs = Job.objects 
    return render(request, 'works/home.html', {'jobs' : jobs } )


def detail(request, Job_id):
    job_detail = get_object_or_404(Job, pk = Job_id)
    
    return render(request,'works/detail.html',{'Job': job_detail})