# About

this is a spack repository containing radio astronomy software, mostly used for APERTIF.

# Usage

First you need to make sure you can compile things and have curl available.
On Ubuntu:

Clone the spack and apertif spack repositories somewhere on a good place on
your filesystem:

```
$ mkdir ~/Work && cd ~/Work
$ git clone -c feature.manyFiles=true --depth=2 https://github.com/spack/spack.git -b v0.23.1
$ git clone https://github.com/TRASAL/spack spack-apertif
```

Now add the spack-apertif repository to your spack configuration. Ensure it is listed _above_ the default repository.
Edit spack/etc/spack/defaults/repos.yaml to look something like this:
```
repos:
  - /home/<your username here>/Work/spack-apertif
  - $spack/var/spack/repos/builtin

```

Next you can activate the spack environment:

```
$ . spack/share/spack/setup-env.sh
```

For now we base everything on the system GCC 12.
```
$ spack compiler find
```


After which you can start spacking astronomy packages:

```
$ spack install tempo2+x11
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

