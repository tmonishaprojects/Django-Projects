from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults
import pickle


# Create your views here.


def predict(request):
    return render(request,'predict.html')


def predict_chances(request):

    if request.method=="POST":

        # Receive data from client
        skills = request.POST["skills"]
        print(skills)
        
        # Unpickle model
        model = pickle.load(open("E:/Advanced Data Science and Machine Learning/AI/NLP/Projects/Skill/skill_classification-20220712T151931Z-001/skill_classification/skill_app/skill.sav", "rb"))
        
        # Make prediction
        result = model.predict([skills])
        print(result)
        skill = skills
        classification = result

        obj=PredResults.objects.create(skill = skills,classification = result)
        obj.save()
        print(result)
        #print(skills)
        
        return render(request,'predict.html',{'result': classification,'skills':skills },)
                            



def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)      