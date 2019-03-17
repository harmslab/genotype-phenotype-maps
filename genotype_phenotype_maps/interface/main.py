import argparse
from . import subcommands

def main():
    # Main interface
    parser = argparse.ArgumentParser(description="""
    A command-line interface for genotype-phenotype-maps. 
    
    Get, add, and list the datasets in this curated list of 
    maps from the literature.
    """)

    # Enable subparsers
    subparsers = parser.add_subparsers()

    # "get" subparser
    get_parser = subparsers.add_parser(
        "get",
        description="Get any dataset in the genotype-phenotype-map list in the format of your choice."
    )
    get_parser.add_argument('name', help="Dataset name.")
    get_parser.set_defaults(subcommand=subcommands.get)

    # "add" subparser
    add_parser = subparsers.add_parser(
        "add",
        description="Add a dataset to the genotype-phenotype-map list."
    )
    add_parser.add_argument('in_path', help="File path to the dataset you'd like to add.")
    add_parser.set_defaults(subcommand=subcommands.add)
    
    list_parser = subparsers.add_parser(
        "list",
        description="List all datasets in genotype-phenotype-maps."
    )
    list_parser.set_defaults(subcommand=subcommands.list)

    # Parse the commandline and filter to the appropriate subcommand.
    args = parser.parse_args()
    args.subcommand(args)

if __name__ == "__main__":
    main()