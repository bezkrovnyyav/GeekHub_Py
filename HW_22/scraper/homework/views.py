# 1. Пройти туторіал по Джанго (частини 1, 2, 3).https://docs.djangoproject.com/en/4.0/
# 2. На основі скрейпера із попередньої ДЗ створити сайт:
#  1. Основна сторінка - одна. На ній - дропдаун із доступними категоріями і кнопка.
# По натисканню на неї відбувається скрейпінг вибраної категорії.
# 2. Кожен тип записів (Ask, Job, Story) - це окрема модель зі своїми полями.
# 3. По полям типа "kids", "parents", "coments" та подібним ітеруватись не потрібно.
# 4. Під час скрейпінга скачувати тільки ті записи, яких немає в базі.
# 5. Всі записи виводити в Адмінці (зараз не потрібно створювати для них окремі сторінки в UI).

# Модифікувати ДЗ №19 таким чином, щоб скрейпінг відбувався в Селері черзі.
# Корисні посилання:
# https://docs.celeryproject.org/en/stable/
# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
# https://www.rabbitmq.com/


from django.shortcuts import render
from .tasks import new, ask, show, job


def index(request):
    value = request.POST.get('news_category')
    if value == 'new':
        new.delay()
    elif value == 'ask':
        ask.delay()
    elif value == 'show':
        show.delay()
    elif value == 'job':
        job.delay()
    return render(request, 'homework/index.html')
