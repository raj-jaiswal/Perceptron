#  importing libraries
import numpy as np

#  Activation function
#  Decides whether something belongs to group A or group B
def activation(x):
    if x>=0:
        return 1
    else:
        return -1

#  Main Perceptron Class
class Perceptron:
    #Class Constructor function
    def __init__(self, inputs, lr):
        self.inputs=inputs;
        self.learningRate=lr
        #Starting with Random Weights
        self.weights=(np.random.random(inputs+1)-0.5)*2
    
    #Predicts based on a given list of Values
    def predict(self, i):
        #Converts the given list to a Numpy Array
        inputs=i.copy()
        inputs.append(1)
        inputs=np.array(inputs)
        #Find output with the Numpy Array
        product=np.matmul(inputs,self.weights)
        output=activation(product)
        return output
    
    #Trains the Perceptron with the test data and target
    def train(self,i,target):
        #Converts the given list to a Numpy Array
        inputs=i.copy()
        inputs.append(1)
        inputs=np.array(inputs)
        #Find output with the Numpy Array
        product=np.matmul(inputs,self.weights)
        output=activation(product)
        #Find The error of the system
        err=target-output
        #Change the weights based on the error
        self.weights+=inputs*err*self.learningRate