"""
Does the following:
# 1. Removes the example project if it isn't going to be used
"""

import os
import shutil
from pathlib import Path

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_example_project(project_directory):
    """Removes the taskapp if celery isn't going to be used"""
    # Determine the local_setting_file_location
    location = os.path.join(PROJECT_DIRECTORY, "tests", "example")
    shutil.rmtree(location)


def insert_python_versions(versions: str = ""):
    env_text = Path(".github/actions.yml").read_text()
    versions_arr = ""
    if "py36" in versions:
        versions_arr += "3.6, "
    if "py37" in versions:
        versions_arr += "3.7, "
    if "py38" in versions:
        versions_arr += "3.8, "
    if "py39" in versions:
        versions_arr += "3.9 "

    env_text = env_text.replace("__PYTHON_VERSIONS__", str(versions_arr))

    Path(".github/actions.yml").write_text(env_text)
    print("Added python versions to .github/actions.yml file.")


# 1. Removes the example project if it isn't going to be used
if "{{ cookiecutter.create_example_project }}".lower() == "n":
    remove_example_project(PROJECT_DIRECTORY)
    insert_python_versions("{{cookiecutter.python_versions}}")
