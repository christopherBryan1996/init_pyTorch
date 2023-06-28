import torch

#toma de arreglos
t = torch.tensor([1,2,2,2,2,3,4,4,5])
#deven ser del mismo tamaño
t2 = torch.tensor([[1,2,2,2,2,5],[1,2,2,2,4,4],[1,2,2,2,4,4]])
t3 = torch.tensor([[1,2,2,2,2,5],[1,2,2,2,4,4],[1,2,2,2,4,4]])
#mescla los arreglos 
reshape_tensor = t2.reshape(t2[0].size()[0],t2.size()[0])
sum = t + t
print(t)
print(t2)
print(reshape_tensor )
print(sum)