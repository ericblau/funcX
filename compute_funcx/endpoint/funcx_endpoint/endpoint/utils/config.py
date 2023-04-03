import warnings

from globus_compute_endpoint.endpoint.utils.config import Config as Config  # noqa: F401
from globus_compute_endpoint.version import DEPRECATION_FUNCX_ENDPOINT

warnings.warn(DEPRECATION_FUNCX_ENDPOINT)
