# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------


def text_deco(text, char='-', show=True, over=False):
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
