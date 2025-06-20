import importlib

def load_model(model_name):
    if model_name == "plantiq8a1-deepthink-lite":
        module = importlib.import_module("model_1")
        return module.PlantExpert()
    elif model_name == "plantiq8a1-vision-lite":
        raise NotImplementedError("Model 'plantiq8a1-deepthink-lite' chưa được khai báo.")
    else:
        raise ValueError(f"Không nhận diện được model: {model_name}")

if __name__ == "__main__":
    model = load_model("plantiq8a1-deepthink-lite")
    cauhoi = "Cây cà chua bị vàng lá thì làm sao khắc phục?"
    traloi = model.traloicauhoi(cauhoi)
    print(f"Câu hỏi: {cauhoi}")
    print(f"Trả lời: {traloi}")

# Plantiq8a1
