# grimlock

A data transform GUI for the systematic review toolchain.

## Quickstart

Initial setup:

```batch
:: make sure it's python 3.9
python -V

:: install
python -m pip install -U pip
python -m pip install install dist\grimlock-0.0.1-py3-none-any.whl
```

Then, to run the program:

```batch
:: run the program
python -m grimlock
```

## Developer setup

```bash
# clone project
git clone https://github.com/rabstejnek/grimlock.git
cd grimlock

# create virtual environment and activate
python -m venv venv --prompt grimlock
source venv/bin/activate  # or venv\Scripts\activate on windows.

# install packages
python -m pip install -U pip
pip install -r requirements_dev.txt

# test local install
python -m grimlock

# these should work on mac/linux/windows
make test   # run tests
make lint   # identify formatting errors
make format # fix formatting errors when possible
make build  # build a python wheel
```

Github actions are setup to execute whenever code is pushed to check code formatting and successful tests. In addition, when code is pushed to the `main` branch, a wheel artifact is created and stored on github.
