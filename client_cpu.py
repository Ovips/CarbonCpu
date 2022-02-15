#! /usr/bin/env python
## -*- coding: utf-8 -*-

import sys
import subprocess
import requests
import logging
import os
import time
import ConfigParser

from daemon import Daemon

LOG_FILE = 'var/log/client_cpu.log'
if not os.path.exists(LOG_FILE):
    file_path, file_name = os.path.split(LOG_FILE)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename=LOG_FILE)


class Client(Daemon):

    def __init__(self, pidfile, ip='127.0.0.1', port='8000'):
        super(Client, self).__init__(pidfile)
        self.ip = ip
        self.port = port

    def run(self):
        while True:
            try:
                raw_load = subprocess.check_output('cat /proc/loadavg', shell=True).decode('ascii')
                load_avg = str(raw_load).split()[0]
                nproc = subprocess.check_output('nproc', shell=True).decode('ascii')
                load_percent = '{:.0f}'.format(float(load_avg) / float(nproc) * 100)
                address = 'http://{}:{}/api/add_cpu_load/'.format(self.ip, self.port)
                try:
                    r = requests.post(address, data={'load': load_percent})
                    if r.status_code == 201:
                        logging.info('Данные успешно отправлены на сервер {0}:{1}. Загрузка {2}%'.format(self.ip, self.port, load_percent))
                    else:
                        logging.info('Данные не удалось отправить. Статус код {}'.format(r.status_code))
                except Exception as e:
                    logging.info('Не удалось отправить данные. {}'.format(e))
            except Exception as e:
                logging.info('Ошибка работы демона {}'.format(e))
            time.sleep(10)


if __name__ == '__main__':
    configParser = ConfigParser.RawConfigParser()
    configFilePath = 'client.conf'
    configParser.read(configFilePath)
    conf_ip = configParser.get('client-config', 'ip')
    conf_port = configParser.get('client-config', 'port')
    daemon = Client('/tmp/daemon-example.pid', conf_ip, conf_port)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            print('Логи работы демона находятся в {}'.format(os.path.abspath(LOG_FILE)))
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print('Unknown command')
            sys.exit(2)
        sys.exit(0)
    else:
        print('usage: %s start|stop|restart' % sys.argv[0])
        sys.exit(2)
