# Generate UML diagram of the target module and save it as png file
from os import name
import pydot
import os


def generate_uml(module_path):
    # Generate compiler graph for the module
    os.system("pyreverse -o png -p traja " f"{module_path}")
    return None


if __name__ == "__main__":
    generate_uml(os.getcwd())
