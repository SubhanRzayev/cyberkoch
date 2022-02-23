from atexit import register
from django.template import Library
from core.models import  CategoryCourse


register = Library()


@register.simple_tag
def header_category():
    return CategoryCourse.objects.all()

