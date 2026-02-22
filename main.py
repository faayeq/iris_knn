from sklearn.datasets import load_iris
import random

dataset = load_iris()
samples = [10,25,49,50,51,100,101]
SAMPLE_NUM = 150
features_X=dataset.data
trgt_labels_y=dataset.target
X_train = []
X_test = []
y_train = []
y_test =[]

def euclidean_distance(p, q):

    if(len(p) != len(q)):
        print("error, dimensions of points are different")
        return
    
    n = len(p)
    summation=0
    for i in range(0, n):
        summation += (q[i] - p[i])**2 # summation of differences, n-dimensional
    
    e_dist = summation**0.5
    return e_dist

def shuffle_features_and_labels():

    fts_and_lbls = []
    for i in range(0, SAMPLE_NUM):
        fts_and_lbls .append([ features_X[i], trgt_labels_y[i] ])

    random.shuffle(fts_and_lbls)

    #now to split them back

    for i in range(0, SAMPLE_NUM):
        features_X[i], trgt_labels_y[i] = fts_and_lbls[i]
        

def print_details():
    print(  "Hello from iris_knn!")
    print(dataset.target[samples])  # format to print the class of a sample (0,1,2) 
    print(dataset.target_names[dataset.target[samples]]) # to print the names of the samples' classes
    print(dataset.data[samples]) #this is for feature value, not for feature name
    p = [4,5]
    q=[7,8]
    
    pminusq=euclidean_distance(p,q)
    print(pminusq)

    print(dataset.target[samples])  # format to print the class of a sample (0,1,2) 
    print(dataset.target_names[dataset.target[samples]]) # to print the names of the samples' classes
    print(dataset.feature_names[0])
    print(dataset.feature_names[1])
    print(dataset.feature_names[2])
    print(dataset.feature_names[3])
        



def train_test_split():

    train_ratio = 80
    test_ratio = 20 

    training_samples_num = int((train_ratio * SAMPLE_NUM) / 100)
    test_samples_num =(test_ratio * SAMPLE_NUM) / 100

    for i in range(0, training_samples_num):
        X_train.append(features_X[i])
        y_train.append(trgt_labels_y[i])

    for i in range(training_samples_num, SAMPLE_NUM):
        X_test.append(features_X[i])
        y_test.append(trgt_labels_y[i])

        
    print("verifying split: \n")
    print(f"total test samples: {len(y_test)}")
    for i in range(len(dataset.target_names)):
        count = y_test.count(i)
        print(f"class {i} ({dataset.target_names[i]}): {count} samples")


def main():
    shuffle_features_and_labels()
    print_details()
    train_test_split()


if __name__ == "__main__":
    main()
