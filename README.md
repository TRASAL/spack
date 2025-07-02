# About

This is a spack repository containing radio astronomy software, mostly for ASTRON's ARTS cluster.

# Setup
Clone spack itself and this repository (n.b. this repo is probably _not_ compatible with spack 1.0, so use the latest 0.x version), e.g.:
```
git clone -c feature.manyFiles=true --depth=2 https://github.com/spack/spack.git -b v0.23.1 /usr/local/spack
git clone https://github.com/TRASAL/spack /usr/local/spack/artsrepo
```

Enable spack in your current shell and bootstrap spack itself:
```
source /usr/local/spack/share/spack/setup-env.sh
spack bootstrap now
```

This repository comes with a spack environment file to do most of the setup automatically. To create an environment named "arts" from this file and activate it:
```
cd ~/spack-repo
spack env create arts env.yaml
spack env activate -p arts
```
The `-p` flag is optional and prepends the environment name to your shell prompt. A shorthand for `spack env activate` is `spacktivate`. Deactivation can be done with `spack env deactivate` or `despacktivate`.

Perform the final initialization steps _inside the environment_. These steps are

1. Find already installed compilers on the system
1. Find already installed packages on the system (e.g. CUDA)
1. Ensure spack can find the packages defined in this repo

```
spack compiler find
spack external find --all -p /usr/local/cuda
spack repo add /usr/local/spack/artsrepo
```
N.b. is it possible to install other compilers using spack itself, but this takes a long time and the compilers on the ARTS system are new enough so these are used instead.

Now you are ready to install packages. To install all packages defined in the environment, first let spack resolve the dependencies:
```
spack concretize
```

If there are no errors, continue with the installation:
```
spack install
```

It is possible to run multiple instances of `spack install` in parallel to speed up the installation process.

# Usage
There are two ways of using the spack environment: Through a spack view, giving access to all installed packages simultaneously, or through module files. Both methods are described here.

## Spack view
To use the spack view, first enable spack, followed by activating the arts environment:
```
source /usr/local/spack/share/spack/setup-env.sh
spack env activate -p arts
```
Now all installed packages are available in your current shell. If you want to know which packages are installed, run `spack find`. The relevant packages are listed under "root specs". Note: The environment includes Python 3.11. Several packages include python module that are also made available through the environment.

## Modules
This method assumes Lmod is already installed on the system (it is on ARTS). Point Lmod to the spack modules to enable them:
```
module use /usr/local/spack/share/spack/lmod/linux-debian12-x86_64/Core
```
The exact path depends on the operating system and system architecture, the above is correct for ARTS.

Run `module avail` to get a list of available modules. In principle, a single version of each package is installed hence it is optional to specify the version number when loading a module. E.g. simply `module load tempo2` works. Dependencies are also handle automatically, e.g. loading `presto` also loads `tempo`.

### Python packages
Note that several packages come with Python modules as well. When one of these packages is loaded, the Python module is loaded as well, but _not_ the other way around. I.e. when you want to use e.g. the PRESTO Python modules, run either `module load python` followed by `module load presto`, or simply `module load presto`.

### ARTS cluster installation
On the ARTS cluster the spack installation is made available locally on each node in `/usr/local/spack`. The installation is synced from arts041 to the other nodes. The installation path must be the same on all nodes to avoid breaking symlinks, wich are used internally by spack. An example script to sync the installation across the cluster is provided in `bin/sync_spack.sh`. It is advised to clean the spack cache with `spack clean --all` before syncing.
