import os, pathlib
from ..methods import load, get_dataset_path, get_dataset_dir, list_datasets
from gpmap import GenotypePhenotypeMap


formats_to_ext = {
    'excel': 'xlsx',
    'csv': 'csv',
    'json': 'json',
}

ext_to_formats = {
    '.xlsx': 'excel',
    '.csv': 'csv',
    '.json': 'json'
}


def get(args):
    # Parse arguments
    name = args.name
    fname = "{}.json".format(name)
    fpath = pathlib.Path(get_dataset_path(fname))

    if fpath.exists():
        print("Found a dataset named {name}\n".format(name=name))
        fformat = input("In what format would you like this dataset: excel, csv, json? [json]")
        if fformat == '':
            fformat = 'json'
        
        gpm = load(name)
    
        # Output filename.
        filename = "{name}.{ext}".format(name=name, ext=formats_to_ext[fformat])
        
        # Write to disk.
        write_method = "to_{file_format}".format(file_format=fformat)
        getattr(gpm, write_method)(filename)
        print("Successfully created {}.".format(filename))
    else: 
        print("Couldn't find a data set named {name}.".format(name=name))

def add(args):
    in_path = args.in_path
    path, ext = os.path.splitext(in_path)
    parent, name = os.path.split(path)

    try:
        fformat = ext_to_formats[ext]
    except:
        fformat = input("I didn't recognize the file format, what format is this? [excel|csv|json]")

    out_name = input("What do you want to name this dataset? [{}]".format(name))
    if out_name == '':
        out_name = name
    
    # build output
    out_path = get_dataset_path(out_name+".json")

    # Write to dataset directory.
    method = getattr(GenotypePhenotypeMap, "read_{}".format(fformat))
    gpm = method(in_path)
    gpm.to_json(out_path)

    print("Successfully added your dataset to genotype-phenotype maps.".format(filename))

def list(args):
    path = get_dataset_dir()
    path = pathlib.Path(path)

    print("\nList of datasets:")
    for name in sorted(list_datasets()):
        print("  {}".format(name))
