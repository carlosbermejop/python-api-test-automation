import csv
import pytest
import pytest_check as check
import requests
from schema import Schema


class TestClass:

    @pytest.fixture(autouse=True)
    def retrieve_csv(self):
        response = requests.get("http://localhost:5000/typeclass", timeout=5 * 1000)
        decoded_response = response.content.decode("utf-8")
        self._csv_data = csv.DictReader(decoded_response.splitlines())


    def test_validate_csv_structure(self):
        csv_data = self._csv_data
        csv_schema = Schema(
            { "product_id": str, "typeclass_name": str, "body_shape": str }
        )

        for row in csv_data:
            assert csv_schema.is_valid(row), f"{row} is not a valid row according to the schema for the CSV."


    def test_validate_body_shape(self):
        csv_data = self._csv_data

        for row in csv_data:
            if any(map(row["typeclass_name"].__contains__, ["FHS", "FHL", "FHT"])):
                check.equal(row["body_shape"], "oBM",
                            msg=f"For typeclass_name {row["typeclass_name"]} the body_shape was set to {row["body_shape"]} instead of oBM")
            else:
                check.equal(row["body_shape"], "gBM",
                            msg=f"For typeclass_name {row["typeclass_name"]} the body_shape was set to {row["body_shape"]} instead of gBM")
