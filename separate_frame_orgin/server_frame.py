#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import frame

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application


class IndexHandler(RequestHandler):
    def get(self):
        self.write(json.dumps({"code": 0}))

    def post(self):
        self.write(json.dumps({"code": 10}))


class FileUploadHander(RequestHandler):
    def get(self):
        self.write("hello")

    def post(self):
        upload_path = os.path.join(os.path.dirname(__file__), 'files')  # 文件的暂存路径
        file_metas = self.request.files.get('file')  # 提取表单中‘name’为‘file’的文件元数据
        print(file_metas)
        for meta in file_metas:
            filename = meta['filename']
            print(filename)
            # print(meta.get('filename', None))
            filebody = meta['body']
            print(filebody)
            file_path = os.path.join(upload_path, filename)
            with open(file_path, 'wb') as up:  # 保存文件到file_path
                up.write(meta['body'])

        file_url = os.path.join(upload_path, filename)
        frame.freme_func(file_url)
        self.write("hi")


def start():
    application = Application(
        [
            (r'/', IndexHandler),
            (r'/file', FileUploadHander),
        ],
        autoreload=True)
    application.listen(8765)
    IOLoop.current().start()


if __name__ == "__main__":
    start()
