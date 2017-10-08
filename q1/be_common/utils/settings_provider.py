import logging
import sys
import yaml
log = logging.getLogger(__name__)
_cfg = None


def _create_setting(path):
    global _cfg
    if _cfg is None:
        """
        Setup misc configurations
        """
        try:
            with open(path, 'r') as ymlfile:
                _cfg = yaml.safe_load(ymlfile)
        except IOError as e:
            sys.exit('Could not load yaml configuration file:{}' % path)


def get_settings(path=None):
    if _cfg is None and path is not None:
        _create_setting(path)
    if _cfg is not None:
        return _cfg
