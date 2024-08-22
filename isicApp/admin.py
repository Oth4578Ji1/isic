# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Competition, Application

# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Competition, Application

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'CIN', 'address', 'date_of_birth', 'place_of_birth', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_type', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'CIN', 'address', 'date_of_birth', 'place_of_birth', 'phone', 'user_type', 'is_staff', 'is_active'),
        }),
    )

# Competition Admin
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('type', 'field', 'deadline', 'created_at', 'updated_at')
    list_filter = ('type', 'field', 'deadline')

# Application Admin
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('student','student_first_name', 'student_last_name', 'CNE', 'competition', 'baccalaureate_category','baccalaureate_grade', 'diploma_category', 'diploma_year', 'diploma_grade',
                  'semester_1_grade', 'semester_2_grade', 'semester_3_grade', 'semester_4_grade', 'semester_5_grade', 'semester_6_grade', 'language', 'status')
    list_filter = ('status', 'competition__type', 'competition__field')
    search_fields = ('student__first_name', 'student__last_name', 'student__CIN')
    
    def student_first_name(self, obj):
        return obj.student.first_name
    
    def student_last_name(self, obj):
        return obj.student.last_name

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Application, ApplicationAdmin)


