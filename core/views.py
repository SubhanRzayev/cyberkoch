from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import JsonResponse

from django.views.generic import ListView,CreateView,TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from core.models import *
from django.views.generic.edit import FormView

from core.forms import ContactForm

from django.contrib import messages
# Create your views here.


# def register(request):
#     return render(request,'register.html')




class CourseView(ListView):
    model = Course
    template_name = 'softwar-automation-test-engineer.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = None
        categoryId = self.request.GET.get('category')
        if categoryId:
            course = Course.get_all_course_by_categoryid(categoryId)
        else:
            course = Course.get_course_all()
            
        context['course_list'] = course
        context['logos_list'] = Logo.objects.all()
        context['course_staff_list'] = CourseStaff.objects.all()
        
        return context
    
    
    


class MainListView(ListView):
    model = Main
    template_name = 'index.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logo_list"] = Logo.objects.all()
        context["reason_list"] = Reason.objects.all()
        context["comments_list"] = Comments.objects.all()[:4]
        
        
        return context
    
    



    
    
    
    
    


class CurriculumListView(ListView):
    model = Curriculum
    template_name = 'curriculum.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    




class AboutView(ListView):
    model = About
    template_name = 'about.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo_list'] = Logo.objects.all()
        return context
    
    
    
class FaqQuestionListView(ListView):
    model = FaqQuestion
    template_name = 'faq.html'

    


    

    
    
class ContactCreateView(SuccessMessageMixin,CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_message = 'Contact request submitted successfully!'
    error_message = 'Invalid form submission.'
    success_url = reverse_lazy('core:contact')
    
    
    def form_valid(self, form):
        form.save()
        context =  super().form_valid(form)
        return context
    
    def form_invalid(self,form):
        self.messages.error(self.request,self.error_message)
        context = super().form_invalid(form)
        return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["address_list"] = Address.objects.all()[:1]
        return context
    



    
def register(request):
    if request.method == 'POST':
    
        
        name = request.POST.get('name')  
        surname = request.POST.get('surname')  
        phone = request.POST.get('phone')  
        email = request.POST.get('email')  
        state = request.POST.get('state')  
        city = request.POST.get('city')  
        experience = request.POST.get('experience')
        highest_education = request.POST.get('highestEducation')
        name_educational = request.POST.get('education')  
        profession = request.POST.get('profession')  
        work_schedule = request.POST.get('workSchedule')  
        hear_about = request.POST.get('hearAbout')


        data = Register.objects.create(
            name=name,
            surname=surname,
            phone=phone,
            email=email,
            state=state,
            city=city,
            experience = experience,
            highest_education=highest_education,
            name_educational=name_educational,
            profession=profession,
            work_schedule=work_schedule,
            hear_about=hear_about
        )
        if data:
            
            return render(request, 'register2.html')


    return render(request, 'register.html')
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    


