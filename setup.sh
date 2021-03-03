export ANAROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export HEA="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd HEA && pwd )"
export PYTHONPATH=$ANAROOT:$ANAROOT/python:$PYTHONPATH/$HEA:$HEA