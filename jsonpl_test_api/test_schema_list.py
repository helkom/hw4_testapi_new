#после установки модуля проблема решилась :)
import json
from jsonschema import validate #ругается на модуль

def assert_validate_schema(data, schema_file):
    with open(schema_file) as file_json:
        schema = json.load(file_json)
        return validate(instance=data, schema=schema)

def test_validate(base_url, session):
    response = session.get(f"{base_url}/posts/1")
    assert_validate_schema(response.json(), "../schemas/post_schema.json")
