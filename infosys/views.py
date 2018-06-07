from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.db.models import Q
import json
# Create your views here.

@csrf_exempt
def index(request):
    template = loader.get_template('infosys/login.html')
    return HttpResponse(template.render(request=request))

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_type = int(request.POST.get('userType'))

    try:
        user = User.objects.get(username=username)
        if user.type != user_type:
            return HttpResponse('fail')
    except User.DoesNotExist:
        return HttpResponse('fail')

    if user and user.password == password:
        return HttpResponse('success')
    else:
        return HttpResponse('fail')




#################### Student start ###################
def main(request):
    template = loader.get_template('infosys/main.html')
    return HttpResponse(template.render(request=request))


# 基本信息
def profile(request):
    #import pdb;pdb.set_trace()
    username = request.GET.get('username')
    student = Student.objects.get(no=username)
    template = loader.get_template('infosys/profile.html')
    return HttpResponse(template.render(request=request, context={'student': student}))

# 请销假记录
def leaves(request):
    #import pdb;pdb.set_trace()
    username = request.GET.get('username')
    leaves = Leave.objects.filter(no=username)
    template = loader.get_template('infosys/leaves.html')
    return HttpResponse(template.render(request=request, context={'leaves': leaves}))

# 毕业学分要求
def credit(request):
    try:
        username = request.GET.get('username')
        student = Student.objects.get(no=username)
        credit = Credit.objects.get(student=student)
    except (Student.DoesNotExist, Credit.DoesNotExist):
        return HttpResponse('fail')
    template = loader.get_template('infosys/credit.html')
    return HttpResponse(template.render(request=request, context={'credit': credit}))

# 我要提问
@csrf_exempt
def ask(request):
    teachers = Teacher.objects.all()
    template = loader.get_template('infosys/ask.html')
    return HttpResponse(template.render(request=request, context={'teachers': teachers}))


def submit_question(request):
    username = request.POST.get('username')
    question_type = request.POST.get('questionType')
    teacher_id = request.POST.get('teacherId')
    question_desc = request.POST.get('question')
    if not username or not question_type or not teacher_id or not question_desc:
        return HttpResponse('fail')

    try:
        student = Student.objects.get(no=username)
        question = Question.objects.create(student=student, type=int(question_type), point=int(teacher_id), desc=question_desc)
    except Exception as e:
        return HttpResponse('fail')
    return HttpResponse('success')

def watch_score_cadre_rewardpunish(request):
    #import pdb;pdb.set_trace()
    username = request.GET.get('username')
    img_name = '{}.jpg'.format(username)
    import os
    from .config import UPLOAD_SCORE_CADRE_REWARDPUNISH_FOLDER
    if not os.path.exists(os.getcwd() + UPLOAD_SCORE_CADRE_REWARDPUNISH_FOLDER + '/' + img_name):
        return HttpResponse('<h1>辅导员尚未上传。</h1>')
    template = loader.get_template('infosys/watch-score-cadre-rewardpunish.html')
    return HttpResponse(template.render(request=request, context={'img_name': img_name}))

def watch_calendar(request):
    username = request.GET.get('username')
    img_name = 'all.jpg'
    import os
    from .config import UPLOAD_CALENDAR_FOLDER
    if not os.path.exists(os.getcwd() + UPLOAD_CALENDAR_FOLDER + '/' + img_name):
        return HttpResponse('<h1>辅导员尚未上传。</h1>')
    template = loader.get_template('infosys/watch-calendar.html')
    return HttpResponse(template.render(request=request, context={'img_name': img_name}))

def watch_reply(request):
    username = request.GET.get('username')
    questions = Question.objects.filter(student__no=username)
    template = loader.get_template('infosys/watch-reply.html')
    return HttpResponse(template.render(request=request, context={'questions': questions}))
#################### Student end ###################




#################### Teacher start ###################
def teacher_main(request):
    template = loader.get_template('infosys/teacher-main.html')
    return HttpResponse(template.render(request=request))

def answer(request):
    try:
        username = request.GET.get('username')
        teacher = Teacher.objects.get(no=username)
    except Exception:
        return HttpResponse('<h1>Fail.</h1>')
    questions = Question.objects.filter(Q(point=teacher.id) | Q(point=0))
    template = loader.get_template('infosys/answer.html')
    return HttpResponse(template.render(request=request, context={'questions': questions}))

def write_answer(request):
    try:
        question_id = request.GET.get('questionId')
        question = Question.objects.get(id=int(question_id))
    except Exception as e:
        print(e)
        return HttpResponse('<h1>Fail.</h1>')
    template = loader.get_template('infosys/write-answer.html')
    return HttpResponse(template.render(request=request, context={'question': question}))

def reply(request):
    question_id = request.POST.get('questionId')
    reply = request.POST.get('reply')
    if not question_id or not reply:
        return HttpResponse('fail')

    try:
        question = Question.objects.get(id=int(question_id))
        question.reply = reply
        question.is_answered = 1
        question.save()
        return HttpResponse('success')
    except Exception:
        return HttpResponse('fail')
################################## Teacher end #####################################




################################## Admin start ###################################
def admin_main(request):
    template = loader.get_template('infosys/admin-main.html')
    return HttpResponse(template.render(request=request))

def about_student(request):
    template = loader.get_template('infosys/about-student.html')
    return HttpResponse(template.render(request=request))

def about_teacher(request):
    template = loader.get_template('infosys/about-teacher.html')
    return HttpResponse(template.render(request=request))

def add_student(request):
    template = loader.get_template('infosys/add-student.html')
    return HttpResponse(template.render(request=request))

def apply_add_student(request):
    username = request.POST.get('username')
    name = request.POST.get('name')
    no = request.POST.get('no')
    gender = int(request.POST.get('gender'))
    identity = request.POST.get('identity')
    nation = request.POST.get('nation')
    major = request.POST.get('major')
    zone = int(request.POST.get('zone'))
    classno = request.POST.get('classno')
    if not username or not no:
        return HttpResponse('fail')

    try:
        Student.objects.create(name=name, no=no, gender=gender, identity=identity, nation=nation, major=major, zone=zone, classno=classno)
        User.objects.create(username=no, password=no, type=User.STUDENT)
        return HttpResponse('success')
    except Exception:
        return HttpResponse('fail')

def list_student(request):
    students = Student.objects.all()
    template = loader.get_template('infosys/list-student.html')
    return HttpResponse(template.render(request=request, context={'students': students}))

def list_leaves(request):
    leaves = Leave.objects.all()
    template = loader.get_template('infosys/list-leaves.html')
    return HttpResponse(template.render(request=request, context={'students': leaves}))

def modify_student(request):
    student_id = request.GET.get('studentId')
    try:
        student = Student.objects.get(id=student_id)
    except Exception:
        return HttpResponse('<h1>Fail.</h1>')
    template = loader.get_template('infosys/modify-student.html')
    return HttpResponse(template.render(request=request, context={'student': student}))

def apply_modify_student(request):
    student_id = int(request.GET.get('studentId'))

    username = request.POST.get('username')
    old_no = request.POST.get('oldNo')
    name = request.POST.get('name')
    no = request.POST.get('no')
    gender = int(request.POST.get('gender'))
    identity = request.POST.get('identity')
    nation = request.POST.get('nation')
    major = request.POST.get('major')
    zone = int(request.POST.get('zone'))
    classno = request.POST.get('classno')
    if not username or not no or not student_id:
        return HttpResponse('fail')

    try:
        student = Student.objects.get(id=student_id)
        student.name = name
        student.no = no
        student.gender = gender
        student.identity = identity
        student.nation = nation
        student.major = major
        student.zone = zone
        student.classno = classno
        student.save()
        user = User.objects.get(username=old_no)
        user.username = no
        user.save()
        return HttpResponse('success')
    except Exception:
        return HttpResponse('fail')

def apply_delete_student(request):
    student_id = int(request.POST.get('studentId'))
    try:
        student = Student.objects.get(id=student_id)
        student_no = student.no
        student.delete()
        User.objects.get(username=student_no).delete()
        return HttpResponse('success')
    except Exception:
        return HttpResponse('fail')

def batch_add_student(request):
    template = loader.get_template('infosys/batch-add-student.html')
    return HttpResponse(template.render(request=request))

def apply_batch_add_student(request):
    # import pdb;pdb.set_trace()
    import xlrd
    f = request.FILES.get('input-b1')
    workbook = xlrd.open_workbook(file_contents=f.read())
    sheet = workbook.sheet_by_index(0)
    rows = sheet.nrows
    try:
        for row in range(rows):
            name = sheet.cell_value(row, 0)
            no = sheet.cell_value(row, 1)
            gender = int(sheet.cell_value(row, 2))
            identity = sheet.cell_value(row, 3)
            nation = sheet.cell_value(row, 4)
            major = sheet.cell_value(row, 5)
            zone = int(sheet.cell_value(row, 6))
            classno = sheet.cell_value(row, 7)
            Student.objects.create(name=name, no=no, gender=gender, identity=identity, nation=nation, major=major, zone=zone, classno=classno)
            User.objects.create(username=no, password=no, type=User.STUDENT)
        return HttpResponse(json.dumps({'msg': 'success'}))
    except Exception:
        return HttpResponse(json.dumps({'msg': 'fail'}))

def batch_add_credit(request):
    template = loader.get_template('infosys/batch-add-credit.html')
    return HttpResponse(template.render(request=request))

def apply_batch_add_credit(request):
    # import pdb;pdb.set_trace()
    import xlrd
    f = request.FILES.get('input-b1')
    workbook = xlrd.open_workbook(file_contents=f.read())
    sheet = workbook.sheet_by_index(0)
    rows = sheet.nrows
    try:
        for row in range(rows):
            no = sheet.cell_value(row, 0)
            graduation = int(sheet.cell_value(row, 1))
            obtain = sheet.cell_value(row, 2)
            need = sheet.cell_value(row, 3)
            student = Student.objects.get(no=no)
            Credit.objects.create(student=student, graduation=graduation, obtain=obtain, need=need)
        return HttpResponse(json.dumps({'msg': 'success'}))
    except Exception:
        return HttpResponse(json.dumps({'msg': 'fail'}))

def batch_add_leave(request):
    template = loader.get_template('infosys/batch-add-leave.html')
    return HttpResponse(template.render(request=request))

def apply_batch_add_leave(request):
    import pdb;pdb.set_trace()
    import xlrd
    f = request.FILES.get('input-b1')
    workbook = xlrd.open_workbook(file_contents=f.read())
    sheet = workbook.sheet_by_index(0)
    rows = sheet.nrows
    try:
        for row in range(rows):
            no = sheet.cell_value(row, 0)
            type = int(sheet.cell_value(row, 1))
            time = sheet.cell_value(row, 2)
            reason = sheet.cell_value(row, 3)
            is_back = int(sheet.cell_value(row, 4))
            student = Student.objects.get(no=no)
            Leave.objects.create(name=student.name, no=no, classno=student.classno, type=type, time=time, reason=reason, is_back=is_back)
        return HttpResponse(json.dumps({'msg': 'success'}))
    except Exception:
        return HttpResponse(json.dumps({'msg': 'fail'}))

def list_teacher(request):
    teachers = Teacher.objects.all()
    template = loader.get_template('infosys/list-teacher.html')
    return HttpResponse(template.render(request=request, context={'teachers': teachers}))

def modify_teacher(request):
    teacher_id = request.GET.get('teacherId')
    try:
        teacher = Teacher.objects.get(id=teacher_id)
    except Exception:
        return HttpResponse('<h1>Fail.</h1>')
    template = loader.get_template('infosys/modify-teacher.html')
    return HttpResponse(template.render(request=request, context={'teacher': teacher}))

def apply_modify_teacher(request):
    teacher_id = int(request.GET.get('teacherId'))

    username = request.POST.get('username')
    old_no = request.POST.get('oldNo')
    name = request.POST.get('name')
    no = request.POST.get('no')
    intro = request.POST.get('intro')
    college = request.POST.get('college')
    if not username or not no or not teacher_id:
        return HttpResponse('fail')

    try:
        teacher = Teacher.objects.get(id=teacher_id)
        teacher.name = name
        teacher.no = no
        teacher.intro = intro
        teacher.college = college
        teacher.save()
        user = User.objects.get(username=old_no)
        user.username = no
        user.save()
        return HttpResponse('success')
    except Exception as e:
        print(e.__traceback__)
        return HttpResponse('fail')

def apply_delete_teacher(request):
    teacher_id = int(request.POST.get('teacherId'))
    try:
        teacher = Teacher.objects.get(id=teacher_id)
        teacher_no = teacher.no
        teacher.delete()
        User.objects.get(username=teacher_no).delete()
        return HttpResponse('success')
    except Exception:
        return HttpResponse('fail')

def add_teacher(request):
    template = loader.get_template('infosys/add-teacher.html')
    return HttpResponse(template.render(request=request))

def apply_add_teacher(request):
    username = request.POST.get('username')
    name = request.POST.get('name')
    no = request.POST.get('no')
    intro = request.POST.get('intro')
    college = request.POST.get('college')
    if not username or not no:
        return HttpResponse('fail')

    try:
        Teacher.objects.create(name=name, no=no, intro=intro, college=college)
        User.objects.create(username=no, password=no, type=User.TEACHER)
        return HttpResponse('success')
    except Exception:
        return HttpResponse('fail')

def add_counsellor(request):
    template = loader.get_template('infosys/add-counsellor.html')
    return HttpResponse(template.render(request=request))

def apply_add_counselor(request):
    username = request.POST.get('username')
    name = request.POST.get('name')
    no = request.POST.get('no')
    intro = request.POST.get('intro')
    college = request.POST.get('college')
    if not username or not no:
        return HttpResponse('fail')

    try:
        Teacher.objects.create(name=name, no=no, intro=intro, college=college)
        User.objects.create(username=no, password=no, type=User.ADMIN)
        return HttpResponse('success')
    except Exception:
        return HttpResponse('fail')

def score_cadre_rewardpunish(request):
    template = loader.get_template('infosys/score-cadre-rewardpunish.html')
    return HttpResponse(template.render(request=request))

def upload_score_cadre_rewardpunish(request):
    no = request.POST.get('no')
    f_obj = request.FILES.get('input-b1')
    from .config import UPLOAD_SCORE_CADRE_REWARDPUNISH_FOLDER
    import os
    try:
        f = open(os.getcwd() + UPLOAD_SCORE_CADRE_REWARDPUNISH_FOLDER + '/' + '{}.jpg'.format(no), 'wb')
        for chunk in f_obj.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse(json.dumps({'msg': 'success'}))
    except Exception:
        return HttpResponse(json.dumps({'msg': 'fail'}))

def calendar(request):
    template = loader.get_template('infosys/calendar.html')
    return HttpResponse(template.render(request=request))

def upload_calendar(request):
    f_obj = request.FILES.get('input-b1')
    from .config import UPLOAD_CALENDAR_FOLDER
    import os
    try:
        f = open(os.getcwd() + UPLOAD_CALENDAR_FOLDER + '/' + '{}.jpg'.format('all'), 'wb')
        for chunk in f_obj.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse(json.dumps({'msg': 'success'}))
    except Exception:
        return HttpResponse(json.dumps({'msg': 'fail'}))

#################### Admin end ###################


def root_main(request):
    template = loader.get_template('infosys/root-main.html')
    return HttpResponse(template.render(request=request))
