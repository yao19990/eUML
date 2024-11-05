from numpy import *# np
from scipy.io import loadmat
import matplotlib.pyplot as plt
import PIL.Image as I
import matplotlib
matplotlib.use('Agg')

def save_image(x):
    for ll,xx in enumerate(x):
        img=xx.reshape(32,32)
        img_=I.fromarray(int8(img))
        img_.save("%s.png"%ll)
def plot_100_image(x,name):
    fig,ax=plt.subplots(nrows=10,ncols=10,figsize=(10,10))
    for c in range(10):
        for r in range(10):
            ax[c,r].imshow(x[10*c+r].reshape(32,32).T,cmap='Greys_r')
            ax[c,r].set_xticks([])
            ax[c,r].set_yticks([])
    plt.savefig(name)
    plt.close()
def reduce_mean(X):
    X_reduce_mean=X-X.mean(axis=0)
    return X_reduce_mean
def sigma_matrix(X_reduce_mean):
    sigma=(X_reduce_mean.T @ X_reduce_mean)/X_reduce_mean.shape[0]
    return sigma
def usv(sigma):
    u,s,v=linalg.svd(sigma)
    return u,s,v
def project_data(X_reduce_mean, u, k):
    u_reduced = u[:,:k]
    z=dot(X_reduce_mean, u_reduced)
    return z
def recover_data(z, u, k):
    u_reduced = u[:,:k]
    X_recover=dot(z, u_reduced.T)
    # exit()
    return X_recover
    
def calculate_ratios(lst):
    ratios = []
    for i in range(1, len(lst)):
        ratio = lst[i] / lst[i - 1]
        ratios.append(ratio)
    return ratios    
    
def Do(x,k_lst):
    x_reduce_mean=reduce_mean(x)
    # print(x_reduce_mean)
    # exit()
    sigma=sigma_matrix(x_reduce_mean)
    u,s,v=usv(sigma)
    print(s)
    xx=calculate_ratios(s)
    plt.plot(s)
    #plt.show()
    plt.savefig('s.jpg')
    plt.close()
    plt.plot(xx)
    #plt.show()
    plt.savefig('s_ratio.jpg')
    
    
    # print(u,'\n',s,'\n',v)
    # print(u.shape,s.shape,v.shape)
    
    ret_dict={}
    for k in k_lst:
        z=project_data(x_reduce_mean,u,k)
        x_recover=recover_data(z,u,k)
        ret_dict[k]={"recover":x_recover,"encode":z}
        # print(ret_dict[k])
        # exit()
    return ret_dict


if __name__=="__main__":
    faces_data = loadmat('/home/zhouchichun/Tensor/datas/tmp/face/ex7faces.mat')
    X=faces_data['X']
    print(X.shape)
    name="raw.png"
    plot_100_image(X,name)
    k_lst=[100,200,300,400,500]
    x_recover_dict=Do(X,k_lst)
    for k,x_recover in x_recover_dict.items():
        name="%s.png"%k
        recover=x_recover["recover"]
        encode=x_recover["encode"]
        # print(encode.shape)
        plot_100_image(recover,name)
