from django.shortcuts import render
from bs4 import BeautifulSoup 
import requests

def Home(request):

    return render(request,'index.html')

def nepal(request):
    if request.method == 'POST':
        try:
            district=request.POST['district']
            res = requests.get("https://kathmandupost.com/covid19")
            soup = BeautifulSoup(res.text, 'lxml')
            index = -1
            data=soup.select('tr td')
            for i in range(len(data)):
                if data[i].text.lower()==district.lower():
                    index=i
                    break
            if(index==-1):
                err=str("Please enter the correct district name")
                view={'err':err}
                return render(request,'nepal.html',view)
            else:     
                for i in range(4):
                    if i == 0:
                        dname=data[i+index].text
                    elif i == 1:
                        Total_cases=data[i+index].text
                    elif i == 2:
                        Total_deaths=data[i+index].text
                    elif i==3:
                        Recovered=data[i+index].text
                        Active=int(Total_cases)-int(Total_deaths)-int(Recovered)
                context_view = {'dname':dname,'Total':Total_cases,'Deaths':Total_deaths,'Recovered':Recovered,'Active':Active}
                
                return render(request,'nepal.html',context_view)
        except ConnectionError:
            errs=str("Please connect to internet")
            viiew={'errs':errs}
            return render(request,'nepal.html',viiew)
    return render(request,'nepal.html')

def world(request):
    if request.method == 'POST':
        country=request.POST['country']
        res = requests.get("https://www.worldometers.info/coronavirus/#countries")
        soup = BeautifulSoup(res.text, 'lxml')
        index = -1
        data=soup.select('tr td')
        for i in range(len(data)):
            if data[i].text.lower()==country.lower():
                index=i
                break
        if(index==-1):
            errr=str("Please enter the correct country name")
            viewss={'errr':errr}
            return render(request,'world.html',viewss)
        else:     
            for i in range(6):
                if i == 0:
                    cname=data[i+index].text
                elif i == 1:
                    TotalCases=data[i+index].text
                elif i == 2:
                    NewCases=data[i+index].text
                elif i == 3:
                    TotalDeaths=data[i+index].text
                elif i == 4:
                    NewDeaths=data[i+index].text
                else:
                    Recovereds=data[i+index].text
                    Active=int(TotalCases.replace(',', ''))-int(TotalDeaths.replace(',', ''))-int(Recovereds.replace(',', ''))
                    
            context_views = {'cname':cname,'TotalCases':TotalCases,'NewCases':NewCases,'TotalDeaths':TotalDeaths,'NewDeaths':NewDeaths,'Recovereds':Recovereds,'Active':Active}
            
            return render(request,'world.html',context_views)
    return render(request,'world.html')
   
    