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
pip install -i https://test.pypi.org/simple/ CarbonCpu==0.1
```
+ После установки перейти в директорию с установленным пакетом
```
cd ./venv/lib/python3.6/site-packages/CarbonCpu/
```
+ Установить зависимости
```
pip install -r requirements.txt
```
### Управление демоном - клиентом
####Запуск
В директории с установленным пакетом выполнить
```
python2.7 client_cpu.py start
```
####Остановка
В директории с установленным пакетом выполнить
```
python2.7 client_cpu.py stop
```
Параметры port и address записаны в файле client.conf

### Запуск сервера
В директории с установленным пакетом выполнить
```
python manage.py runserver
```