from app.utils.validates import valid_params_and_values


def test_validate_params():
    """
    Test validate params
    """
    params = {
        "state": "en_venta",
        "city": "bogota",
        "year": 2011
    }
    response = valid_params_and_values(params=params)
    assert not response
    


def test_validate_params_invalids():
    """
    Test validate params
    """
    params = {
        "name": "en_venta",
        "city": "bogota",
        "year": 2011
    }
    response = valid_params_and_values(params=params)
    assert response
    assert isinstance(response, dict)
    assert response["error"] is True
    assert response["message"] == "Invalid params: name"