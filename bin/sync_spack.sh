#!/bin/bash

# NOTE: spack_dir must have a trailing slash
spack_dir=/usr/local/spack/
# in case rsync is not installed system wide
rsync="$HOME/bin/rsync --rsync-path=/shared/$(whoami)/bin/rsync"

if [[ "$(hostname)" != arts041 ]]; then
    echo "This script must run on arts041"
    exit 1
fi

for i in $(seq -w 01 40); do
    node=arts0$i

    echo "Syncing spack software to ${node}"
    if ! $(ssh ${node} test -d ${spack_dir}); then
        echo "${node}: ${dest_dir} does not exist or is not writable, check manually"
        exit 1
    fi
    ${rsync} -ar --partial --info=progress2 --hard-links --sparse --delete ${spack_dir} ${node}:${spack_dir}
done

