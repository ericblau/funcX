import warnings

from globus_compute_endpoint.executors.high_throughput.worker import (  # noqa: F401
    Worker as FuncXWorker,
)
from globus_compute_endpoint.version import DEPRECATION_FUNCX_ENDPOINT

warnings.warn(DEPRECATION_FUNCX_ENDPOINT)
