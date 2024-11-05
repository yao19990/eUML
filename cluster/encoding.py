import PIL.Image as I
import torch
import os,glob ,shutil
from torchvision import transforms# Load ViT
from pytorch_pretrained_vit import ViT
import numpy as np
from tqdm import tqdm
import timm

def makedata(data):
    new = []
    for i in data:
        #print(i)
        #exit()
        new.append(i)
    return new

def check_file(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        os.makedirs(path)
        
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")        
model=ViT('B_16_imagenet1k',pretrained=True)
model = model.to(device)
model.eval()# Load image# NOTE: Assumes an image `img.jpg` exists in the current directory

model = timm.create_model('convnext_xlarge_in22k', pretrained=True, num_classes=0)
model = model.to(device)
model.eval()# Load image# NOTE: Assumes an image `img.jpg` exists in the current directory


img=transforms.Compose([transforms.Resize((384,384)),transforms.ToTensor(),transforms.Normalize(0.5,0.5),])
img=transforms.Compose([transforms.Resize((224,224)),transforms.ToTensor()])
#训练和测试集地址，例如：‘/xxx/train’,‘/xxx/test’
train_path=r'../Data/Datasets/train'
test_path=r'../Data/Datasets/test'

imgs = []
imgs_ = []

check_file('data/')

for i in tqdm(glob.glob(train_path+'/*')):
    #注意如果是Linux跑程序，将'\\'改为'/'
    # print(i)
    # exit()
    label = i.split('/')[-1].split('_')[0]
    img1 = I.open(i).convert('RGB')
    # print(img1.shape)
    # exit()
    img1 = img(img1)
    img1 = img1.unsqueeze(0)
    #print(img1.shape,'==')
    with torch.no_grad():
        img1 = img1.to(device)
        outputs = model(img1)
        outputs = outputs.cpu()
        np.set_printoptions(suppress=True)
        outputs = np.array(outputs,dtype = 'float32')

        imgs.append([outputs,label])
        datas = makedata(outputs[0])
        with open('data/encode_train.txt','a') as f:
            f.write('%s\t%s\t%s\n'%(i,'<=>'.join([str(x) for x in datas]),label))
            #f.write('%s\t%s\n'%(datas,label))
        with open('data/encode_train_name.txt','a') as f:
            f.write('%s\n'%(i))

for i in tqdm(glob.glob(test_path+'/*')):
    #注意如果是Linux跑程序，将'\\'改为'/'
    label = i.split('/')[-1].split('_')[0]
    img1 = I.open(i).convert('RGB')
    img1 = img(img1)
    img1 = img1.unsqueeze(0)
    #print(img1.shape,'==')
    with torch.no_grad():
        img1 = img1.to(device)
        outputs = model(img1)
        outputs = outputs.cpu()
        np.set_printoptions(suppress=True)
        
        outputs = np.array(outputs,dtype = 'float32')

        imgs_.append([outputs,label])
        datas = makedata(outputs[0])
        with open('data/encode_test.txt','a') as f:
            f.write('%s\t%s\n'%(datas,label))
            f.write('%s\t%s\t%s\n'%(i,'<=>'.join([str(x) for x in datas]),label))
        with open('data/encode_test_name.txt','a') as f:
            f.write('%s\n'%(i))
