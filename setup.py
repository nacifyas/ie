from setuptools import setup, find_packages

setup(
    name='ie',
    version='1.1',
    author='Nassh',
    author_email='nacifyas@gmail.com',
    description='FastAPI powered backend for IE project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    python_requires='>=3.12',
    packages=find_packages(),
    install_requires=[
        'uvicorn[standard]',
        'fastapi[all]==0.110.1',
        'redis-om==0.2.2',
    ],
)

# [build-system]
# requires = ["setuptools"]
# build-backend = "setuptools.build_meta"

# [project]
# name = "ie"
# version = "1.1"
# authors = [
#     {name="Nassh",email="nacifyas@gmail.com"}
# ]
# description = "FastAPI powered backend for IE project"
# readme = "README.md"
# requires-python = ">=3.12"
# license = {file = "LICENCE"}
# dependencies = [
#     "uvicorn[standart]",
#     "fastapi[all]==0.110.1",
#     "redis-om==0.2.2",
# ]


# [tool.setuptools]
# py-modules = ["app"]
