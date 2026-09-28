import torch
from torchvision import models

def create_model(num_classes):
    model = models.resnet18(weights="DEFAULT")

    #Freeze the pretrained feature layers.
    for parameter in model.parameters():
        parameter.requires_grad = False

    #Replace the original classifier with one for our food classes.
    model.fc = torch.nn.Linear(
        model.fc.in_features,
        num_classes,
    )

    return model

if __name__ == "__main__":
    model = create_model(num_classes=10)

    print(model.fc)