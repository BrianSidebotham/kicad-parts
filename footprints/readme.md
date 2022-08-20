## Getting Started

You can simply clone this repository somewhere are reference it in your global library table.

To develop the parts, create a python virtual environment and update the packages that should already be available:

```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install --upgrade setuptools wheel pip
```

Install the requirements for this library:

```shell
$ python -m pip install -r requirements.txt
```

Each library comes with a python script that will generate the footprints as necessary. For example, to re-build the `connectors-te-valulok-vertical-no-pegs` library:

```shell
(venv) $ cd connectors-te-valulok-vertical-no-pegs.pretty
(venv) $ python3 generate.py
