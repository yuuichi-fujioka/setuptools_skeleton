import setuptools
import sys



with open('requirements.txt' if sys.version_info < (3,0,0) else 'requirements-py3.txt') as f:
    requirements = f.read().splitlines()

with open('README.rst') as f:
    description = f.read()

setuptools.setup(
    name='skeleton',
    version='0.1',
    description=description,
    url='http://github.com/yuuichi-fujioka/setuptools_skeleton.git',
    author='Yuuichi Fujioka',
    author_email='fujioka.yuuichi@gmail.com',
    entry_points={
        'console_scripts': [
            'skeleton=skeleton.main:main',
        ],
        'oslo.config.opts': [
            'skeleton=skeleton.config:list_opts',
        ],
    },
    classifiers=[
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    packages=['skeleton'],
    install_requires=requirements
)
