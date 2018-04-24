from setuptools import setup, find_packages

setup(name='cloneme',
      version='0.1.2',
      description='A git clone wrapper to make cloning repos easier',
      keywords='git clone wrapper',
      url='http://github.com/LucianoFromTrelew/cloneme',
      author='Luciano Serruya Aloisi',
      author_email='lucianoserruya@gmail.com',
      license='MIT',
      #
      # Con la funcion 'find_packages', indicamos que queremos
      # incluir todos los paquetes que encuentre,
      # exluyendo los que indicamos con el parámetro 'exclude'
      #
      packages=find_packages(exclude=['*tests*']),
      #
      # Indicamos la versión mínima necesaria para correr
      # nuestro paquete
      #
      python_requires='>=3',
      #
      # Indicamos que dependencias
      # (que se puedan encontrar en pip)
      # tiene nuestro paquete
      # install_requires=[
          # 'markdown',
      # ],

      #
      # Indicamos que nuestro paquete va a generar un script
      # entonces se lo va a poder ejecutar desde la consola
      # ingresando 'cloneme'
      #
      entry_points={
          'console_scripts': ['cloneme=cloneme.cloneme:main'],
      },
      #
      # Indicamos que queremos incluir archivos de datos
      # como por ejemplo el README.md en nuestra distribución
      #
      include_package_data=True,
  )
