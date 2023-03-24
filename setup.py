from __future__ import with_statement
from setuptools import setup, find_packages

__version__ = None

with open('README.md') as f:
    long_description = f.read()

setup(name='greensms',
      version='2.0.1',
      description='GREENSMS API: SMS, Call, Voice, VK, WhatsApp, Viber, HLR, Pay',
      url='https://github.com/greensms-ru/greensms-python',
      author='GreenSMS',
      author_email='support@greensms.ru',
      license='MIT',
      packages=find_packages(exclude=['tests', 'tests*']),
      install_requires=[
          'requests',
          'six',
          'twine',
          'cerberus',
          'pyhumps'
      ],
      extras_require={
          ':python_version<"3.0"': [
              "requests[security] >= 2.0.0",
              "pyhumps == 3.0.2",
          ],
          ':python_version>="3.0"': [
              "requests >= 2.0.0",
              "pyhumps >= 3.5.0"
          ],
      },
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      include_package_data=True,
      keywords=['greensms', 'sms', 'sms-api', 'call-for-code',
                'rest', 'api', 'viber', 'whatsapp'],
      long_description=long_description,
      long_description_content_type='text/markdown'
      )
