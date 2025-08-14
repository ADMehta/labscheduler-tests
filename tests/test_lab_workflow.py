import pytest
from utils.api_client import create_lab, get_lab, update_lab, delete_lab

# Fixture to create a lab and share its ID across tests
@pytest.fixture(scope="module")
def lab_id():
    payload = {
        "name": "Central Medical Lab",
        "address": "456 Medical Ave",
        "city": "Boston",
        "state": "MA",
        "zipCode": "02101",
        "phone": "(510) 987-6543"
    }
    response = create_lab(payload)
    assert response.status_code in [200, 201]
    return response.json()["id"]

# Fixture to provide updated lab data
@pytest.fixture(scope="module")
def updated_payload():
    return {
        "name": "Updated Medical Lab",
        "address": "789 Health Blvd",
        "city": "Cambridge",
        "state": "MA",
        "zipCode": "02139",
        "phone": "(555) 111-2222"
    }

@pytest.mark.order(0)
def test_create_lab_with_missing_required_fields_should_fail():
    invalid_payload = {
        # "name" is intentionally omitted
        "address": "123 Broken St.",
        "city": "Nowhere",
        "state": "ZZ",
        "zipCode": "00000",
        "phone": "(000) 000-0000"
    }
    response = create_lab(invalid_payload)
    assert response.status_code == 400

@pytest.mark.order(1)
def test_create_lab_and_validate_with_get_by_id(lab_id):
    response = get_lab(lab_id)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Central Medical Lab"

@pytest.mark.order(2)
def test_update_lab_and_validate_changes_with_get_by_id(lab_id, updated_payload):
    response = update_lab(lab_id, updated_payload)
    assert response.status_code in [200, 204]

    # Confirm update
    response = get_lab(lab_id)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Medical Lab"

@pytest.mark.order(3)
def test_delete_lab_by_id(lab_id):
    response = delete_lab(lab_id)
    assert response.status_code in [200, 204]

@pytest.mark.order(4)
def test_validate_lab_is_deleted_with_get_by_id(lab_id):
    response = get_lab(lab_id)
    assert response.status_code == 404  #  deleted lab returns 404