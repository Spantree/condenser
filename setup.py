from setuptools import setup

requires = [
    "toposort",
    "psycopg2-binary",
    "mysql-connector-python"
]

setup(name='condenser',
      version='0.1',
      description='Condenser database subsetting tool',
      url='https://github.com/Spantree/condenser',
      author='Spantree, based on original work by TonicAI',
      author_email='gary@spantree.net',
      license='MIT',
      packages=['condenser'],
      install_requires=requires,
      zip_safe=False)