'''
Function:
    Define some utils for normalization
'''
import copy
'''constructnormcfg'''


def constructnormcfg(placeholder, norm_cfg):
    norm_cfg = copy.deepcopy(norm_cfg)
    norm_cfg['placeholder'] = placeholder
    return norm_cfg
