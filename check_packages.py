import importlib

packages = [
    "pandas",
    "dimod",
    "dwave.system",
    "tabulate"
]

for package in packages:
    try:
        importlib.import_module(package)
        print(f"{package} is installed.")
    except ImportError:
        print(f"{package} is NOT installed.")
