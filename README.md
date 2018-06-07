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

After which you can start spacking astronomy packages:

```
$ spack install tempo
```
