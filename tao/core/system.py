# -*- coding: utf-8 -*-
"""
System relative operations.
"""
import os
import shlex
import subprocess


__all__ = ('execute',)


def execute(command, cwd=os.path.curdir, **options):
    """
    Run the system command with optional options.

    Args:
        * command: system command.
        * cwd: current working directory.
        * verbose: direct options for :func:`subprocess.Popen`.

    Returns:
        Opened process, standard output & error.
    """
    process = subprocess.Popen(shlex.split(command), cwd=cwd, **options)
    stdout, stderr = process.communicate() 
    return process, stdout, stderr
