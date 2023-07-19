from django import template
from django.template.loader import get_template

register = template.Library()
def my_template(value,arg):
    if arg == 'change':
        value = 'Rahim'
        return value
    if arg == 'title':
        return value.title()

def show_courses():
    courses = [
        {
            "id": 1,
            "course":"C",
            "teacher":"Fahim"
            },
        {
            "id":2,
            "course":"C++",
            "teacher":"Faria"
            },
        {
            "id":3,
            "course":"Python",
            "teacher":"Taha"
            }
        ]
    return {"courses":courses}

course_template = get_template('first_app/courses.html')

register.filter('change_name',my_template)
register.inclusion_tag(course_template)(show_courses)
