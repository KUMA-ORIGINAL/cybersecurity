from django.contrib import admin
from .models import Course, Test


class TestInline(admin.TabularInline):  # Используем TabularInline для отображения тестов прямо в форме курса
    model = Test
    extra = 1


# Регистрируем модель Course в админке
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'duration', 'created_at', 'updated_at')  # Поля, которые будут отображаться в списке
    list_filter = ('level',)  # Фильтры для уровней курсов
    search_fields = ('title', 'description')  # Поиск по названию и описанию
    ordering = ('-created_at',)  # Сортировка по дате создания
    inlines = [TestInline]


# Регистрируем модель Test в админке
class TestAdmin(admin.ModelAdmin):
    list_display = ('course', 'question', 'correct_answer')  # Поля, которые будут отображаться в списке
    list_filter = ('course',)  # Фильтры для курсов
    search_fields = ('question', 'correct_answer')  # Поиск по вопросам и правильным ответам

# Регистрируем модели с указанными настройками
admin.site.register(Course, CourseAdmin)
admin.site.register(Test, TestAdmin)
