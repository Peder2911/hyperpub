
from hyperpub.rndr import *
import jinja2

env = jinja2.Environment(
    loader = jinja2.PackageLoader("hyperpub","html,css")
)

