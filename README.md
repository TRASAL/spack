# About

this is a spack repository containing radio astronomy software, mostly used for APERTIF.

# Usage

First you need to make sure you can compile things and have curl available.
On Ubuntu:

Clone the spack and apertif spack repositories somewhere on a good place on
your filesystem:

```
$ mkdir ~/Work && cd ~/Work
$ git clone https://github.com/spack/spack.git
$ git clone https://github.com/AA-ALERT/spack spack-apertif
```

Now add the spack-apertif repoistory to your spack configuration:

```
$ echo "  - `pwd`/spack-apertif" >> spack/etc/spack/defaults/repos.yaml
```

Next you can activate the spack environment:

```
$ . spack/share/spack/setup-env.sh
```

Now you need to bootstrap your new environment:

```
$ spack bootstrap
```

For now we base everything on GCC 6.4.0:
```
$ spack install gcc@6.4.0
$ spack module load gcc@6.4.0
$ spack compiler find
```


After which you can start spacking astronomy packages:

```
$ spack install tempo %gcc@6.4.0
```

Notes:

If you run into troubles spacking dspsr with an error like:
```
openmpi requires hwloc version :1.999, but spec asked for 2.0.1   
```

you have ran into [this issue](https://github.com/spack/spack/issues/7938)
which you can solve by running:
```
$ spack install ompss ^hwloc@1.11.9
```

