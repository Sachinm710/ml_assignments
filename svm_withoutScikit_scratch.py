import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np


class Support_Vector_Machine:
    
    def __init__(self, visualisation = True):
        self.visualisation = visualisation
        self.colors = {1:'r', -1:'b'}
        
        if self.visualisation:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1,1,1)

    # TRAIN
    def fit(self,data):
        # The data is used to train or used for optmization
        self.data = data
        # {||w|| : [w,b]} THIS DICTIONARY HOLDS ALL THE POSSIBLE OPTIMIZATION VALUES 
        opt_dict = {}
        
        transform = [[1,1],
                    [-1,-1],
                    [-1,-1],
                    [1,-1]]

        # THIS IS TO CHOSE FEATURE SET VALUE TO START THE OPTIMISATION
        all_data = []

        for yi in self.data:
            for featureset in self.data[yi]:
                for features in featureset:
                    all_data.append(features)

        self.max_features_value = max(all_data)
        self.min_features_value = min(all_data)
        all_data = None

        
        # STEP SIZES TO ITERATE DOWN
        step_sizes = [self.max_features_value *0.1,
                      self.max_features_value *0.01,
                      self.max_features_value *0.001,]

        # Expensive for b
        b_range_multiple = 2
        b_multiple = 5
        latest_optimum = self.max_features_value*10

        for step in step_sizes:
            w = np.array([latest_optimum,latest_optimum])
            # we can do this because convex
            optimized = False
            
            while not optimized:
                # How much step to chose # ex {-50 to 50 with step of step*b_multiple}
                for b in np.arange(-1*(self.max_features_value*b_range_multiple),self.max_features_value*b_range_multiple,step*b_multiple):

                    for transformation in transform:
                        w_t = w*transformation
                        found_option = True
                        # weakest link in SVM
                        # yi(xi.w+b)>=1 # constraint function
                        for i in self.data:
                            for xi in self.data[i]:
                                yi = i
                                if not yi*(np.dot(w_t,xi)+b) >= 1:
                                    found_option = False
                                    
                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t,b]

                    if w[0] < 0:
                        optimised = True
                        print('optimised a step')
                    else:
                        w = w-step

            norms = sorted([n for n in opt_dict])
            opt_choice = opt_dict[norms[0]]

            self.w = opt_choice[0]
            self.b = opt_choice[1]
            latest_optimum = opt_choice[0][0] + step*2
                        
        for i in self.data:
            for xi in self.data[i]:
                yi=i
                print(xi,':',yi*(np.dot(self.w,xi)+self.b))

                
    # PREDICTION
    def predict(self,features):
        # sign(x.w+b)
        classification = np.sign(np.dot(np.array(features),self.w)+self.b)
        if classification != 0 and self.visualisation:
            self.ax.scatter(features[0], features[1], s=200, marker = '*', c=self.colors[classification])
        return classification


    def visualise(self):
        for i in data_dict:
            for x in data_dict[i]:
                self.ax.scatter(x[0],x[1],s=100, color=self.colors[i])


    def hyperplane(self, x, w, b, v):
        #(x.w+b)
        #
        return (-w[0]*x-b+v) / w[1]

        datarange = (self.min_feature_value*0.9,self.max_feature_value*1.1)
        hyp_x_min = datarange[0]
        hyp_x_max = datarange[1]

        # (w.x+b) = 1
        # positive support vector hyperplane
        psv1 = hyperplane(hyp_x_min, self.w, self.b, 1)
        psv2 = hyperplane(hyp_x_max, self.w, self.b, 1)
        self.ax.plot([hyp_x_min,hyp_x_max],[psv1,psv2], 'k')

        # (w.x+b) = -1
        # negative support vector hyperplane
        nsv1 = hyperplane(hyp_x_min, self.w, self.b, -1)
        nsv2 = hyperplane(hyp_x_max, self.w, self.b, -1)
        self.ax.plot([hyp_x_min,hyp_x_max],[nsv1,nsv2], 'k')

        # (w.x+b) = 0
        # positive support vector hyperplane
        db1 = hyperplane(hyp_x_min, self.w, self.b, 0)
        db2 = hyperplane(hyp_x_max, self.w, self.b, 0)
        self.ax.plot([hyp_x_min,hyp_x_max],[db1,db2], 'y--')

        plt.show()        
## Dictionary for positive and negative classes

data_dict = {-1:np.array([[1,7],
                         [2,8],
                         [3,8],]),
             
             1:np.array([[5,1],
                         [6,-1],
                         [7,3],])}


svm = Support_Vector_Machine()
svm.fit(data=data_dict)
svm.visualize()
