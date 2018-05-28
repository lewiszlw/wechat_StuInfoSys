from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField('用户名', max_length=25, unique=True)
    password = models.CharField('密码', max_length=25)
    ADMIN = 1
    STUDENT = 2
    TEACHER = 3
    ROOT = 4
    TYPES = (
        (ADMIN, '管理员（辅导员）'),
        (STUDENT, '学生'),
        (TEACHER, '教师'),
        (ROOT, '超级管理员'),
    )
    type = models.IntegerField(choices=TYPES, default=STUDENT)

class Teacher(models.Model):
    no = models.CharField('职工号', max_length=25, default='')
    name = models.CharField('姓名', max_length=25, default='')
    intro = models.CharField('介绍', max_length=500, default='')
    college = models.CharField('所属学院', max_length=25, default='')

class Student(models.Model):
    name = models.CharField('姓名', max_length=25, default='')
    no = models.CharField('学号', max_length=25, unique=True)

    MALE = 1
    FEMALE = 2
    UNKNOWNGENDER = 3
    GENDERS = (
        (MALE, '男'),
        (FEMALE, '女'),
        (UNKNOWNGENDER, '未知'),
    )
    gender = models.IntegerField(choices=GENDERS, default=UNKNOWNGENDER)

    identity = models.CharField('身份证号', max_length=25, default='')
    nation = models.CharField('民族', max_length=25, default='汉族')
    major = models.CharField('专业', max_length=25, default='')

    MAQU = 1
    YUQU = 2
    UNKNOWNZONE = 3
    ZONES = (
        (MAQU, '马区'),
        (YUQU, '余区'),
        (UNKNOWNZONE, '未知'),
    )
    zone = models.IntegerField(choices=ZONES, default=MAQU)

    classno = models.CharField('班级号', max_length=25, default='')
    counsellor = models.CharField('辅导员职工号', max_length=25, default='') # 辅导员

class Leave(models.Model):
    name = models.CharField('姓名', max_length=25, default='')
    no = models.CharField('学号', max_length=25)
    classno = models.CharField('班级号', max_length=25, default='')

    FORTHINGS = 1
    FORILLNESS = 2
    FOROTHER = 3
    TYPES = (
        (FORTHINGS, '事假'),
        (FORILLNESS, '病假'),
        (FOROTHER, '其他'),
    )
    type = models.IntegerField(choices=TYPES, default=FOROTHER)

    time = models.CharField('请假时间', max_length=100, default='')
    reason = models.CharField('请假原因', max_length=100, default='')

    NOTBACK = 1
    ISBACK = 2
    BACKCHOICES = (
        (NOTBACK, '未销假'),
        (ISBACK, '已销假'),
    )

    is_back = models.IntegerField(choices=BACKCHOICES, default=NOTBACK)


class Query(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sorce = models.CharField('成绩图片url', max_length=125, default='')
    cadre = models.CharField('干部任职情况图片url', max_length=125, default='')
    reward_punish = models.CharField('奖惩情况图片url', max_length=125, default='')


class Credit(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    graduation = models.IntegerField('毕业学分', default=0)
    obtain = models.IntegerField('已修学分', default=0)
    need = models.IntegerField('所需学分', default=0)


class Question(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    RECOMMEND = 1
    GRADUATE = 2
    ABROAD = 3
    WORK = 4
    SOLDIER = 5
    TYPES = (
        (RECOMMEND, '推免保送'),
        (GRADUATE, '考研深造'),
        (ABROAD, '出国留学'),
        (WORK, '就业'),
        (SOLDIER, '应征入伍'),
    )
    type = models.IntegerField(choices=TYPES, default=WORK)
    point = models.IntegerField('指定老师id', default=0)
    desc = models.CharField('问题描述', max_length=500, default='')
    is_answered = models.IntegerField(default=0) # 0未回答， 1已回答
    reply = models.CharField('回答', max_length=500, default='')
