import glob
import os
import shutil

from setuptools import Command, setup

class clean(Command):
    user_options = []
    CLEAN_DIRS = [
        "./build",
        "./dist",
        *[dir for dir in glob.glob("./**/*.egg-info", recursive=True)],
        *[dir for dir in glob.glob("./**/__pycache__", recursive=True)],
    ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for dir in self.CLEAN_DIRS:
            dir = os.path.relpath(dir)
            for path in glob.glob(os.path.join(dir, "**/*"), recursive=True):
                print("removing", path)
            for path in glob.glob(dir):
                print("removing", path)
            if os.path.exists(dir):
                shutil.rmtree(dir)

setup(cmdclass={"clean": clean})
