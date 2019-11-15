#! /usr/bin/env python3
# -*-encoding: utf-8 -*-
# logging设置
import mylog

# 携程来做这些事情来测试
import asyncio, os, json, time

from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b"<html><head></head><body><h1>Awesome Hello World! </h1></body></html>")

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), "127.0.0.1", 9000)
    mylog.infoLog("server started at http://127.0.0.1:9000....")
    return srv


if __name__ == "__main__":
    mylog.infoLog("app is start !")
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()

