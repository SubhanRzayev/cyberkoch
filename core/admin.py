from django.contrib import admin
from core.models import *


# Register your models here.




@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display=['name',]

@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ['category','teachers_count','max_students','skill_level','cover_image']


@admin.register(CategoryCourse)
class CategoryCourse(admin.ModelAdmin):
    list_display = ['category',]



@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    
    list_display = ['logos']


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email','created_at','update_at',]
    

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ['description',]
    list_filter = ['description',]
    search_fields = ('description',)
    


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ['numbers','description',]
    list_filter = ['numbers','description',]
    

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    
    list_display = ['comment_count','description','full_name','position',]
    list_filter = ['full_name','position',]
    


class AboutImageInline(admin.TabularInline):
    model = Image
    extra = 1
    


    
@admin.register(FaqQuestion)
class FaqQuestionAdmin(admin.ModelAdmin):
    list_display = ['question',]
    list_filter = ['question',]
    search_fields = ('question',)
    
    
    
@admin.register(FaqAnswer)
class FaqAnswerAdmin(admin.ModelAdmin):
    list_display = ['question_answer','answer',]
    list_filter = ['question_answer','answer',]
    search_fields = ('question','answer',)
    
    

@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ['count','course_number','course_name','queastion',]
    
    
    
@admin.register(CurriculumDetail)
class CurriculumDetailAdmin(admin.ModelAdmin):
    list_display = ['curriculum_detail','detail',]
    
    

        


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['email','phone','sales','title','description',]
    list_filter = ['email',]
    search_fields = ('email',)

    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','surname','phone','email','message',]
    list_filter = ['name',]
    search_fields = ('name',)
    
    

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['content1','content2','image_tag']
    readonly_fields = ('image_tag',)
    inlines = [AboutImageInline]
    
    
    
    
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['about','curric_image','course_image',]

    
    
@admin.register(Head)
class HeadAdmin(admin.ModelAdmin):
    list_display = ['head',]
    
    
    
