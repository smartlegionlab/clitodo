# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
import json
import os

from pathlib import Path

import click
from smartprinter.printers import Printer
from smartcliapp.climanager import CliManager

from clitodo.task_man import TaskMan


class Commander:

    def __init__(self):
        self._printer = Printer()
        self._cli_man = CliManager()
        self._task_man = TaskMan()
        self.file_path = Path(Path.home()).joinpath('.clitodo_tasks.json')
        self.open()

    def run(self):

        while True:
            self._printer.smart.echo('Main menu', '=')
            self._printer.smart.echo(f'My Tasks: {self._task_man.count}')
            print('a: add task')
            print('s: show tasks')
            print('q: quit')
            self._printer.smart.echo()

            char = click.getchar()

            if char.lower() in ('q', 'й'):
                self.quit()
                break
            elif char.lower() in ('a', 'ф'):
                self.add()
            elif char.lower() in ('s', 'ы'):
                self.show()
                continue
            else:
                continue

            self._printer.smart.echo()
            input('Enter to continue...')

    def open(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.decoder.JSONDecodeError:
                    data = {}

            if data:
                for k, v in data.items():
                    self._task_man.make(k, v['body'], v['date'])
        else:
            self.save()

    def save(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            data = {task.title: {'body': task.body, 'date': task.date}
                    for task in self._task_man.tasks.values()}
            json.dump(data, f, indent=4, ensure_ascii=False)

    def add(self):
        self._printer.smart.echo('Add new task:', '=')
        title = input('Enter title: ') or 'New task'
        self._printer.smart.echo()
        body = input('Enter body: ') or 'New task description'
        self._task_man.make(title, body)
        self._printer.smart.echo()
        print(f'Task "{title}" added successfully!')

    @classmethod
    def _show_tasks(cls, num_tasks):
        for n, task in num_tasks.items():
            print(f'{n}: {task.title}')

    @classmethod
    def _text_deco(cls, text, char='-', show=True, over=False):
        deco = char * len(text)

        if over:
            msg = f'{deco}\n'
        else:
            msg = ''

        msg += f'{text}\n'
        msg += char * len(text)
        if show:
            print(msg)
        return msg

    def show(self):
        while True:
            self._printer.smart.echo('My Tasks:', '=')
            tasks = self._task_man.tasks
            num_tasks = {n: task for n, task in enumerate(tasks.values(), 1)}

            if num_tasks:
                self._show_tasks(num_tasks)
            else:
                print('No tasks...')
                self._printer.smart.echo()
                break

            self._printer.smart.echo()

            try:
                n = input('Enter task number or [<b> + <enter>] to back: ')

                if n in ('b', ''):
                    break

                n = int(n)

                if n not in num_tasks:
                    raise ValueError

            except ValueError:
                continue

            task = num_tasks[n]

            while True:
                self._printer.smart.echo()
                self._printer.smart.echo('Task selected:', '=')
                print()
                print('Name:')
                self._text_deco(f'  {task.title}', over=True)
                print('Body:')
                self._text_deco(f'  {task.body}', over=True)
                print('Date:')
                self._text_deco(f'  {task.date}', over=True)
                print()
                self._printer.smart.echo('Available actions')
                print('e: edit')
                print('r: remove')
                print('b: back')
                self._printer.smart.echo()

                char = click.getchar()

                if char.lower() in ('b', 'и'):
                    break
                elif char.lower() in ('e', 'у'):
                    self._edit_task(task)
                elif char.lower() in ('r', 'к'):
                    self._remove_task(task)
                break

    def _remove_task(self, task):
        self._printer.smart.echo('Remove task:', '=')
        if self._cli_man.get_action(f'Remove task {task.title}?'):
            print(f'Remove: {task.title}')
            self._task_man.remove(task)

    def _edit_task(self, task):
        self._printer.smart.echo('Edit task:')
        self._printer.smart.echo('New title:')
        self._text_deco(f'old title: ')
        self._text_deco(task.title)

        title = input('Enter title: ')

        if not title:
            title = task.title

        self._printer.smart.echo()
        self._printer.smart.echo('Enter new body:')
        self._text_deco('old body: ')
        self._text_deco(task.body)

        body = input('Enter body: ')

        if not body:
            body = task.body

        self._task_man.remove(task)

        task.title = title
        task.body = body

        self._task_man.add(task)

    def quit(self):
        self.save()
