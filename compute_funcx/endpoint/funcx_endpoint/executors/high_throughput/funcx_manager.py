import warnings

from globus_compute_endpoint.executors.high_throughput.manager import (  # noqa: F401
    Manager as FuncXManager,
)
from globus_compute_endpoint.version import DEPRECATION_FUNCX_ENDPOINT

warnings.warn(DEPRECATION_FUNCX_ENDPOINT)
