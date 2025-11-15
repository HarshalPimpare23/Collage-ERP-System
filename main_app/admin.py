from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.


class UserModel(UserAdmin):
    ordering = ('email',)


admin.site.register(CustomUser, UserModel)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Book)
admin.site.register(IssuedBook)
admin.site.register(Library)
admin.site.register(Subject)
admin.site.register(Session)
admin.site.register(Attendance)
admin.site.register(ApplicationReport)
admin.site.register(StudentAdmissionReport)
admin.site.register(ConfirmApplicationReport)
admin.site.register(StudentRegistrationReport)
admin.site.register(StudentGeneralReport)
admin.site.register(StudentAddressReport)
admin.site.register(CancelledAdmissionReport)
admin.site.register(FeesAndPayment)
admin.site.register(VidyapeethFeesCollection)
admin.site.register(VidyapeethFeesPeinding)
admin.site.register(OthersFeesCollection)
admin.site.register(CreateTimetable)
admin.site.register(Subjects)