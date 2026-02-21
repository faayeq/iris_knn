from sklearn.datasets import load_iris
import random

dataset = load_iris()
samples = [10,25,49,50,51,100,101]
SAMPLE_NUM = 15
features_X=dataset.data
trgt_labels_y=dataset.target


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

    fts_and_lbls = [features_X[0], trgt_labels_y[0]]
    for i in range(1, SAMPLE_NUM):
        fts_and_lbls .append( [features_X[i], trgt_labels_y[i]])

    random.shuffle(fts_and_lbls)

    #now to split them back

    for i in range(0, SAMPLE_NUM):
        features_X[i], trgt_labels_y[i] = fts_and_lbls[i]
        

        




def main():
    print(  "Hello from wine-knn!")
    print(dataset.target[samples])  # format to print the class of a sample (0,1,2) 
    print(dataset.target_names[dataset.target[samples]]) # to print the names of the samples' classes
    print(dataset.data[samples]) #this is for feature value, not for feature name
    p = [4,5]
    q=[7,8]
    
    pminusq=euclidean_distance(p,q)
    print(pminusq)

    random.shuffle(dataset.data)
    print(dataset.target[samples])  # format to print the class of a sample (0,1,2) 
    print(dataset.target_names[dataset.target[samples]]) # to print the names of the samples' classes
    print(dataset.feature_names[0])
    print(dataset.feature_names[1])
    print(dataset.feature_names[2])
    print(dataset.feature_names[3])

    



if __name__ == "__main__":
    main()
