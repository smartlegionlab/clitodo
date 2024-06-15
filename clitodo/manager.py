# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
from smartcliapp.informer import Informer

from clitodo.commander import Commander
from clitodo import __version__


class AppMan(Informer):
    commander = Commander()
    name = 'clitodo'
    title = 'Cli ToDo'
    description = 'Console task manager'
    version = __version__
    copyright = 'Copyright © 2018-2024, A.A. Suvorov'
    url = 'https://github.com/smartlegionlab/'
