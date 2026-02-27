def to_dict(model) -> dict:
    if model is None:
        return {}
    data = dict(model.__dict__)
    data.pop("_sa_instance_state", None)
    return data
