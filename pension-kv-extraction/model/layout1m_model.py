from transformers import LayoutLMForTokenClassification

def get_model(num_labels):
    return LayoutLMForTokenClassification.from_pretrained(
        "microsoft/layoutlm-base-uncased",
        num_labels=num_labels
    )
