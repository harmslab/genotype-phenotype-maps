# A repository of published genotype-phenotype maps

Here, we're collecting a list of published, combinatorial genotype-phenotype maps.

If you have a dataset you'd like to add to our list, let us know. You can open an issue here, and we'll help you merge you're dataset into this repo.

**Contents**

* [Genotype-phenotype map file format](#genotype-phenotype-map-file-format)
* [How to use these datasets](#how-use-these-datasets)
* [How to create an Excel file for one of the datasets](#how-to-create-an-excel-file-for-one-of-the-datasets)
* [How to add my dataset to the list](#how-to-add-my-dataset-to-the-list)

## Genotype-phenotype map file format

Each dataset is stored in a JSON file with a particular format. Minimally, `genotype-phenotype-maps`
expects a `"data"` field, and its value is a list of fields and values: `"genotypes"`, `"phenotypes"`, `"stdeviations"`, and `"n_replicates"`. `genotype-phenotype-maps` will also look for a `"wildtype"` field that provides the reference genotype and a `"mutations"` field that lists the possible mutations at each site. If these fields are not included, they will be inferred.

This resulting JSON file looks like:
```json
{
  "wildtype": "AA",
  "mutations": {
    "0": ["A", "T"],
    "1": ["A", "T"], 
  },
  "data": {
    "genotypes": ["AA", "AT", "TA", "TT"],
    "phenotypes": [0.5, 0.5, 0.8, 1.0],
    "stdeviations": [0.1, 0.1, 0.1, 0.1],
    "n_replicates": 1
  }
}
```

You can store other metadata about each dataset as extra fields in the JSON files.
```json
{
  "source": "url to the dataset",
  "journal": "Nature Genetics", 
  "authors": ["Alice", "Bob", "Charlie"],
  "wildtype": "AA",
  "mutations": {
    "0": ["A", "T"],
    "1": ["A", "T"], 
  },
  "data": {
    "genotypes": ["AA", "AT", "TA", "TT"],
    "phenotypes": [0.5, 0.5, 0.8, 1.0],
    "stdeviations": [0.1, 0.1, 0.1, 0.1],
    "n_replicates": 1
  }
}
```


## How use these datasets

We added a Python interface to these datasets to make it easy to load and analyze them. The following instructions explain how to install and use this interface. We assume you have Python and `pip`, Python's package manager and installer, installed properly on your machine. 

**Download genotype-phenotype maps**

The first step is to download this repository. You can either download this repository and its contents or use git to clone the repository. i.e.:
```
git clone https://github.com/harmslab/genotype-phenotype-maps
```

**Install genotype-phenotype maps API/interface**

The remaining steps must to be done in a terminal/command-line. Navigate into the `genotype-phenotype-maps/` folder you just downloaded (there should be a `setup.py` file in this folder). We'll now setup Python's "entry points" to this folder. Note, if you move this folder, you'll need to rerun the following steps in the new location. 

"Install" the package using `pip` via this command:
```
pip install -e .
```
This command creates a symbolic link in your Python site-packges to the directory of genotype-phenotype maps. 

**Use datasets in genotype-phenotype maps**

You can now interact with these datasets two different ways. 
1. Export a dataset into a useful file format (like an Excel spreadsheet). 
2. Import a dataset into a Python (or IPython/Jupyter) session.

If you import a dataset in a Python session, `genotype-phenotype-maps` returns a [`GenotypePhenotypeMap`](https://github.com/harmslab/gpmap) object:  
```python
>>> import genotype_phenotype_maps as datasets
>>> gpm = datasets.weinreich()
>>> gpm
<gpmap.gpm.GenotypePhenotypeMap at 0x11b726128>
```
The `GenotypePhenotypeMap` is a flexible object for managing genotype-phenotype map data. This object has a `data` attribute. It's a [Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html). 

```python
>>> import genotype_phenotype_maps
>>> genotype_phenotype_maps.list_datasets()
['anderson',
 'bridgham',
 'bridgham2',
 'bridgham3',
 'costanzo',
 'dasilva',
 'flynn1',
 'flynn2',
 'hall_diploid_growth',
 'hall_haploid_growth',
 'hall_mating_efficiency',
 'hall_sporulation_efficiency',
 'jochumsen',
 'khan',
 'krug1',
 'krug2',
 'lalic',
 'palmer',
 'summers',
 'weinreich']
```

## How to create an Excel file for one of the datasets

If [installed our Python command-line interface](), you export any dataset to an Excel file (or some other format) using the following command: 

```
> genotype_phenotype_maps get weinreich

Found a dataset named weinreich.

In what format would you like this dataset: excel, csv, json? [excel]

> excel

Successfully created weinreich.json.
```

## How to add my dataset to the list

You can add a new dataset to the list by manually creating a JSON file in the `datasets/` folder *or* using the command line interface to convert other formats

```
> genotype_phenotype_maps add my_dataset.xlsx

What do you want to name this dataset? [my_dataset]

> my_dataset

Successfully added your dataset to genotype-phenotype maps.
```