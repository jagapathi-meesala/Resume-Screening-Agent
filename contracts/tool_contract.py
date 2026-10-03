class ToolContract:
    def __init__(self, required, properties):
        self.required = set(required)
        self.properties = properties
    def validate(self, data):
        if not isinstance(data, dict): raise ValueError("input must be an object")
        missing = self.required - data.keys()
        if missing: raise ValueError(f"missing required fields: {sorted(missing)}")
        extra = set(data) - set(self.properties)
        if extra: raise ValueError(f"unexpected fields: {sorted(extra)}")
        for key, typ in self.properties.items():
            if key in data and not isinstance(data[key], typ):
                raise ValueError(f"invalid type for {key}")
        return data
