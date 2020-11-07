# greensms-node

## Documentation

The documentation for the GREENSMS API can be found [here][apidocs].

## Installation

```bash
pipenv install greeensms
```

or

```bash
pip install greeensms
```

## Sample Usage

Check out these [code examples](examples) to get up and running quickly.

```python

from greensms.client import GreenSMS

// Register at my.greeensms.ru first
client = GreenSMS(user='test', password='test')

client.sms.send(to='71231234567', txt='Message to deliver')
print(response.request_id)

```

### Environment Variables

`greensms-python` supports credential storage in environment variables. If no credentials are provided following env vars will be used: `GREENSMS_USER`/`GREENSMS_PASS` OR `GREENSMS_TOKEN`.

### Token Auth

```python

from greensms.client import GreenSMS

// Register at my.greeensms.ru first
client = GreenSMS(token='yourtoken')

client.account.balance()
print(response.balance)

```

## Compatibility

`greensms-python` is compatible with Python 2.7 and Python 3.4 onwards until the latest Python 3.9 version

## Methods

- You can either use username/password combination or auth token to create an object with constructor
- All methods support named \*\*kwargs
- Each API Function is available as `MODULE.FUNCTION()`
- Parameters for each API can be referred from [here][apidocs]
- Response keys by default are available in `snake_case`. If you want to use `camelCase`, then pass `use_camel_case=true`, in the constructor

## Handling Exceptions

- TODO

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
npm install
```

You can run the existing tests to see if everything is okay by executing:

```bash
npm test
```

[apidocs]: https://api.greensms.ru/
