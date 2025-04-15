import csv
import json
import time
import pytest
import pytest_check as check
import requests
from schema import Schema
from tqdm import tqdm



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
                
    def test_huge_json_file(self):
        start_time = time.time()
        first_response = requests.get("http://localhost:5000/json-1", timeout=5 * 1000)
        first_decoded_response = first_response.content.decode("utf-8")
        first_json = json.loads(first_decoded_response)
        
        second_response = requests.get("http://localhost:5000/json-2", timeout=5 * 1000)
        second_decoded_response = second_response.content.decode("utf-8")
        second_json = json.loads(second_decoded_response)
        
        idx = 1
        objs_not_found = []
        for obj in tqdm(first_json):
            found_objs_by_name = list(filter(lambda x:x["name"]==obj["name"], second_json))[0]
            
            if found_objs_by_name:
                check.equal(obj["email"], found_objs_by_name["email"],
                            msg=f"For name {obj["name"]}, the email {found_objs_by_name["email"]} was found instead of {obj["email"]}.")
                check.equal(obj["address"], found_objs_by_name["address"],
                            msg=f"For name {obj["name"]}, the address {found_objs_by_name["address"]} was found instead of {obj["address"]}.")
                check.equal(obj["phone"], found_objs_by_name["phone"],
                            msg=f"For name {obj["name"]}, the phone {found_objs_by_name["phone"]} was found instead of {obj["phone"]}.")
                check.equal(obj["website"], found_objs_by_name["website"],
                            msg=f"For name {obj["name"]}, the website {found_objs_by_name["website"]} was found instead of {obj["website"]}.")
            else:
                print(f"Name {obj["name"]} is new and was not retrieved from endpoint 2.")
                objs_not_found.append(obj)
            idx += 1
        print("The following objects were new and were not found in endpoint 2:\n")
        print(*objs_not_found, sep='\n')
        print("--- %s seconds ---" % (time.time() - start_time))
