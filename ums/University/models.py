from django.db import models


class Student(models.Model):
    ID = models.AutoField
    student_name=models.CharField(max_length=50)
    dept_name=models.CharField(max_length=50)
    student_tot_credit=models.IntegerField(default=0)

    def __str__(self):
        return self.ID

class Course(models.Model):
    course_id = models.AutoField
    course_tittle = models.CharField(max_length=20)
    dept_name = models.CharField(max_length=50)
    course_tot_credit = models.IntegerField(default=0)

    def __str__(self):
        return self.course_id


class Classroom(models.Model):
    building = models.CharField(max_length=50)
    room_no = models.IntegerField(default=0)
    capacity=models.IntegerField(default=0)

    def __str__(self):
        return self.building


class Timeslot(models.Model):
    time_slot_id = models.IntegerField(default=0)
    Day=models.CharField(max_length=10)
    start_time=models.CharField(max_length=20)
    end_time=models.CharField(max_length=20)

    def __str__(self):
        return self.time_slot_id





class Section(models.Model):
    course_id = models.AutoField
    sec_id = models.IntegerField(default=0)
    semester=models.IntegerField(default=0)
    Year = models.IntegerField(default=0)
    building = models.CharField(max_length=50)
    room_no=models.IntegerField(default=0)
    time_slot_id=models.CharField(max_length=20)

    def __str__(self):
        return self.sec_id


# class Takes(models.Model):
#     student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course_id = models.ForeignKey(Section, on_delete=models.CASCADE)
#     sec_id = models.ForeignKey(Section, on_delete=models.CASCADE)
#     semester = models.ForeignKey(Section, on_delete=models.CASCADE)
#     Year = models.ForeignKey(Section, on_delete=models.CASCADE)
#     grade=models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.student_id

class Instructor(models.Model):
    instructor_id = models.AutoField
    instructor_name=models.CharField(max_length=50)
    dept_name=models.CharField(max_length=50)
    instructor_salary=models.IntegerField(default=0)

    def __str__(self):
        return self.instructor_id


# class Teaches(models.Model):
#     instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
#     course_id = models.ForeignKey(Section, on_delete=models.CASCADE)
#     sec_id = models.ForeignKey(Section, on_delete=models.CASCADE)
#     semester = models.ForeignKey(Section, on_delete=models.CASCADE)
#     Year = models.ForeignKey(Section, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.teacher_id

class Prereq(models.Model):
    course_id = models.AutoField
    prereq_id = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.prereq_id

class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    building=models.CharField(max_length=50)
    budget=models.IntegerField(default=0)

    # def __str__(self):
    #     return self.dept_name



class Advisor(models.Model):
    id = models.AutoField
    instructor_id = models.IntegerField(default=0)

    def __str__(self):
        return self.instructor_id

class Contact(models.Model):
    msg_id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name