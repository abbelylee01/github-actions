from setuptools import setup, find_packages

setup(
    name="simple-python-project",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "simple-python=simple_python_project.main:main",
        ],
    },
)
