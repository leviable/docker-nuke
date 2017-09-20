from pbr.version import VersionInfo

from .main import main  as nuke  # NOQA

__version__ = VersionInfo('traw').semantic_version().release_string()
__all__ = ('__version__', 'nuke')
