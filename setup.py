from setuptools import setup, find_packages

setup(
    name="test_release",                           # Nombre del paquete
    version="0.1.0",                                # Versión inicial
    packages=find_packages(),                       # Paquetes a incluir
    description="Un paquete pip simple de saludo",  # Breve descripción
    author="Yofran Perdomo",                         # Tu nombre
    author_email="yofran795@gmail.com",                 # Tu correo electrónico
    url="https://github.com/yofranexp/test_release",     # URL del proyecto
)