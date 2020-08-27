[![Build Status](https://travis-ci.org/LesyaLeontyeva/inno-graduation-work.svg?branch=master)](https://travis-ci.org/github/LesyaLeontyeva/inno-graduation-work)

# Выпускная работа на курсе Автоматизация тестирования
Стек технологий: Selenium, Python, Pytest
# Выбранный ресурс:
URL https://idemo.bspb.ru/

# Установка зависимостей проекта и запуск:
pip install -r requirements.txt
1) Рекомендуется использоваться виртуальное окружение командой:
pip install virtualenv
2) Затем нужно активировать окружение:
virtualenv <env_name>
<env_name>\Scripts\activate.bat
3) Для запуска конкретного теста из файла:
    `pytest <filename>::<testclassname>::<testname>`

# Pre-commit-hooks
Перед началом работы, необходимо выполнить команду
pre-commit install
для того, чтобы pre-commit запускался перед каждым коммитом

Принудительный запуск pre-commit:
pre-commit run --all-files

Запуск конкретного hook:
pre-commit run <hook_id>

Пропуск pre-commit:
git commit -m "your_message_text" --no-verify

# Allure
Установка allure
Для генерации отчетов необходимо установить Scoop через PowerShell https://scoop.sh/

После чего нужно выполнить команду
scoop install allure
в окне PowerShell

Генерация отчетов
После прохождения тестов сформируется папка allure_result в корневой директории проекта

Для генерации отчета необходимо ввести команду в окне PowerShell
allure serve ${path}\inno_graduation_work\allure_result
