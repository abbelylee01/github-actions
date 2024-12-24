# important information
This is a demo repository for practicing github for dbt.

# deployment details
Explanation of New Steps
Build Project:

Runs python setup.py sdist bdist_wheel, which:
- Creates a source distribution (sdist) and a wheel distribution (bdist_wheel).
- Outputs the build files to the dist/ directory.
- Upload Build Artifacts:

Uses actions/upload-artifact@v3 to save the dist/ directory as an artifact in your GitHub Actions workflow.
You can download this artifact for deployment or further processing.

# Before running in CI/CD

Before running in CI/CD, test the build process locally:
Build: python setup.py sdist bdist_wheel
Install locally for testing: pip install dist/simple_python_project-0.1.0-py3-none-any.whl

to test locally 
- run pip install --force-reinstall dist/simple_python_project-0.1.0-py3-none-any.whl
- run simple-python

# To run the main.py module directly, you must explicitly include the src directory in the PYTHONPATH:

- PYTHONPATH=/Users/abiodunadeoye/KINGS-PLATFORM/CICD/Project_cicd/src python -m simple_python_project.main
- export PYTHONPATH="/Users/abiodunadeoye/KINGS-PLATFORM/CICD/Project_cicd/src:$PYTHONPATH"
- python -m simple_python_project.main


#  to clean uo

python setup.py clean --all
- .git prehook



