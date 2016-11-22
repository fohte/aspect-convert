from setuptools import setup

setup(name='aspect-convert',
      version='0.0.1',
      description='A CLI tool for converting aspect ratio of images',
      url='https://github.com/fohte/python-aspect-convert',
      author='Hayato Kawai',
      author_email='fohte.hk@gmail.com',
      license='MIT License',
      packages=[
          'aspect',
      ],
      entry_points={
          'console_scripts': [
              'aspect = aspect.main:main',
          ],
      },
      install_requires=[
          'click',
          'Pillow',
          'numpy',
      ],
      )
