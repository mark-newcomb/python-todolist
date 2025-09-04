#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, task
from src.main.python.controller.main_controller import MainController
import sys
import os

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.distutils")
use_plugin("python.install_dependencies")

name = "python_todolist"
default_task = "publish"

@init
def set_properties(project):
    project.depends_on("psycopg2-binary")

@init
def initialize(project):
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src', 'main', 'python'))

@task
def run_app():
    print("Running my custom Python script...")
    # Import and call your Python code here
    from src.main.python.main import main
    main()
    print("Script execution complete.")