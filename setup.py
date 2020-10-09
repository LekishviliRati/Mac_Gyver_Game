# -*- coding: utf-8 -*-

from cx_Freeze import setup, Executable

setup(name='hello',
      version='0.1',
      description='Sample cx_Freeze script',
      executables=[Executable("main.py")]
      )