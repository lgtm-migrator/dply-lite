# -*- coding: utf-8 -*-
import datetime, json, os
from .manage import *

class container:
    def __init__(self) -> None:
        pass

    # 이메일 테이블 에 데이터 추가
    def add_data(name, port, password, dockerid, status):
        filelocation = '../Data/containers_{0}.json'.format(name)
        jsondata = {
            'name':name,
            'docker id':dockerid,
            'docker port':port,
            'password':password,
            'status':status,
            'time':str(datetime.datetime.now())
        }
        if os.path.isfile(filelocation) == False:
            jsonwrite = open(filelocation, "w",encoding="utf-8")
            json.dump(jsondata, jsonwrite, indent="\t")
            return 'Container add done'
        else:
            containers_service.remove(dockerid)
            return "Have a container with that name"

    # 이메일 테이블에 데이터 업데이트
    def update(status, name):
        filelocation = '../Data/containers_{0}.json'.format(name)
        jsondata = open(filelocation, "r",encoding="utf-8")
        jsonlist = json.load(jsondata)
        chang = jsonlist["status"]="stop"
        jsonwrite = open(filelocation, "a",encoding="utf-8")
        json.dump(chang, jsonwrite, indent="\t")

    # 이메일 테이블에 데이터 삭제
    def remove(name):
        filelocation = '../Data/containers_{0}.json'.format(name)

        if os.path.isfile(filelocation):
            os.remove(filelocation)
            return 'container delete data done'
        else:
            return 'Container has already been deleted'
    
    def status(name):
        filelocation = '../Data/containers_{0}.json'.format(name)
        jsondata = open(filelocation, "r",encoding="utf-8")
        return json.load(jsondata)
    
    def dockerid(name):
        filelocation = '../Data/containers_{0}.json'.format(name)
        jsondata = open(filelocation, "r",encoding="utf-8")
        return json.load(jsondata)['docker id']