import os, pathlib
from gpmap import GenotypePhenotypeMap

def get_dataset_dir():
    """Get the data directory."""
    this_dir = pathlib.Path(__file__).parent
    data_dir = this_dir.joinpath('../datasets/').resolve()
    return str(data_dir)


def get_dataset_path(dataset):
    """Get path to dataset."""
    data_dir = get_dataset_dir()
    dataset_path = pathlib.Path(data_dir).joinpath(dataset)
    return str(dataset_path)


def list_datasets():
    path = get_dataset_dir()
    files = os.listdir(path)
    return sorted([os.path.splitext(f)[0] for f in files])


def load(name):
    """Loads a provide dataset."""
    fname = "{}.json".format(name)
    fpath = get_dataset_path(fname)
    gpm = GenotypePhenotypeMap.read_json(fpath)
    return gpm


def read(filename, format, **kwargs):
    # Use the read method for this format
    method = getattr(GenotypePhenotypeMap, "read_{}".format(format))
    gpm = method(filename, **kwargs)
    return gpm 


def lazy_load(name):
    """Pass a dataset name, return a callable that loads the datasets into a GenotypePhenotypeMap."""
    def inner():
        return load(name)
    return inner