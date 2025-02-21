from __future__ import absolute_import

# import the common modules
from exkaldirt.version import version
from exkaldirt import base
from exkaldirt.base import info
from exkaldirt import stream
from exkaldirt import transmit

# these modules will be hidden if exkaldirt only run on local environment where Kaldi is not existed
if info.KALDI_EXISTED:
  from exkaldirt import feature
  from exkaldirt import decode

