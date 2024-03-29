from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.shortcuts import render, redirect

from social.models import Social_User_Table
from main.models import Registered_User_Table
from .models import Query_Table
from config.settings import LAST_DATE, THIS_DATE, NEXT_DATE

@csrf_protect
def submit(request):
    
    session_user_info = request.session.get('user_info')

    # RDB 사용자 데이터 존재
    if Registered_User_Table.objects.filter(user_id=session_user_info.get('user_id')).exists():
        recent_matching_user = Registered_User_Table.objects.get(user_id=session_user_info.get('user_id'))
        # RDB 매칭 날짜가 최근 날짜
        if recent_matching_user.recent_matching_date == LAST_DATE:
            return redirect('/status')

    if request.method == "GET":

        # 거절당한 사람 정보 지우고 다시 등록
        if Social_User_Table.objects.filter(user_id=session_user_info.get('user_id')).exists():
            deny_user = Social_User_Table.objects.get(user_id=session_user_info.get('user_id'))
            if deny_user.admin_allow == False:
                pass
                # return redirect('/submit')
            else:
                return redirect('/')                

        if session_user_info :            
            quiz01 = Query_Table.objects.get(pk=1)
            quiz02 = Query_Table.objects.get(pk=2)
            quiz03 = Query_Table.objects.get(pk=3)
            quiz04 = Query_Table.objects.get(pk=4)
            quiz05 = Query_Table.objects.get(pk=5)
            quiz06 = Query_Table.objects.get(pk=6)
            quiz07 = Query_Table.objects.get(pk=7)
            quiz08 = Query_Table.objects.get(pk=8)
            quiz09 = Query_Table.objects.get(pk=9)
            quiz10 = Query_Table.objects.get(pk=10)

            context = {'user' : session_user_info, 'quiz01' : quiz01, 'quiz02' : quiz02, 'quiz03' : quiz03,
                         'quiz04' : quiz04, 'quiz05' : quiz05, 'quiz06' : quiz06, 'quiz07' : quiz07,
                         'quiz08' : quiz08, 'quiz09' : quiz09,  'quiz10' : quiz10,
                          'LAST_DATE' : LAST_DATE, 'THIS_DATE' : THIS_DATE, 'NEXT_DATE' : NEXT_DATE}
            return render(request, 'submit/submit.html', context)

        else:
            return redirect('/')

    elif request.method == "POST":

        # select, option 데이터 넘길 때
        html_university = request.POST['html_university']
        html_option = request.POST.get('html_option')
        html_contact = request.POST.get('html_contact')
        html_image = request.FILES.get('html_image')

        # 매칭 옵션 1:1 선택시
        if html_option == '1:1':
            html_preference = request.POST.get('html_preference')
            html_Q01 = request.POST.get('html_Q01')
            html_Q02 = request.POST.get('html_Q02')
            html_Q03 = request.POST.get('html_Q03')
            html_Q04 = request.POST.get('html_Q04')        
            html_Q05 = request.POST.get('html_Q05')
            html_Q06 = request.POST.get('html_Q06')     
            html_Q07 = request.POST.get('html_Q07')
            html_Q08 = request.POST.get('html_Q08')        
            html_Q09 = request.POST.get('html_Q09')
            html_Q10 = request.POST.get('html_Q10')
            
            html_Q01 = string_to_bool(html_Q01)
            html_Q02 = string_to_bool(html_Q02)
            html_Q03 = string_to_bool(html_Q03)
            html_Q04 = string_to_bool(html_Q04)
            html_Q05 = string_to_bool(html_Q05)
            html_Q06 = string_to_bool(html_Q06)
            html_Q07 = string_to_bool(html_Q07)
            html_Q08 = string_to_bool(html_Q08)
            html_Q09 = string_to_bool(html_Q09)
            html_Q10 = string_to_bool(html_Q10)        
    
            Social_User_Table(
                # 유저 정보
                user_id         = session_user_info.get('user_id'),
                user_nickname   = session_user_info.get('user_nickname'),
                gender          = session_user_info.get('gender'),
                age_range       = session_user_info.get('age_range'),
                contact         = html_contact,        
                university      = html_university,   
                option          = html_option,              
                preference      = html_preference,  
                image           = html_image,

                # 질문 결과 Q1~10
                Q01 = html_Q01,
                Q02 = html_Q02,
                Q03 = html_Q03,
                Q04 = html_Q04,
                Q05 = html_Q05,
                Q06 = html_Q06,
                Q07 = html_Q07,
                Q08 = html_Q08,
                Q09 = html_Q09,
                Q10 = html_Q10,
            ).save()

        # 매칭 옵션 N:N- 선택시
        else:            
            Social_User_Table(
                # 유저 정보
                user_id         = session_user_info.get('user_id'),
                user_nickname   = session_user_info.get('user_nickname'),
                gender          = session_user_info.get('gender'),
                age_range       = session_user_info.get('age_range'),
                contact         = html_contact,        
                university      = html_university,   
                option          = html_option,          
                image           = html_image,
            ).save()


        return redirect('/status')


def string_to_bool(str):
    if str == 'left':
        return True
    elif str == 'right' :
        return False
