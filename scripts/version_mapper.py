"""A script for updating the JSON file controlling the version switching."""

import argparse
import json


def add_version_to_switcher_file(version, base_url, filename="switcher.json"):
    """Add new version number and associated URL to JSON file.

    Parameters
    ----------
    version : str
        Desired version number.
    filename : str, optional
        File name of the switcher JSON file.

    """
    with open(filename, "r+") as switcher_file:
        # Get the whole content of the file
        content = json.load(switcher_file)

        # Add the new version name and its url according to Sphinx format
        version_data = {
            "version": version,
            "url": base_url + f"/release/{version}",
        }
        content.append(version_data)

        # Update JSON file
        switcher_file.seek(0)
        json.dump(content, switcher_file, indent=4)


def parse_cli_arguments():
    """Parse all command line arguments."""
    parser = argparse.ArgumentParser(description="Switcher JSON file updater.")
    parser.add_argument("-base-url", type=str, help="URL of website.")
    parser.add_argument("-version", type=str, help="New version to be added.")
    parser.add_argument("-filename", type=str, default="version_mapper.json", help="Name of the JSON file.")
    args = parser.parse_args()
    return args

def main():
    """Entry function of the script."""
    args = parse_cli_arguments()
    add_version_to_switcher_file(args.version, args.filename)

if __name__ == "__main__":
    main()