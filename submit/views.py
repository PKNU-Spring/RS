from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from social.models import Social_User_Table

import requests
import json



# =============상한-=============
from .forms import test

def submit(request):

    if request.method == "GET":

        user = request.session.get('user')
        
        if user :
            social_user = Social_User_Table.objects.get(pk=user)
            context = {'user' : social_user}
            return render(request, 'submit/submit.html', context)
        
        else :            
            return redirect('/')      

    elif request.method == "POST":
        """
        1. 페이지 내 데이터 받기
        2. 데이터 DB 반영
        3. 페이지 전환
        """

        

        # user = request.session.get('user')
        # print(user)

        html_user_nickname = request.POST.get('html_user_nickname','')
        print("html_user_nickname : ",html_user_nickname)
        print("asdsa")

        html_university = request.POST.get('html_university',None)
        print("html_university : " ,html_university)

        con = {}
        con['form']=test()


        html_contact = request.POST.get('html_contact')
        print("html_contact : ",html_contact)

        html_image = request.POST.get('html_image')
        print("html_image : ",html_image)

        html_preference = request.POST.get('html_preference','')
        print("html_preference : ",html_preference)

        html_Q01 = request.POST.get('html_Q01')
        print("html_Q01 : ",html_Q01)




        # social_user = Social_User_Table.objects.get(pk=user)

        # Social_User_Table(
        #         user_id         = user,
        #         contact         = html_data,
        #     ).save()
        

        
        print("post fin")

        return redirect('/status')