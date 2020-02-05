from django.contrib import admin

# Register your models here.
from .models import Department,Student,Course,Section,Timeslot,Classroom,Prereq,Instructor,Advisor,Contact

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Section)
# admin.site.register(Takes)
admin.site.register(Timeslot)
admin.site.register(Classroom)
# admin.site.register(Teaches)
admin.site.register(Prereq)
admin.site.register(Instructor)
admin.site.register(Advisor)
admin.site.register(Contact)

