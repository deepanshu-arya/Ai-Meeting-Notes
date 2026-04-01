from transformers import pipeline

model = None

def load_model():
    global model
    if model is None:
        model = pipeline("text2text-generation", model="google/flan-t5-small")


def generate_summary(data):
    lines = data.split("\n")
    products = {}

    for line in lines[1:]:
        parts = line.split(",")

        # Skip invalid rows
        if len(parts) < 4:
            continue

        try:
            product = parts[1].strip()
            qty = int(parts[2].strip())
        except:
            continue  # skip bad data like "wind speed"

        if product in products:
            products[product] += qty
        else:
            products[product] = qty

    summary = "Sales Summary:\n"
    for p, q in products.items():
        summary += f"{p}: {q}\n"

    return summary

def extract_action_points(text):
    load_model()
    prompt = f"Extract action points:\n{text[:500]}"
    result = model(prompt, max_length=150)
    return result[0]['generated_text']