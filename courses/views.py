from django.shortcuts import render
from .models import Course, Test


def home(request):
    courses = Course.objects.all()[:3]  # Выведем несколько курсов на главной странице
    return render(request, 'courses/home.html', {'courses': courses})


def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})


def about(request):
    return render(request, 'courses/about.html')


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    tests = Test.objects.filter(course=course)

    if request.method == 'POST':
        # Переменная для подсчета правильных ответов
        correct_answers_count = 0
        total_questions = tests.count()

        # Проверяем ответы
        for test in tests:
            # Получаем выбранный пользователем ответ
            selected_answer = request.POST.get(f'answer{test.id}')
            if selected_answer == test.correct_answer:
                correct_answers_count += 1

        # Проверяем, сдал ли тест
        passed = correct_answers_count >= total_questions / 2  # Например, нужно больше половины правильных ответов

        # Отправляем результат в контекст для отображения
        context = {
            'course': course,
            'tests': tests,
            'correct_answers_count': correct_answers_count,
            'total_questions': total_questions,
            'passed': passed,
        }
        return render(request, 'courses/course_test_result.html', context)

        # Если это GET-запрос, отображаем форму с вопросами
    context = {
        'course': course,
        'tests': tests,
    }
    return render(request, 'courses/course.html', context)

