from setuptools import setup, find_packages


setup(name='projectname',
      version='0.0.1',
      py_modules=['modules'],
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'Click',
          'requests',
          'nose'
      ],
      package_data={'': ['*.txt', '*.lst']},
      entry_points='''
        [console_scripts]
        projectname=projectname:cli
    ''',
      test_suite='nose.collector',
      tests_require=['nose'],
      )
