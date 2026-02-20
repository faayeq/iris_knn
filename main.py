from sklearn.datasets import load_iris

dataset = load_iris()
samples = [10,25,49,50,51,100,101]
features_X=dataset.data
trgt_labels_y=dataset.target


def euclidean_distance(p, q):

    if(len(p) != len(q)):
        print("error, dimensions of points are different")
        return
    for(i in range())


def main():
    print(  "Hello from wine-knn!")
    print(dataset.target[samples])  # format to print the class of a sample (0,1,2) 
print(dataset.target_names[dataset.target[samples]]) # to print the names of the samples' classe


if __name__ == "__main__":
    main()
