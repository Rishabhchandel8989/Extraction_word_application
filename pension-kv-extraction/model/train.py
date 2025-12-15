from torch.optim import AdamW

def train(model, dataloader):
    optimizer = AdamW(model.parameters(), lr=5e-5)
    for batch in dataloader:
        loss = model(**batch).loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
