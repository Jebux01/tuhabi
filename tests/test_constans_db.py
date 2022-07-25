from app.constants.db import params


def test_params_db():
    """
    Test params db
    """
    for param in params:
        assert params[param] is not None