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


def insert_python_versions(versions: str = "", repo_name: str = ""):
    env_text = Path(".github/workflows/actions.yml").read_text()
    versions_arr = ""
    if "py36" in versions:
        versions_arr += "3.6, "
    if "py37" in versions:
        versions_arr += "3.7, "
    if "py38" in versions:
        versions_arr += "3.8, "
    if "py39" in versions:
        versions_arr += "3.9 "

    new_env_text = env_text.replace("__PYTHON_VERSIONS__", str(versions_arr))
    new_env_text = new_env_text.replace("__REPO_NAME__", str(repo_name))

    Path(".github/workflows/actions.yml").write_text(new_env_text)
    print("Added python versions to .github/workflows/actions.yml file.")


# 1. Removes the example project if it isn't going to be used
if "{{ cookiecutter.create_example_project }}".lower() == "n":
    remove_example_project(PROJECT_DIRECTORY)
if "{{ cookiecutter.create_example_project }}".lower() in ["n", "y"]:
    insert_python_versions("{{cookiecutter.python_versions}}", "{{ cookiecutter.repo_name }}")
