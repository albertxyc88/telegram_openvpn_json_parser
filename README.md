# Telegram bot.

## Скрипт парсит файл JSON в котором хранятся данные по подключениям OpenVPN (дата время подключения, дата время отключения, логин)

На сервере OpenVPN подключен скрипт который при каждом подключении \ отключении удаленного сотрудника отправляет в чат Telegram информацию в таком виде:

`2022/10/01 08:47:17 - CONNECT 10.0.110.131, login, 78.85.49.13`

`2022/10/01 13:47:21 - DISCONNECT 10.0.110.131, login, 78.85.49.13`

В конце месяца или иного произвольного периода, штатными средствами Telegram делается экспорт чата в формате JSON (образец файла приложен в репозитории)

Далее запускается скрипт который выдает суммарное время работы сотрудника на удаленке в формате логин - суммарное время, списком отсортированным по алфавиту

## Технологии

Python 3.7, Telegram, bot, JSON.

## Установка

- склонируйте репозитарий 

- подготовьте файл в нужном формате

- запустите скрипт

