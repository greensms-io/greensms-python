# greensms-python

![GitHub release (latest by date)](https://img.shields.io/github/v/release/greensms-ru/greensms-python)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/greensms)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/greensms-ru/greensms-python/python-package.yml?branch=main)
![Coveralls github](https://img.shields.io/coveralls/github/greensms-ru/greensms-python)

## Documentation

The documentation for the GREENSMS API can be found [here][apidocs].

## Installation

```bash
pipenv install greensms
```

or

```bash
pip install greensms
```

## Sample Usage

Check out these [code examples](examples) to get up and running quickly.

```python

from greensms.client import GreenSMS

# Register at my.greensms.ru first
client = GreenSMS(user='test', password='test')

response = client.sms.send(to='71231234567', txt='Message to deliver')
print(response.request_id) # or print(response['request_id'])

```

### Environment Variables

`greensms-python` supports credential storage in environment variables. If no credentials are provided following env vars will be used: `GREENSMS_USER`/`GREENSMS_PASS` OR `GREENSMS_TOKEN`.

### Token Auth

```python

from greensms.client import GreenSMS

# Register at my.greensms.ru first
client = GreenSMS(token='yourtoken')

response = client.account.balance()
print(response.balance)

```

## Compatibility

`greensms-python` is compatible with Python 2.7 and Python 3.4 onwards until the latest Python 3.11 version

## Methods

- You can either use username/password combination or auth token to create an object with constructor
- All methods support named \*\*kwargs
- Each API Function is available as `MODULE.FUNCTION()`
- Parameters for each API can be referred from [here][apidocs]
- Response keys can be used as dictionary keys `response['key']` or properties `response.key`
- Response keys by default are available in `snake_case`. If you want to use `camelCase`, then pass `use_camel_case=true`, in the constructor

## Handling Exceptions

- Exceptions for all APIs are thrown with `RestError` class. It extends the default Python Exception class.
- Each error, will have `error`, `code`, `message`, `errorType` fields.
- In case of _Validation Error_, additional params are available to show field-wise rule failures. Can be accessed by `e.params` property on the error object

## Getting help

If you need help installing or using the library, please contact us: [support@greensms.ru](mailto:support@greensms.ru).

If you've instead found a bug in the library or would like new features added, go ahead and open issues or pull requests against this repo!

## Contributing

Bug fixes, docs, and library improvements are always welcome. Please refer to our [Contributing Guide](CONTRIBUTING.md) for detailed information on how you can contribute.
If you're not familiar with the GitHub pull request/contribution process, [this is a nice tutorial](https://gun.io/blog/how-to-github-fork-branch-and-pull-request/).

### Getting Started

If you want to familiarize yourself with the project, you can start by [forking the repository](https://help.github.com/articles/fork-a-repo/) and [cloning it in your local development environment](https://help.github.com/articles/cloning-a-repository/). The project requires [Node.js](https://nodejs.org) to be installed on your machine.

After cloning the repository, install the dependencies by running the following command in the directory of your cloned repository:

```bash
pip install -r requirements.txt
```

In addition to this, we recommend running the setup with [virtualenv](https://virtualenv.pypa.io/), for creating an isolated Python development environment.

GreenSMS has all the unit tests defined under **tests** folder with `_test.py` extension. Although it uses Python Unittest, we recommended that you test with [py.test](http://pytest.org/). PyTest supports Python unit tests out of the box and is faster for running the tests in bulk.

```bash
pytest tests
```

We also support [tox](https://tox.readthedocs.io/) for automate env/interpretor wise testing. Support versions are added to tox.ini. Dependencies added in root requirements.txt are supposed to be added to `tests/requirements.txt` as well.

You can install and run tox for the project with the following commands.

```bash
pip install tox  # Install tox

tox # Run test

```

[apidocs]: https://api.greensms.ru/
