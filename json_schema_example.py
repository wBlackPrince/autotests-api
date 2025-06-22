from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"}
    },
    "required": ["name"]
}

data = {
    "name": 50,
    "age": 30
}


validate(instance=data, schema=schema)


# Отступы. Используйте два пробела для отступов.

{
  "type": "object",
  "properties": {
    "username": {"type": "string", "minLength": 5, "maxLength": 15}
  },
  "required": ["username"]
}

{
  "type": "object",
  "properties": {
    "id": {"type": "string"},
    "email": {"type": "string", "format": "email"},
    "age": {"type": "integer"}
  },
  "required": ["id", "email"]
}