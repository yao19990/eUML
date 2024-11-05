import config as CF
import model as m
import glob
import os,shutil,re
import time
import PCA
import numpy as np

def seq(names):
    name = [1,2,3,4]
    for i in range(0,len(names)):
        if 'encode_train.txt' in names[i]:
            name[0] = names[i]
        elif 'encode_train_name.txt' in names[i]:
            name[2] = names[i]
        elif 'encode_test.txt' in names[i]:
            name[1] = names[i]
        elif 'encode_test_name.txt' in names[i]:
            name[3] = names[i]
    return name

def make_data(path):
    print(glob.glob(path+"/*"))
    # exit()
    #print(path+"/*")
    # print(seq(glob.glob(path+'/*')))
    # exit()
    if os.path.exists('encode_result'):
        os.remove('encode_result')
    if os.path.exists('encode_result') or os.path.exists('encode_result_name'):
        print('=======编码文件已存在=========')
    else:
        name = seq(glob.glob(path+'/*'))
        print(name)
        for i in range(0,len(name)):
            if i == 0 or i == 1:
                print(name[i],'-=-=-=-=-=-=-=-=-=-')
                with open(name[i],'r') as f:
                    for j in f:
                        line = j.strip().split()
                        # print(line,len(line))
                        # exit()
                        with open('encode_result','a',encoding='utf-8') as f_:                                                  
                                f_.write('%s\n'%j)
            # if i == 1:
                # with open(name[i],'r') as f:
                    # for j in f:
                        # with open('encode_result_name','a',encoding='utf-8') as f_:                                                  
                                # f_.write('%s\n'%j)
def load_data(file_):#,file):
    
    data=[]
    file_lst=[]
    labels = []
    for line in open(file_,"r",encoding="utf-8"):
        # print(len(line.strip().split("\t")))
        # da,label =line.strip().split("\t")
        # print(da,'=====',label)
        # exit()
        try:
        
            na,da,label =line.strip().split("\t")
            file_lst.append(na)
            # print(type(da),len(da),'=====',label)
            # print(na)
            # exit()
            ss = da#.split('[')[-1].split(']')[0].split(',')
            # print(ss,len(ss),'-------------')
            # exit()
            #break
            #print('1111111111111111')
            label=int(label)#.replace("\\","/")
            # print(label)
            # exit()
        #print(da)
            da_=[]
            for x in ss.split("<=>"):
                # print(x,'99999999999')
                # exit()
                try:
                    da_.append(float(x))
                    # print(type(x),'-=-=-=')
                    # exit()
                except:
                    print((x),'0000000000')
                    # exit()
                    da_.append(0.0)
            data.append(da_)
            #da=[float(x) for x in da.strip("<=>")]#(da)
            labels.append(label)
            # print('99999999999999999999999')
        except:
            # print('=====1====')
            # print(len(line.strip().split('\t')),'=====1====')
            # exit()
            pass
            
    # for line in open(file,"r",encoding="utf-8"):
        # path =line.strip().split("\t")
        # try:
            # if len(path[0]) > 10:
            # path =line.strip().split("\t")
            # print(path,len(path[0]))
            # exit()
                # print(path,len(path[0]))
                # file_lst.append(path)
            # else:
                # pass
            
        # except:
            # pass
            # exit()
    # if  len(labels) == len(file_lst):
        # pass
    # else:
    print(len(labels), 'label==name' ,len(file_lst))
    return file_lst,data



def save_data(path,data,name):
    with open(name,"w",encoding="utf-8")as f:
        for pa,da in zip(path,data):
            
            to_write="<=>".join([str(x)for x in da])
            lab = pa.split('/')[-1].split('_')[0]
            f.write("%s\t%s\t%s\n"%(pa,to_write,lab))




#=====================================================================================================================

st=time.time()
# path = input("请输入vit编码数据存放的绝对地址（例如：r'E:\文件\项目列表\以假乱真\VIT-Sklearn\Sklearn\data'）：")
path = 'data'
make_data(path)
file_lst,data=load_data("encode_result")#,"encode_result_name")
method = 'PCA'
#with open('encode_result','r',encoding='utf-8') as f:
data_img = np.array(data)    
#k_lst=[10, 20, 50, 100, 200, 500, 1000, 1200, 1500, 1600, 1700]
k_lst=[1500]
rec_dict=PCA.Do(data_img,k_lst)
#if os.path.exists('result/'):
#    shutil.rmtree('result_pca/')
#except:
#    print('shutilrmtree error=========================')
#    pass
if os.path.exists('result_pca/'):
    pass
else:
    for k,datas in rec_dict.items():
        os.makedirs('result_pca/',exist_ok=True)
        name="result_pca/%s_%s"%(method,k)
        encode=datas["encode"]
        #print(data,encode)
        #exit()
        recover=datas["recover"]
        save_data(file_lst,encode,name)
# print()
#print(file_lst[:10])
print("sample number is %s, sample dim is %s"%(len(data),len(data[0])))
#exit()
m_name = (input('please certain method：(pca/raw)'))
class_num = int(input('请输入数据类别总数：'))

if m_name == 'pca':
    d_name = (input('please print the dim of out:'))
    file_lst,data=load_data("result_pca/PCA_%s"%(d_name))
    if os.path.exists('result/'):
        shutil.rmtree('result/')
    for model_type in CF.config["type"]: 
        model= m.model(class_num=class_num)
        model.build(model_type)
        model.run(data)
        model.show(file_lst)

else:
    if os.path.exists('result/'):
        shutil.rmtree('result/')
    for model_type in CF.config["type"]:
        model= m.model(class_num=class_num)
        model.build(model_type)
        model.run(data)
        model.show(file_lst)


print("聚类完成，一共用时:%s秒"%(time.time()-st))
