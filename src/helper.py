from prophet.serialize import model_from_json, model_to_json


def save_prophet_model(model, output_path):
    with open(output_path, 'w') as f:
        f.write(model_to_json(model))
    print(f"Successfully saved model at {output_path}")


def load_prophet_model(model_path):
    with open(model_path, 'r') as f:
        model = model_from_json(f.read())
    return model
