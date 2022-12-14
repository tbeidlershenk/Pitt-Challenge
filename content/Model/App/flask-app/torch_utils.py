import torch
import torchvision.transforms as tsf
from PIL import Image
import io
import numpy
 
# load the model
model = torch.load("models/test.pt")
#model.eval()
 
# turn image to tensor
def img_to_tensor(img_bytes):
   transform = tsf.Compose([
       #tsf.Grayscale(num_output_channels=1),
       tsf.Resize((224,224)),
       tsf.ToTensor()
       #tsf.Normalize((0.1307,),(0.3081,))
   ])
   image = Image.open(io.BytesIO(img_bytes))
   numpy.array(image).shape
   # reverse (white -> black)
   tensor = 1-transform(image).unsqueeze(0)
   print(tensor.shape)
   #print(tensor)
   return tensor
 
def predict_img(tensor):
   guess = model.predict(tensor)
   print(guess)
   return guess.item()