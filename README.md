# -
මෙතෙක් හොඳම විෂය පිළිබඳ හොඳම ගුරුවරයා සඳහා කාර්යයන් පිළිබඳ මගේ විසඳුම්

Собственна тут есть 1й Task из 1го пака задач.

Справка по использованию: (пишем в терминале)

  `python Task1_1.py -h`
  
  `python Task1_1.py --help`
  
  выдаст вспомогательную информацию по использованию
  
  ```python Task1_1.py 173.194.222.139```
  
  (обращаемся к google.com)
  
  Получим:
  
IP: 192.168.0.1          ASN: Local

IP: 92.248.191.252       ASN: 51604     COUNTRY:RU      PROVIDER:JSC ER-Telecom Holding

IP: 109.195.104.105      ASN: 51604     COUNTRY:RU      PROVIDER:JSC ER-Telecom Holding

IP: 72.14.215.165        ASN: 15169     COUNTRY:US      PROVIDER:Google LLC

IP: 72.14.215.166        ASN: 15169     COUNTRY:US      PROVIDER:Google LLC

IP: 142.251.53.67        ASN: 15169     COUNTRY:US      PROVIDER:Google LLC

IP: 108.170.250.66       ASN: 15169     COUNTRY:US      PROVIDER:Google LLC

IP: 142.251.238.84       ASN: 15169     COUNTRY:US      PROVIDER:Google LLC

IP: 142.251.238.72       ASN: 15169     COUNTRY:US      PROVIDER:Google LLC

IP: 172.253.51.237       ASN: 15169     COUNTRY:US      PROVIDER:Google LLC

*       *       *

*       *       *

*       *       *

*       *       *

*       *       *

*       *       *

*       *       *

*       *       *

*       *       *

*       *       *

*       *       *

IP: 173.194.222.139      ASN: 15169     COUNTRY:US      PROVIDER:Google LLC




Задача 4 (второй блок) находится в папке DNS
#запуск
1) запускаем DNS.py
2) открываем консольку
3) пишем в нее:
''' nslookup google.com 127.0.0.1 '''
получаем результат



задача 8 (третий блок) лежит отдельным файлом
#запуск
1) открываем файлик Task3_8.py
2) находим там "access_token=?"
3) заходим на сайтик: https://vkhost.github.io/
4) получаем себе токен и вставляем вместо вопросика (см. пункт 2)
5) запускаем и вбиваем id или ссылку на аккаунт VK
   пример:
   '''https://vk.com/ice.druid'''
   '''218821006'''
6) получаем результат в виде списка друзей пользователя онлайн и списка всех друзей
