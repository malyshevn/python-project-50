### Hexlet tests and linter status:
[![Actions Status](https://github.com/malyshevn/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/malyshevn/python-project-50/actions)
<a href="https://codeclimate.com/github/malyshevn/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/89f1fbfb774e33d38001/maintainability" /></a>
<a href="https://codeclimate.com/github/malyshevn/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/89f1fbfb774e33d38001/test_coverage" /></a>

### Generate difference
CLI tool generating the difference between two files with specified formats (JSON/YML)

<a href="https://asciinema.org/a/7lu0zCMSbyqobMxt2MgZTUJwB" target="_blank"><img src="https://asciinema.org/a/7lu0zCMSbyqobMxt2MgZTUJwB.svg" /></a>

### Download:
`pip install --user git+https://github.com/malyshevn/python-project-50`

*** usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output (default: stylish).
                        Formats: {stylish, plain, json}. ***

Plain
<a href="https://asciinema.org/a/2SP19Ak95YFUJcvcL1WtAB1rl" target="_blank"><img src="https://asciinema.org/a/2SP19Ak95YFUJcvcL1WtAB1rl.svg" /></a>
Stylish
<a href="https://asciinema.org/a/rwIwqpC82aY4K8XwxEnlIVA2M" target="_blank"><img src="https://asciinema.org/a/rwIwqpC82aY4K8XwxEnlIVA2M.svg" /></a>
