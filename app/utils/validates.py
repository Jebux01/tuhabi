from typing import Dict
from app.constants.params import params as params_filters

def valid_params_and_values(params: Dict):
    invalids = list(
        filter(
            lambda param: param not in params_filters, 
            list(
                params.keys()
            )
        )
    )

    if len(invalids) > 0:
        message = "Invalid params: " + ", ".join(invalids)
        return {"error": True, "message": message}

    empty = list(
        filter(
            lambda key: len((str(params[key])).strip()) == 0, params.keys()
        )
    )

    if len(empty) > 0:
        message = "Empty params: " + ", ".join(empty)
        return {"error": True, "message": message}

    return False
