import os as _os
from .methods import load as _load
from .methods import list_datasets as _list_datasets

for f in _list_datasets():
    name = _os.path.splitext(f)[0]
    vars()[name] = _load(name)
