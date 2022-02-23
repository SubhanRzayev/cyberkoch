import re
from django import forms

from core.models import Contact,Subscriber


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'surname',
            'phone',
            'email',
            'message',
        )
        
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'name-surname'
                }),
            
            'surname': forms.TextInput(attrs={
                'class': 'name-surname'
                }),
            
            'phone':forms.TextInput(attrs={
                'class':'phone'
                
                }),

            
            'email': forms.EmailInput(attrs={
                'class':'email1'
                
                }),
            
            'message': forms.Textarea(attrs={
                'class': 'textarea'
            })
        }
            
            
            
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = (
            'email',
        )
        
        widgets = {
            'email': forms.EmailInput(),
        }
            
            
# class RegisterForm(forms.ModelForm):
    
    
#     class Meta:
#         model = Register
#         fields = (
#             'name',
#             'surname',
#             'phone',
#             'email',
#             'state',
#             'city',
#             'expirence',
#             'highest_education',
#             'name_educational',
#             'profession',
#             'work_schedule',
#             'hear_about'
#         )
        
        
#         def __init__(self, *args, **kwargs):
#             super(RegisterForm, self).__init__(*args, **kwargs)
#             self.fields['expirence'] = forms.ModelChoiceField(
#                 queryset=Register.objects.all(),initial=0
#             )
#             self.fields['highest_education'] = forms.ModelChoiceField(
#                 queryset=Register.objects.all(),initial=0
#             )
            
#             self.fields['current_work_schedule'] = forms.ModelChoiceField(
#                 queryset=Register.objects.all(),initial=0
#             )

            
        # program_expirence = forms.ChoiceField(choices=Register.EXPERIENCE_CHOICES)
        # highest_level_of_education = forms.ChoiceField(choices=Register.HIGHEST_EDUCATION_CHOICES)
        # current_work_schedule = forms.ChoiceField(choices=Register.WORK_SCHEDULE_CHOICES)
    
        


            
            
        
        