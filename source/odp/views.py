# Create your views here.
from django.shortcuts import render
from django.db import IntegrityError
from .models import ProcessCatalogue,ProcessGroup
from django.conf import settings
from .forms import ProcessGroupForm,ProcessCatalogueForm
from django.core.paginator import Paginator
import math
from django.shortcuts import get_object_or_404


def corecontext(dict):
    dict['site_brand_name']=settings.SITE_BRAND_NAME
    return dict


def index(request):
    context={}
    context=corecontext(context)
    return render(request, 'odp/base.html', context)


def create_job(request):
    context={}
    context=corecontext(context)
    return render(request, 'odp/create_job.html', context)

def process_list(request):
    #use paginator to show the groups of the processes
    parent_group = request.GET.get('parentgroup',0)
    
    if(parent_group==0):
        context={}
        context=corecontext(context)
        return render(request, 'odp/process_list.html', context)    
    
    procs_list=ProcessCatalogue.objects.filter(group_id__group_name=parent_group)
    paginate_value=1
    procs_paginator = Paginator(procs_list, paginate_value) 
    page_number = request.GET.get('page',1)
    page_obj = procs_paginator.get_page(page_number)
    procs=[]
    for proc in page_obj:
        procs.append(
            {
                "name":proc.process_name,
                "description":proc.process_description,
                "id":proc.process_id,
            }
        )
    
    context = {
        "procs_list":procs,
        "next_page":int(page_number)+1,
        "previous_page":int(page_number)-1,
        "page_number":int(page_number),
        "max_pages":math.ceil(procs_paginator.count/paginate_value),
        "parent_group":parent_group,
    }
    print(procs_list)
    context=corecontext(context)

    return render(request, 'odp/process_list.html', context)
    
def group_list(request):

    
    #use paginator to show the groups of the processes
    groups_list= ProcessGroup.objects.filter()
    paginate_value=10
    groups_paginator = Paginator(groups_list, paginate_value) 
    page_number = request.GET.get('page',1)
    page_obj = groups_paginator.get_page(page_number)
    groups=[]
    for group in page_obj:
        groups.append(
            {
                "name":group.group_name,
                "description":group.group_description,
                "id":group.id,
            }
        )
    
    context = {
        "groups_list":groups,
        "next_page":int(page_number)+1,
        "previous_page":int(page_number)-1,
        "page_number":int(page_number),
        "max_pages":math.ceil(groups_paginator.count/paginate_value)
    }
    print(groups_list)
    context=corecontext(context)

    return render(request, 'odp/group_list.html', context)

def create_process(request):
    context={}
    if(request.method=='GET'):
        mymapid = request.GET.get('processid',"none")
        print(mymapid)
        if(str(mymapid)=='none'):
                form=ProcessCatalogueForm()
                restart_form=0
        else:
            proc= get_object_or_404(ProcessCatalogue,process_id=mymapid)
            
            print(proc.__dict__)
            form=ProcessCatalogueForm(initial=proc.__dict__)
            restart_form=0
    # restart_form=1
    if(request.method=='POST'):
        form = ProcessCatalogueForm(request.POST)
        if form.is_valid():
            form.save()
            form.success='Process succesfully created'
            restart_form=0
        else:
            print('form is invalid')
            restart_form=0
                
    if(restart_form==1):
        context={
            'form':ProcessCatalogueForm
        }
    else:
        context={
            'form':form
            }

    context=corecontext(context)
    return render(request, 'odp/create_process.html', context)

def create_group(request):
    context={}
    if(request.method=='GET'):
        mymapid = request.GET.get('groupid',"none")
        if(str(mymapid)=='none'):
                form=ProcessGroupForm()
                restart_form=0
        else:
            group_obj= get_object_or_404(ProcessGroup,id=mymapid)
            populate={
                'group_name':group_obj.group_name,
                'group_description':group_obj.group_description,
            }
            
            form=ProcessGroupForm(initial=populate)
            restart_form=0
    
    if(request.method=='POST'):
        restart_form=1
        form=ProcessGroupForm(request.POST)
        form.non_field_errors=[]
        if(form.is_valid()):
            data=form.cleaned_data
            group_new=ProcessGroup()
            try:
                group_new.group_name=data['group_name']
                group_new.group_description=data['group_description']
                group_new.save()
                form.success='Group succesfully created'
                restart_form=0
            except IntegrityError as e:
                form.non_field_errors.append('Group Name already exsists.')
                restart_form=0
            except Exception as e:
                print(e)
                form.non_field_errors.append('Error occured while saving form try lter')
                restart_form=0

        else:
            print('form is invalid')
            restart_form=0
    if(restart_form==1):
        context={
            'form':ProcessGroupForm
        }
    else:
        context={
            'form':form
            }
    context=corecontext(context)
    return render(request, 'odp/create_group.html', context)