class PensionDataset:
    def __init__(self, annotations, tokenizer):
        self.data = annotations
        self.tokenizer = tokenizer

    def __getitem__(self, idx):
        return self.data[idx]

    def __len__(self):
        return len(self.data)
