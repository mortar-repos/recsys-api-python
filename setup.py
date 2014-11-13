try:
    from setuptools import setup
except:
    from distutils.core import setup

try:
    long_description = []
    for line in open('README.md'):
        # Strip all images from the pypi description
        if not line.startswith('!') and not line.startswith('```'):
            long_description.append(line)
except IOError:
    # Temporary workaround for pip install
    long_description = ''

setup(name='recsys-api-python',
      version='0.1.0',
      description='Python API for Mortar Recsys',
      long_description=long_description,
      author='Mortar Data',
      author_email='info@mortardata.com',
      url='http://github.com/mortardata/recsys-api-python',
      namespace_packages = [
                  'mortar_recsys'
      ],
      packages=[
          'mortar_recsys.api'
      ],
      license='LICENSE.txt',
      install_requires=[
          'requests'
      ]
)
