import torch
import torchvision.transforms as transforms

#create a tensor with ramdomvalues
tensor = torch.randn(100, 100)

transform = transforms.Compose([transforms.Lambda(lambda x : x+1)])

transform_tensor = transform(tensor)

print(tensor)
print(transform_tensor)