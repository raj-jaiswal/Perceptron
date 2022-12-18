import matplotlib.pyplot as plt
import numpy as np
import Perceptron

points=np.random.random((500,2))

def f(x):
    return -0.9*x+1
         
def checkPoint(point):
    if point[1]>f(point[0]):
        return 1
    else:
        return -1
        
def train(ppt):
    for i in range(10):
        for point in points:
            ppt.train(point.tolist(), checkPoint(point))

def iterate(ppt):
    plt.clf()
    fig=plt.figure()
    ax=fig.add_subplot(111)
    plt.axis('off')
    plt.xlim(0,1)
    plt.ylim(0,1)
    colors=[]
    for point in points:
        if ppt.predict(point.tolist())==1:
            colors.append('r')
        else:
            colors.append('b')
    xs=[]
    ys=[]
    for i in range(len(points)):
        xs.append(points[i,0])
        ys.append(points[i,1])
    plt.scatter(xs,ys,c=colors,s=10)
    plt.plot([0,1],[f(0),f(1)],'#000')
    ax.set_aspect('equal',adjustable='box')
    plt.show()
    
    train(ppt)

def main():
    ppt=Perceptron(2,0.1)
    
    while True:
        iterate(ppt)
    
if __name__=='__main__':
    main()