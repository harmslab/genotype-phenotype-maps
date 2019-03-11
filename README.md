# A repository of published genotype-phenotype maps

This repository provides a curated list of published, combinatorial genotype-phenotype maps.

**Contents**

* [What are genotype-phenotype maps?]()
* [Genotype-phenotype map file format.]()
* [Datasets included here.]()
* [How to import and use these datasets.]()
* [How to create an Excel file for one of the datasets.]()
* [How to add my dataset to the list.]()
    * Excel data
    * CSV Data
    * JSON Data
    * Other formats.

## What are genotype-phenotype maps?

Genotype-phenotype maps are...

## Genotype-phenotype map file format.

The structure of the python metadata is:
```
{   
    "filename": "filename ...",
    "title": "some-title ... ",
    "authors": "author names ...",
    "url_to_source": "...",
    "journal": "journal name ...",
    "data" : {
        "genotypes": [...],
        "phenotypes": [...],
        "stdeviations": [...],
        "n_replicates": [...]
    }
}
```

## How to import and use these datasets.

To make it convenient for *most* users, we added a Python interface to this repository. The following instructions explain how to use these datasets in Python. We assume you have Python and `pip`, Python's package manager and installer, installed properly on your machine. 

The first step is to download this repository. You can either download this repository and its contents or use git to clone the repository. i.e.:
```
git clone xx
```
 
The remaining steps need to be done in a terminal/command-line. Navigate into the folder you just downloaded (there should be a `setup.py` file in this folder). We'll now setup Python's "entry points" to this folder. Note, if you move this folder, you'll need to rerun the following steps in the new location. 

"Install" the package using `pip` via this command:
```
pip install -e .
```

You can now use the command line interface we've provided. You can also import the datasets directly into a Python (or IPython/Jupyter) session.

```python
>>> import genotype_phenotype_maps as gpmaps
>>> print(gpmaps)


```

## How to create an Excel file for one of the datasets.

If you have Python and you [installed our Python interface](), you can use our command-line interface to create Excel (and other formats) for the available datasets. 

```
> genotype_phenotype_maps get weinreich

Found a dataset named weinreich.

In what format would you like this dataset: excel, csv, json? [json]

Successfully created weinreich.json.
```

## How to add my dataset to the list.

```
genotype_phenotype_maps add my_dataset.xlsx

What do you want to name this dataset? [my_dataset]

Successfully added your dataset to genotype-phenotype maps.
```

## List the datasets available.

```
genotype_phenotype_maps list

List of datasets:
  anderson
  bridgham
  bridgham2
  bridgham3
  costanzo
  dasilva
  flynn1
  flynn2
  hall_diploid_growth
  hall_haploid_growth
  hall_mating_efficiency
  hall_sporulation_efficiency
  jochumsen
  khan
  krug1
  krug2
  lalic
  palmer
  summers
  weinreich
```