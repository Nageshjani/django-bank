from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from bank_store.models import *
import json
import pandas as pd
from  django.db import transaction


def delete(request):
    bank=Bank.objects.get(id=60)
    Branch.objects.all().delete()

    return render(request,'data.html')





def data(request):
    df=pd.read_csv('static/bank_branches.csv')
    print(len(df))
    data=df['ifsc'][:100]
    
    df=df[:1000]
    ifsc_list=[]
    id_list=[]
    branch_list=[]
    address_list=[]
    city_list=[]
    district_list=[]
    state_list=[]

    

    
    for ifsc in df['ifsc']:
        ifsc_list.append(ifsc)

    for id in df['bank_id']:
        id_list.append(id)
    
    for branch in df['branch']:
        branch_list.append(branch)
    
    for add in df['address']:
        address_list.append(add)
    for city in df['city']:
        city_list.append(city)
    for dis in df['district']:
        district_list.append(dis)
    for state in df['state']:
        state_list.append(state)

    d=dict()
    print(len(ifsc_list),len(id_list),len(branch_list),len(address_list),len(city_list),len(district_list),len(state_list))
    
    with transaction.atomic():
        for i in range(len(id_list)):
            ifsc=ifsc_list[i]
            id=id_list[i]
            branch=branch_list[i]
            address=address_list[i]
            city=city_list[i]
            district=district_list[i]
            state=state_list[i]
            print(ifsc,id,branch,address,city,district,state)

            bank=Bank.objects.get(id=id)
            queryset1 = Branch.objects.create(ifsc=ifsc,bank_id=bank,branch=branch,address=address,
                                            city=city,district=district,state=state)  
            queryset1.save()
        
        
    
    
   

   

    
    
    


    return render(request,'data.html',{'data':data})




























def index(request):

    return render(request,'index.html')

def home(request):

    return render(request,'home.html')


def test(ifsc):
    branch=Branch.objects.get(ifsc=ifsc)
    return render('index.html',{'branch':branch})



def branchesData(request):
    data=json.loads(request.body)
    name=data['name']
    city=data['city']
    bank_id=Bank.objects.get(name=name).id

    print('bankid',bank_id)
    branches=Branch.objects.filter(bank_id=bank_id) & Branch.objects.filter(city=city)
    branch=branches[0]
    branches_list=[]
    for branch in branches:
        obj={
        'IFSC':branch.ifsc,
        'BRANCH':branch.branch,
        'CITY':branch.city,
        'DISTRICT':branch.district,
        'STATE':branch.state,
        'ADRESS':branch.address
        }
        branches_list.append(obj)
    
     

    
         
    return JsonResponse({'branches_list':branches_list},safe=False)

def ifsc(request):
    data=json.loads(request.body)
    print(data['ifsc'])
    branch=Branch.objects.get(ifsc=data['ifsc'])
    branch_obj={
        'IFSC':branch.ifsc,
        'BRANCH':branch.branch,
        'CITY':branch.city,
        'DISTRICT':branch.district,
        'STATE':branch.state,
        'ADRESS':branch.address

    }
    print('msg',branch_obj)

    
    return JsonResponse({'msg':branch_obj},safe=False)




def insert(request):
    queryset=Bank.objects.create(name='SBI',id=65)
    queryset.save()

    bank=Bank.objects.get(id=60)
    queryset1 = Branch.objects.create(ifsc='SBIN1212126',bank_id=bank,branch='vasnan',address='adress ahemdabad',city='Ahmedabad',district='ahmedabad',state='Gujrat')  
    
        
    queryset1.save()
    return render(request,'index.html')

