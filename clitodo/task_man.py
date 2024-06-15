# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
from datetime import datetime


class Task:
    def __init__(self, title, body='', status=False):
        self._title = title
        self._body = body
        self._date = self._get_date()
        self._status = status

    def switch(self):
        self._status = not self._status

    @property
    def status(self):
        return self._status

    @classmethod
    def _get_date(cls):
        d = datetime.now()
        return d.strftime('%Y-%m-%d %H:%M:%S')

    @property
    def date(self):
        return self._date

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body):
        self._body = body

    def __repr__(self):
        status = '[+]' if self._status else '[-]'
        return f'<Task {self._title} {status}>'


class TaskMan:
    def __init__(self):
        self._tasks = {}

    def add(self, task):
        self._tasks[task.title] = task

    def make(self, title, body='', date=None,):
        self.add(Task(title, body, date))

    def remove(self, task):
        self._tasks.pop(task.title)

    @property
    def tasks(self):
        return self._tasks

    @property
    def count(self):
        return len(self._tasks)

    def get_json_data(self):
        pass

    def __repr__(self):

        return f'<TaskMan {self.count}>'
