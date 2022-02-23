from importlib.metadata import requires
from itertools import count
from tkinter import N
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import IntegerField
from django.utils.safestring import mark_safe
from django.urls import reverse

# Create your models here.


        
        
        
    
class Course(models.Model):
    #relations
    category = models.ForeignKey('CategoryCourse',db_index=True,blank=True,null=True,related_name='coruse_category',on_delete=models.CASCADE)
    
    head = RichTextUploadingField()
    course_count = models.IntegerField()
    description = RichTextUploadingField()
    duration = models.CharField(max_length=100)
    teachers_count = models.IntegerField()
    max_students = models.IntegerField()
    skill_level = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='course_img',blank = True,null = True)

    def __str__(self):
        return str(self.category)

    @staticmethod
    def get_course_all():
        return Course.objects.all()
    
    @staticmethod
    def get_all_course_by_categoryid(category_id):
        if category_id:
            return Course.objects.filter(category = category_id)
        
        
    class Meta:
        verbose_name_plural = 'Course'



class CategoryCourse(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category
    
    
    class Meta:
        verbose_name_plural = 'Category_Course'
    


class Main(models.Model):
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='media',blank=True,null=True)


    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name_plural = 'Main'
    
    
        
class Reason(models.Model):
    numbers = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return self.numbers
    
    class Meta:
        verbose_name_plural = 'Why CyberKoch Academy?'


class Comments(models.Model):
    description = RichTextUploadingField()
    full_name = models.CharField(max_length=120,blank=True,null=True)
    position = models.CharField(max_length=120,blank=True,null=True)
    user_image = models.ImageField(upload_to='media')
    comment_count = models.IntegerField()
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name_plural = 'Comments'
        
    
        
class Curriculum(models.Model):
    count = models.IntegerField(blank=True,null=True)
    course_number = models.CharField(max_length=100)
    course_name = models.CharField(max_length=1000,blank=True,null=True)
    queastion = models.TextField(max_length=1000,blank=True,null=True)
    
    def __str__(self):
        return self.course_name
    
    class Meta:
        verbose_name_plural = 'Curriculum'
        

    

class CurriculumDetail(models.Model):
    curriculum_detail = models.ForeignKey(Curriculum,on_delete=models.CASCADE,blank=True,null=True,related_name='curriculum_detail')
    detail =models.TextField(max_length=2000,blank=True,null=True)
        
        
    def __str__(self):
        return f'{self.curriculum_detail} is detail'
    
    class Meta:
        verbose_name_plural = 'CurriculumDetail'
        
    
    

class CourseStaff(models.Model):
    course_duration = models.CharField(max_length=100,blank=True,null=True,default='24 Weeks')
    teachers_count = models.CharField(max_length=100,blank=True,null=True,default='8')
    max_students = models.CharField(max_length=100,blank=True,null=True,default='8')
    skill_level = models.CharField(max_length=100,blank=True,null=True,default='All')

    def __str__(self):
        return str(self.course_duration)
    
    class Meta:
        verbose_name_plural = 'Course_Staff'
    


class About(models.Model):
    content1 = RichTextUploadingField()
    content2 = RichTextUploadingField()
    about_image = models.ImageField(upload_to='media')

    def __str__(self):
        return str(self.about_image)

    
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.about_image.url))
    
    class Meta:
        verbose_name_plural = 'About'
        
        
        
    
        
class Address(models.Model):
    title = models.CharField(max_length=1000,default="Get In Touch")
    description = models.TextField(max_length=1000,default="Not to give you mom-guilt or anything, but it would be so nice to hear from you every once in a while.")
    phone = models.CharField(max_length=30,default='+1 (289) 788-9196')
    email = models.EmailField(default='office@cyberkoch.com',blank=True)
    sales = models.EmailField(default='sales@cyberkoch.com',blank=True)
    
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = "Address"
    
    
class Contact(models.Model):
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)
    email = models.EmailField(max_length=120)
    message = models.TextField(max_length=1000)
    
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Contact'
        
        

class Logo(models.Model):
    logos = models.FileField(blank=True,null=True)
    
    
    def __str__(self):
        return str(self.logos)
    
    
    

class Subscriber(models.Model):
    email = models.EmailField()
    
    created_at = models.DateTimeField(auto_now=True,blank=True)
    update_at = models.DateTimeField(auto_now_add=True,blank=True)
    
    
    def __str__(self):
        return self.email
    
    
    
class FaqQuestion(models.Model):
    question = models.TextField(max_length=1000,blank=True,null=True)
    
    class Meta:
        verbose_name_plural = 'Faq_Question'
    
    
    def __str__(self):
        return self.question
    
    
    

class FaqAnswer(models.Model):
    question_answer = models.ForeignKey(FaqQuestion,on_delete=models.CASCADE,blank=True,null=True,related_name='question_answer')
    answer = models.TextField(max_length=1000,blank=True,null=True)
    
    
    
    class Meta:
        verbose_name_plural = 'Faq_Answer'
    
    
    
    def __str__(self):
        return f'{self.question_answer} answers to the question {self.answer}'
    
    
        


    

class Image(models.Model):
    about = models.ForeignKey('About',on_delete=models.CASCADE, related_name='about_images',db_index=True,blank=True,null=True)
    curric_image = models.ForeignKey(Curriculum,on_delete=models.CASCADE, related_name='curric_images',db_index=True,blank=True,null=True)
    course_image = models.ForeignKey(Course,on_delete=models.CASCADE, related_name='courses_images',db_index=True,blank=True,null=True)
    
    image = models.ImageField(blank=True,upload_to='images')
    
    
    def __str__(self):
        return str(self.image)
    
    # def image_tag(self):
    #     return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.image.url))
    # image_tag.short_description = 'Image'
            


    
class Head(models.Model):
    about_head = models.ForeignKey('About',on_delete=models.CASCADE,blank=True,null=True,related_name='about_head')
    faq_head = models.ForeignKey('FaqQuestion',on_delete=models.CASCADE,blank=True,null=True,related_name='faq_head')
    curriculum_head = models.ForeignKey('Curriculum',on_delete=models.CASCADE,null=True,blank=True,related_name='curriculum_head')
    
    head = RichTextUploadingField()
    def __str__(self):
        return self.head
    

class Register(models.Model):    
    
    WORK_SCHEDULE_CHOICES = (
        ("Employed Full Time","Employed Full Time"),
        ("Employed Part Time","Employed Part Time"),
        ("Not Employed","Not Employed")
    )
    
    
    HIGHEST_EDUCATION_CHOICES = (
        ("No Degree","No Degree"),
        ("High School Diploma","High School Diploma"),
        ("Bachelor’s Degree","Bachelor’s Degree"),
        ("Master’s Degree","Master’s Degree"),
        ("PHD","PHD"),
    )


    
    
    EXPERIENCE_CHOICES = (
        ("HTML","HTML"),
        ("CSS","CSS"),
        ("JS","JS"),
        ("JAVA","JAVA"),
        ("DJANGO","DJANGO"),
        ("PYTHON","PYTHON"),
        ("C","C"),
        ("C#","C#"),

    )
        
    
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    experience = models.CharField(max_length=100,choices=EXPERIENCE_CHOICES)
    highest_education = models.CharField(max_length=100,choices=HIGHEST_EDUCATION_CHOICES)
    name_educational = models.CharField(max_length=100,blank=True,null=True)   
    profession = models.CharField(max_length=100,blank=True,null=True)  
    work_schedule = models.CharField(max_length=100,choices=WORK_SCHEDULE_CHOICES)
    hear_about = models.CharField(max_length=1000)
    
    
    class Meta:
        verbose_name_plural = 'Register'
        
    def __str__(self):
        return self.name
    
  

  