from typing import Any
from db.connection import Connection
from constants.params import params as params_filters

def params(f) -> Any:
    """
    Get params from request
    """
    def checksum(*args, **kwargs):
        params, values = set_filters(**kwargs)
        return f(filters=params, values=values)

    return checksum


@params
def get_estates(filters: str, values: tuple) -> str:
    """
    Get last state of estate
    """
    query = """
            SELECT
	            p.address,
	            p.city,
                s.label,
	            p.price,
	            p.description
            FROM
            	property p
            LEFT JOIN (SELECT MAX(update_date) as update_date, property_id, status_id FROM status_history sh GROUP BY property_id) sh ON
            	p.id = sh.property_id
            INNER JOIN status s ON
            	sh.status_id = s.id
            WHERE
            	s.name in ('pre_venta', 'en_venta', 'vendido')
            	AND p.address != ''
            	AND p.description != ''
    """

    query = query + filters
    query_result = Connection.get(query, values)
    return query_result


def set_filters(filters: dict) -> list:
    """
    Filter estates by filters
    """
    query_params = []
    query = "AND "
    query_params_values = []
    for key, value in filters.items():
        if key in params_filters and ((isinstance(value, str) and len(value.strip()) > 0) or (isinstance(value, int) and value > 0)):
            if key == "state":
                key = "s.name"

            query_params.append(f"{key} = %s")
            query_params_values.append(value)

    if len(query_params) == 0:
        return "", ()

    if len(query_params) == 1:
        path = query_params[0]
        values = tuple(query_params_values)

    if len(query_params) > 1:
        path = " AND ".join(query_params)
        values = tuple(query_params_values)

    return (query + path), values
