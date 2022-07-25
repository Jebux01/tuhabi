"""
this module contains the request parameters
"""

from enum import Enum


class StatesValids(Enum):
    """
    States valids
    """
    PRE_VENTA = "pre_venta"
    EN_VENTA = "en_venta"
    VENDIDO = "vendido"

params = {
    "year": 0,
    "city": "",
    "state": "",
}
