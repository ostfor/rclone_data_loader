"""
Helping tools

Copyright 2019 Denis Brailovsky, denis.brailovsky@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import json
import os
from pathlib import Path

DEFAULT = {'TEMP': '/tmp/~temp/',
           'REMOTE_NAME': 'MyGoogleDrive',
           'REMOTE_DIR': 'NN/Dataset',
           'ARCH_NAME': 'dataset'}


class Config(object):
    def __init__(self, **args):
        self.__dict__ = args


def create_not_ex(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder


def get_config(dir_path, project_name=None):
    if project_name is None:
        project_name = os.path.basename(dir_path)
    cfg_folder = create_not_ex(os.path.join(str(Path.home()), ".rclone_data_loader", project_name))
    cfg_name = os.path.join(cfg_folder, "load.conf")
    cfg_dict = DEFAULT
    cfg_dict["DIR_PATH"] = dir_path
    if not os.path.exists(cfg_name):
        with open(cfg_name, 'w') as f:
            json.dump(cfg_dict, f)
    else:
        with open(cfg_name, 'r') as f:
            cfg_dict = json.load(f)
    cfg_dict["REMOTE"] = "{}:{}/{}".format(cfg_dict["REMOTE_NAME"], cfg_dict["REMOTE_DIR"],
                                           os.path.basename(cfg_dict["DIR_PATH"]))
    return Config(**cfg_dict)
