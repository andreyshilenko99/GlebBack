import os
import yaml
from yaml import Loader

wd = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(wd, 'config/config.yaml'), 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=Loader)

with open(os.path.join(wd, 'config/config.default.yaml'), 'r') as ymlfile:
    defcfg = yaml.load(ymlfile, Loader=Loader)


def settings_loader(key, default=None):
    if key in cfg:
        return cfg[key]

    if default:
        return default

    if key in defcfg:
        return defcfg[key]

    return default