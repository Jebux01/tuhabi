
from app.services.estates_services import get_estates, set_filters


def test_get_estates_without():
    """
    Test get estates
    """
    response = get_estates(filters={})
    assert response != []
    assert "address" in response[0]
    assert "city" in response[0]
    assert "label" in response[0]
    assert "price" in response[0]
    assert "description" in response[0]

def test_get_estates_year():
    """
    Test get estates
    """
    response = get_estates(filters={"year":2011})
    assert response != []
    assert "address" in response[0]
    assert "city" in response[0]
    assert "label" in response[0]
    assert "price" in response[0]
    assert "description" in response[0]

def test_get_estates_city():
    """
    Test get estates
    """
    response = get_estates(filters={"city": "bogota"})
    assert response != []
    assert "address" in response[0]
    assert "city" in response[0]
    assert "label" in response[0]
    assert "price" in response[0]
    assert "description" in response[0]

def test_get_estates_state():
    """
    Test get estates
    """
    response = get_estates(filters={"state": "pre_venta"})
    assert response != []
    assert "address" in response[0]
    assert "city" in response[0]
    assert "label" in response[0]
    assert "price" in response[0]
    assert "description" in response[0]


def test_set_filters():
    """
    Test set filters
    """
    filters = {
        "state": "en_venta",
        "city": "bogota",
        "year": 2011
    }
    response = set_filters(filters=filters)
    assert response
    assert isinstance(response, tuple)
    assert response[0] == "AND s.name = %s AND city = %s AND year = %s"


def test_set_filters_others_params():
    """
    Test set filters
    """
    filters = {
        "name": "en_venta",
        "city": "bogota",
        "year": 2011
    }
    response = set_filters(filters=filters)
    assert response
    assert isinstance(response, tuple)
    assert response[0] == "AND city = %s AND year = %s"


def test_set_filters_year():
    """
    Test set filters
    """
    filters = {
        "year": 2011
    }
    response = set_filters(filters=filters)
    assert response
    assert isinstance(response, tuple)
    assert response[0] == "AND year = %s"


def test_set_filters_city():
    """
    Test set filters
    """
    filters = {
        "city": "bogota"
    }
    response = set_filters(filters=filters)
    assert response
    assert isinstance(response, tuple)
    assert response[0] == "AND city = %s"
    

def test_set_filters_state():
    """
    Test set filters
    """
    filters = {
        "state": "en_venta"
    }
    response = set_filters(filters=filters)
    assert response
    assert isinstance(response, tuple)
    assert response[0] == "AND s.name = %s"
    