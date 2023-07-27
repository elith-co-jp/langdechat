from setuptools import setup, find_packages

setup(
    name='langdechat',
    version='0.1.0',
    url='https://github.com/yourusername/langdechat',
    author='beluuuuuuga',
    author_email='author@gmail.com',
    description='Description of my package',
    packages=find_packages(),    
    install_requires=[
        'langchain==0.0.240',
    ],
)
