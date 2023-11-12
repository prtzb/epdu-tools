from distutils.core import setup

setup(
    name='epdutools',
    version='1.0',
    py_modules=['epdutools.driver_http', 'epdutools.driver_serial', 'epdutools.exceptions', 'epdutools.validation'],
    install_requires=[
        'requests>=2.22',
    ]
)