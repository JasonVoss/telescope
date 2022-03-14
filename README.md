  [![Build status](https://github.com/astronomer/telescope/workflows/build/badge.svg?branch=main&event=push)](https://github.com/astronomer/telescope/actions?query=workflow%3Abuild)
  [![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/astronomer/telescope/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
  [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
  [![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
  [![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/astronomer/telescope/blob/main/.pre-commit-config.yaml)
  [![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/astronomer/telescope/releases)

# Telescope
<p align="center">
  <img src="resources/astro.png" alt="Astronomer Telescope Logo" />
</p>


A tool to observe distant (or local!) Airflow installations, and gather metadata or other required data.

# Installation
*optionally*, create a virtualenv called `venv` (or anything else ) in the current directory for easy cleanup
```shell
python -m venv venv
source venv/bin/activate 
```

Install Telescope using Pip from Github

```shell
python -m pip install telescope --find-links https://github.com/astronomer/telescope/releases/
```

# Quickstart - Kubernetes Autodiscovery Assessment Mode

This will work if your Airflows are in Kubernetes and were deployed with one of the major Helm charts (
and `component=scheduler` is used to identify the schedulers). It will use Helm to interrogate the installation, and
connect to the Airflow schedulers to gather metadata

```shell
telescope --kubernetes
```
You should now have a `data.json` - which is an intermediate data payload

# Quickstart - SSH Assessment Mode
This will work if your Airflow's are on hosts accessible via SSH and SSH is configured to connect to all of these hosts (e.g. you have `~/.ssh/config` with entries for all hosts)
Create a `hosts.yaml` file, like this, enumerating every host:
```shell
ssh:
  - host: airflow.foo1.bar.com
  - host: airflow.foo2.bar.com 
  - host: ...
```

```shell
telescope -f hosts.yaml
```
You should now have a `data.json` - which is an intermediate data payload

# Compatability Matrix
Telescope is been tested against the following Airflow versions:
- "2.2.1", "2.1.3", "1.10.15", "1.10.10"

Telescope is tested with the following Metadata Database Backends:
- (automated) PostgreSQL, SQLite
- (manually) MySQL, SQLServer

Telescope is tested on the following versions of Python:
- 3.9

Telescope is tested on the following Operating Systems:
- Ubuntu
- Mac (arm64)

# Usage

```shell
$ telescope --help                                                
Usage: telescope [OPTIONS]

  Telescope - A tool to observe distant (or local!) Airflow installations, and
  gather usage metadata

Options:
  --version                      Show the version and exit.
  --local                        Airflow Reporting for local Airflow
                                 [default: False]
  --docker                       Autodiscovery and Airflow reporting for local
                                 Docker  [default: False]
  --kubernetes                   Autodiscovery and Airflow reporting for
                                 Kubernetes  [default: False]
  -l, --label-selector TEXT      Label selector for Kubernetes Autodiscovery
                                 [default: component=scheduler]
  --cluster-info                 Get cluster size and allocation in Kubernetes
                                 [default: False]
  --verify                       Introspect Helm installation information for
                                 Reporting and Verification purposes
                                 [default: False]
  --versions                     checks versions of locally installed tools
                                 [default: False]
  -f, --hosts-file PATH          Hosts file to pass in various types of hosts
                                 (ssh, kubernetes, docker) - See README.md for
                                 sample
  -p, --parallelism INTEGER      How many cores to use for multiprocessing
                                 [default: (Number CPU)]
  --gather / --no-gather         Gather data about Airflow environments
                                 [default: gather]
  --report / --no-report         Generate report summary of gathered data
                                 [default: no-report]
  --charts / --no-charts         Generate charts of summary of gathered data
                                 [default: no-charts]
  --summary / --no-summary       Generate summary text file of gathered data
                                 [default: no-summary]
  --upload / --no-upload         Upload charts to get access to rich reporting
                                 [default: no-upload]
  -n, --organization-name TEXT   Denote who this report belongs to, e.g. a
                                 company name
  --report-type [json|csv|xlsx]  What report type to generate
  -o, --data-file PATH           Data file to write intermediate gathered
                                 data, can be '-' for stdout
  --help                         Show this message and exit.
```

# Requirements
## Locally - Python
- Python >=3.8
- `pip`

## Locally - Docker or Kubernetes or SSH Airflow Assessment modes
- **Docker**: Permissions to Exec Containers, `docker.sock` Access locally
- **Kubernetes**: Permission to List Nodes and Exec in Pods, `KUBECONFIG` set locally
- **SSH**: Credentials to connect to all hosts, SSH Access configured locally
- **Local**: Permission to execute Python locally

## Remote Airflow Requirements
- Airflow Scheduler >1.10.5
- Python 3
- Curl
- Postgresql/Mysql/Sqlite Metadata Database (support not guaranteed for other backing databases)
- **Kubernetes**: Kubernetes Scheduler has label `component=scheduler` (or `--label-selector` specified)

# Input
## Local autodiscovery
Either use `--local` or have an empty `local` key in your hosts file to enable autodiscovery.
Autodiscovery simply runs the Airflow Report as a process, assuming that an Airflow Scheduler is being run
on the current node.

## Docker autodiscovery
Either use `--docker` or have an empty `docker` key in your hosts file to enable autodiscovery.
Autodiscovery searches for containers running locally that contain "scheduler" in the name and returns
the container_id

- `hosts.yaml`
```
docker: 
```

## Kubernetes autodiscovery
Either use `--kubernetes` or an empty `kubernetes` in your hosts file to enable autodiscovery.
Autodiscovery searches for pods running in the Kubernetes cluster defined by `KUBEPROFILE` 
in any namespace, that contain the label `component=scheduler` (or another label defined by `--label-selector`), 
and returns the namespace, name, and container (`scheduler`)

- `hosts.yaml`
```
kubernetes: 
```

## Example `hosts.yaml` input 
use `-f hosts.yaml`
```
local:

docker:
  - container_id: demo9b25c0_scheduler_1

kubernetes:
  - namespace: astronomer-amateur-cosmos-2865
    name: amateur-cosmos-2865-scheduler-bfcfbd7b5-dvqqr
    container: scheduler

ssh:
  - host: 1.2.3.4
  - host: foo.com
```

# Extra Functionality
## Versions
`--versions` - checks installed versions of various tools, see [config.yaml](config.yaml) for more details.

## Precheck
`--precheck` - ensures the environment, useful before installing the Astronomer Enterprise chart

## Label Selection
`--label-selector` allows Kubernetes Autodiscovery to locate Airflow Deployments with alternate key/values. 
The default is `component=scheduler`, however, if your Airflows contain `role=scheduler` instead, you would 
use `--label-selector "role=scheduler"`.


# DATA SHEET
## Data Collected
The following Data is collected, which is then assembled into the `Outputs` mentioned below

### `report.json`
The name of this file can vary depending on what options were passed to the tool. There is an intermediate output called `report.json` collects all the data gathered, and is utilized to generate the report outputs.

#### Airflow Report
This information is saved under the `airflow` key, under the host_type key and the host key. E.g. `kubernetes.mynamespace|myhost-1234-xyz.airflow_report` or `ssh.my_hostname.airflow_report`

Using `curl`, `airflow_report.py` is piped and executed on the remote host (the host or container running the airflow scheduler). The performance impact of this report is negligible
- `airflow.version.version` output to determine Airflow's version
- `airflow.providers_manager.ProvidersManager`'s output, to determine what providers and versions are installed
- `socket.gethostname()` to determine the hostname
- `pkg_resources` to determine installed python packages and versions
- `airflow.configuration.conf` to determine Airflow configuration settings and what is modified from defaults. Sensitive values are redacted
- `os.environ` to determine what airflow settings, variables, and connections are set via ENV vars. Names only
- the `pools` table is retrieved to list Airflow pools and sizes from the Airflow metadata db
- the `dag` table is inspected from the Airflow metadata db
- the `connection` table is fetched from the Airflow metadata db
- the `task_instance` table is analyzed from the Airflow metadata db


#### Verify
This information is saved under the `helm` key
- `helm ls -aA -o json` and `helm get values` are run. The latter redacts sensitive information.

#### Pre-Check
This special mode runs a pod `bitnami/postgresql` and gets Kubernetes secrets (`astronomer-tls`, `astronomer-bootstrap`) to verify connectivity and information relating to Astronomer Enterprise installations.

### `--versions` Output
See [here](https://github.com/astronomer/telescope/blob/main/telescope/config.yaml) for the most recent description of what is gathered with the local flag. Generally, versions are gathered for the following tools:
- python
- helm
- kubectl
- docker
- astro
- docker-compose
- os
- aws
- gcp
- az

Additionally, 
- `aws_id` checks `aws sts get-caller-identity`

## Pre-requisites
See [Requirements](#requirements) above.
