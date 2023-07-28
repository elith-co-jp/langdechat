from setuptools import setup, find_packages

setup(
    name='langdechat',
    version='0.1.1',
    url='https://github.com/yourusername/langdechat',
    author='beluuuuuuga',
    author_email='koki.inoue@elith.co.jp',
    description='Prompt Performance Check Library',
    packages=find_packages(),    
    install_requires=[
        'langchain==0.0.240',
        'datasets>=0.2.0',
        'openai>=0.27.0',
    ],
)
