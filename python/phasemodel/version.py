"""phase-coupling-estimation version/release information"""

ISRELEASED = False

# Format expected by setup.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 4
_version_micro = 'dev'
__version__ = "%s.%s.%s" % (_version_major, _version_minor, _version_micro)
version = __version__

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: BSD License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

description = "Phase-coupling-estimation: univariate and multivariate phase distribution modeling and fitting."

long_description = """

Cadieu CF, Koepsell K (2010) Phase coupling estimation from multivariate phase
statistics. Neural Computation (in press). 

"""

NAME                = "phasemodel"
MAINTAINER          = "Charles Cadieu and Kilian Kopesell"
MAINTAINER_EMAIL    = "cadieu@berkeley.edu,kilian@berkeley.edu"
DESCRIPTION         = description
LONG_DESCRIPTION    = long_description
URL                 = "http://redwood.berkeley.edu/klab/"
DOWNLOAD_URL        = "http://github.com/koepsell/phase-coupling-estimation"
LICENSE             = "BSD"
AUTHOR              = "Charles Cadieu and Kilian Koepsell"
AUTHOR_EMAIL        = "cadieu@berkeley.edu,kilian@berkeley.edu"
PLATFORMS           = "OS Independent"
MAJOR               = _version_major
MINOR               = _version_minor
MICRO               = _version_micro
VERSION             = __version__
PACKAGES            = ['phasemodel']
REQUIRES            = ["numpy", "matplotlib", "scipy"]
