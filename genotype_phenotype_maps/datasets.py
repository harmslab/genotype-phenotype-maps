from .methods import lazy_load as _load
from .methods import list_datasets as _list_datasets

for name in _list_datasets():
    vars()[name] = _load(name)
