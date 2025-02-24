import logging

__author__ = """Alex Carimán"""
__email__ = "alex@cariman.cl"
__version__ = "0.1.0"


logging.basicConfig(
    level=logging.DEBUG,
    format=f"%(asctime)s %(levelname)s\t%(module)s\t[{__version__}]\t%(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S%z",
    handlers=[logging.StreamHandler(), logging.FileHandler("sampler.log")],
)
