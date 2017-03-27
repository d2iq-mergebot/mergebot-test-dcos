# DC/OS - The Datacenter Operating System

The easiest way to run microservices, big data, and containers in production.


# What is DC/OS?

Like traditional operating systems, DC/OS is system software that manages computer hardware and software resources and provides common services for computer programs.

Unlike traditional operating systems, DC/OS spans multiple machines within a network, aggregating their resources to maximize utilization by distributed applications.

To learn more, see the [DC/OS Overview](https://dcos.io/docs/latest/overview/).


# How Do I...?

- Learn More - <https://dcos.io/>
- Find the Docs - <https://dcos.io/docs/>
- Install - <https://dcos.io/install/>
- Get Started - <https://dcos.io/get-started/>
- Get Help - <http://chat.dcos.io/>
- Join the Discussion - <https://groups.google.com/a/dcos.io/d/forum/users>
- Report an Issue - <https://dcosjira.atlassian.net>
- Contribute - <https://dcos.io/contribute/>


# Releases

DC/OS releases are publicly available on <http://dcos.io/releases/>

Release artifacts are managed by Mesosphere on Amazon S3, using a CloudFront cache.

To find the git SHA of any given release, check the latest commit in the versioned branches on GitHub: <https://github.com/dcos/dcos/branches/>

| Release Type | URL Pattern |
|--------------|--------------------|
| Latest Stable| `https://downloads.dcos.io/dcos/stable/dcos_generate_config.sh` |
| Specific Stable Release | `https://downloads.dcos.io/dcos/stable/commit/<git-sha>/dcos_generate_config.sh` |
| Latest Early Access | `https://downloads.dcos.io/dcos/EarlyAccess/dcos_generate_config.sh` |
| Specific Early Access Release | `https://downloads.dcos.io/dcos/EarlyAccess/commit/<git-sha>/dcos_generate_config.sh` |
| Latest Master | `https://downloads.dcos.io/dcos/testing/master/dcos_generate_config.sh` |
| Specific PR, Latest Build	| `https://downloads.dcos.io/dcos/testing/pull/<github-pr-number>/dcos_generate_config.sh` |


# Development Environment

**Linux is required for building and testing DC/OS.**

1. Linux distribution:
  - Docker doesn't have all the features needed on OS X or Windows
  - `tar` needs to be GNU tar for the set of flags used
1. [tox](https://tox.readthedocs.org/en/latest/)
1. git 1.8.5+
1. Docker 1.11
  - [Install Instructions for various distributions](https://docs.docker.com/engine/installation/). Docker needs to be configured so your user can run docker containers. The command `docker run alpine  /bin/echo 'Hello, World!'` when run at a new terminal as your user should just print `"Hello, World!"`. If it says something like "Unable to find image 'alpine:latest' locally" then re-run and the message should go away.
1. Python 3.5
  - Arch Linux: `sudo pacman -S python`
  - Fedora 23 Workstation: Already installed by default / no steps
  - Ubuntu 16.04 LTS:
    - [pyenv-installer](https://github.com/yyuu/pyenv-installer)
    - Python dependencies: `sudo apt-get install make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils liblzma-dev`
    - Install Python 3.5.2: `pyenv install 3.5.2`
    - Create DC/OS virtualenv: `pyenv virtualenv 3.5.2 dcos`
    - Activate environment: `pyenv activate dcos`
1. Over 10GB of free disk space
1. _Optional_ pxz (speeds up package and bootstrap compression)
  - ArchLinux: [pxz-git in the AUR](https://aur.archlinux.org/packages/pxz-git). The pxz package corrupts tarballs fairly frequently.
  - Fedora 23: `sudo dnf install pxz`


# Unit Tests

Unit tests can be run locally but require the [development environment](#development-environment) specified above.

```
tox
```

[Tox](https://tox.readthedocs.io/en/latest/) is used to run the codebase unit tests, as well as coding standard checks. The config is in `tox.ini`.


# Integration Tests

Integration tests can be run on any deployed DC/OS cluster. For installation instructions, see <https://dcos.io/install/>.

Integration tests are installed via the [dcos-integration-test](./packages/dcos-integration-test/) Pkgpanda package.

## Minimum Requirements

- 1 master node
- 2 private agent nodes
- 1 public agent node
- Task resource allocation is currently insignificantly small
- DC/OS itself requires at least 2 (virtual) cpu cores on each node

## Instructions
