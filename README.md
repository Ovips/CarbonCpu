# CarbonCpu

### Установка
+ Перейти в тестовую директорию и создать виртуальное окружение
```
python3 -m venv venv
```
+ Включить виртуальное окружение
```
source venv/bin/activate
```
+ Обновить pip внутри виртуального окружения
```
python3 -m pip install --upgrade pip
```
+ Провести установку пакета
```
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple CarbonCpu==0.6
```
+ После установки перейти в директорию с установленным пакетом
```
cd ./venv/lib/python3.6/site-packages/CarbonCpu/
```
+ Установить зависимости
```
pip3 install -r requirements.txt
```
+ Установить requests в python2
 ```
pip2 install requests
```
### Управление демоном - клиентом
***Запуск*** в директории с установленным пакетом выполнить
```
python2.7 client_cpu.py start
```
***Остановка*** в директории с установленным пакетом выполнить
```
python2.7 client_cpu.py stop
```
Параметры port и address записаны в файле client.conf

### Запуск сервера
В директории с установленным пакетом выполнить
```
python3 manage.py runserver
```
Сервер будет запущен по адресу
```
http://127.0.0.1:8000/
```