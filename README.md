Для выполнения тестирования применялись методы:

Тестирование требований
Ручное тестирование
Автотестирование с помощью Python, Devtools, Selenium
Позитивное/негативное/деструктивное тестирование
Функциональное тестирование (Авторизация через телефон и имейл, Выход из личного кабинета )
Нефункциональное тестирование (Тестирование пользовательского интерфейса)
Комманда для запуска тестов python из директории tests 'pytest -v --driver Chrome --driver-path chromedriver.exe  test_auth_rt.py' 
при условии нахождения chromedriver в указаной директории. 

Тестов можно, конечно, написать намного больше, использовать больше различных вводных данных. 
Останавливало появление капчи, тк из-за нее тесты падают. Приходится чередовать вход в личный кабинет с выходом и тд. Иначе вылезает капча.
Так же не тестировал форму регистрации и личный кабинет, не проводил проверку сайта с помощью SEO Tools, не проверял на коды ошибок в DevTools, 
не делал нагрузочное тестирование и много всего, что можно было сделать.
Что не получилось:
Сделать скрин всплывающего окна при вызове телефона и закрыть его нажатием кнопки ESCAPE. В итоге отказался от этого теста.
Закрыть окно чата. Если ставить тест чата в середину, то он открывается во всех остальных тестах

Было очень интересно, узнал много нового!
