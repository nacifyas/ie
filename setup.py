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
        # 'pandas==2.2.2',
        # 'seaborn==0.13.2',
        # 'matplotlib==3.8.4'
    ],
)
