# -*- coding: utf-8 -*-
import contextlib
import logging
from importlib.metadata import PackageNotFoundError, version

import canmatrix.formats as formats
import canmatrix.cancluster as cancluster

from canmatrix.canmatrix import (
    Ecu,
    Signal,
    SignalGroup,
    DecodedSignal,
    ArbitrationId,
    Frame,
    Define,
    CanMatrix,
)

from canmatrix.canmatrix import (
    StartbitLowerZero,
    EncodingComplexMultiplexed,
    MissingMuxSignal,
    DecodingComplexMultiplexed,
    DecodingFrameLength,
    ArbitrationIdOutOfRange
)

# todo remove this later
from canmatrix.canmatrix import *

# Set default logging handler to avoid "No handler found" warnings in python 2.
logging.getLogger(__name__).addHandler(logging.NullHandler())

with contextlib.suppress(PackageNotFoundError):
    __version__ = version("canmatrix")