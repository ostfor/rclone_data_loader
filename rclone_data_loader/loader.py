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

from rclone_data_loader.config import get_config, create_not_ex
import shutil
import os
import subprocess


def upload(dir_path):
    config = get_config(dir_path)
    create_not_ex(config.TEMP)
    shutil.make_archive(os.path.join(config.TEMP, config.ARCH_NAME), 'zip', dir_path)
    rclone_sync_command = "rclone sync {} {}".format(config.TEMP, config.REMOTE)
    print(os.listdir(config.TEMP))
    print(rclone_sync_command)
    process = subprocess.Popen(rclone_sync_command.split(), stdout=subprocess.PIPE, cwd=".")
    output, error = process.communicate()
    print("Remote out: ", output)
    print("Remote errors: ", error)
    shutil.rmtree(config.TEMP)


def download(dir_path):
    config = get_config(dir_path)
    create_not_ex(dir_path)
    create_not_ex(config.TEMP)
    rclone_sync_command = "rclone sync {} {}".format(config.REMOTE, config.TEMP)
    process = subprocess.Popen(rclone_sync_command.split(), stdout=subprocess.PIPE, cwd=".")
    output, error = process.communicate()
    print("Remote out: ", output)
    print("Remote errors: ", error)
    # TODO: Rid of hardcode
    shutil.unpack_archive(os.path.join(config.TEMP, config.ARCH_NAME + ".zip"), extract_dir=dir_path)
    shutil.rmtree(config.TEMP)
