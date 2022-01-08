# -*- coding: utf-8 -*-
from chardet import detect
import docker, re, random
from time import sleep

client = docker.from_env()

def port():
    port = random.randrange(150,59999)
    return int(port)

class containers_build:
    def __init__(self) -> None:
        pass

    def build():
        ports = int(port())

        dockerbuild = client.containers.run(ports={'8888/tcp': ports} ,hostname="HOSTING", image="teamsirius921/dplyapp:ubuntuapp", detach=True)
        dockerbuild.start()

        sleep(1)

        data1 = str(dockerbuild.exec_run(cmd='jupyter server list'))
        data = [{'dockerid' : dockerbuild.short_id, 'port' : ports, 'password' : data1[88:136]}]
        return list(data)