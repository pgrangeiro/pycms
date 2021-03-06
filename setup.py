from distutils.core import setup


setup(
    name='PyCMS',
    version='1.0',
    description='Python CMS lib',
    author='Paula Grangeiro',
    author_email='contato@paulagrangeiro.com.br',
    url='https://github.com/pgrangeiro/pycms',
    license='GNU 3.0',
    extras_require={
        'test': ['mock'],
    },
)
