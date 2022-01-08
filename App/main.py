# -*- coding: utf-8 -*-
import uvicorn, dply
from dply.build import *
from dply.data import *
from dply.manage import *
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class dockerservice(BaseModel):
    name : str

#API 페이지
@app.get("/",tags=["info"])
async def main_info_webpages():
    return {"Hosting API Version : {0}".format(dply.__version__)}

#사용자 도커 컨테이너 빌드
@app.post("/container/build")
async def api_build(dockerservice : dockerservice):
    date = containers_build.build()
    return container.add_data(dockerservice.name, date[0]["port"], date[0]["password"], date[0]["dockerid"], "start")

#사용자 도커 컨테이너 시작
@app.post("/container/start")
async def api_start(dockerservice : dockerservice):
    containers_service.restart(container.dockerid(dockerservice.name))
    return container.update("start", dockerservice.name)

#사용자 도커 컨테이너 정지
@app.post("/container/stop")
async def api_stop(dockerservice : dockerservice):
    containers_service.stop(container.dockerid(dockerservice.name))
    return container.update("stop", dockerservice.name)

#사용자 도커 컨테이너 강제 종료
@app.post("/container/kill")
async def api_kill(dockerservice : dockerservice):
    containers_service.kill(container.dockerid(dockerservice.name))
    return container.update("stop", dockerservice.name)

#사용자 도커 컨테이너 삭제
@app.post("/container/remove")
async def api_rm(dockerservice : dockerservice):
    containers_service.remove(container.dockerid(dockerservice.name))
    return container.remove(dockerservice.name)

#사용자 도커 컨테이너 웹 리스트 전송
@app.post("/container/info")
async def container_data(dockerservice : dockerservice):
    return container.status(dockerservice.name)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)