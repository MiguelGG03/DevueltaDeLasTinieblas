from setuptools import setup

setup(
    name='paquete',
    version='1.0',
    description='Paquete de prueba',
    author='Miguel',
    packages=['paquete.hola','paquete.adios'],
    install_requires=['numpy', 'pandas']
)