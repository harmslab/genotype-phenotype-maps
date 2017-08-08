# Experimental datasets

Each dataset has a `.txt` file with the raw data and a `.json` file with metadata. The textfile also has a header with the metadata, commented out with `#`.

The structure of the python metadata is:

```
{   
    "filename": "filename ...",
    "title": "some-title ... ",
    "authors": "author names ...",
    "url": "...",
    "journal": "journal name ...",
    "sep": "...",
    "comment: "...",
    "genotypes": [...],
    "phenotypes": [...],
    "stdeviations": [...],
    "n_replicates": [...]
}
```

## Metadata meaning:

filename: name of the `.txt` file.
title: title of the journal article where data was published.
authors: name of all authors on journal.
url: website url where article can be found.
journal: journal name.
columns: titles for each column for pandas to use.
dtypes: datatypes of each column, (genotypes=str, phenotypes=float)
sep: separator for columns in the `.txt` file. Should use `" "`
comment: characters used for commenting in the `.txt`. Should use `"#"`
