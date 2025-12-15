def predict(model, inputs):
    outputs = model(**inputs)
    return outputs.logits.argmax(-1)
