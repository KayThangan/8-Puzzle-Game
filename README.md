# 8-Puzzle Game

The 8-puzzle game consists of a 3 x 3 board. There are 9 tiles in the
board are numbered from 1 to 8, and one tile is blank tile. I
created A* search algorithm to solve the 8 puzzle game using the
two heuristic functions(Euclidean and Manhattan).

To calculate the Euclidean distance is by:
sqrt((new_node.x - goal_node.x) ** 2 +
(new_node.y - goal_node.y) ** 2)

To calculate the Manhattan distance is by:
abs(new_node.x - goal_node.x) + abs(new_node.y - goal_node.y)

During the execution, user need to input the start board, goal board
and enter E for Euclidean or M for Manhattan.

In the user input of the board size, start and goal state. The user must enter
0 to represented as a blank tile. Also, when inputting the values for
the board, it will guide the user by telling what value they would like to input
for each position in the board.

### Prerequisites

What things you need to install the software and how to install
them

```
install python 3.6.0+
```

## Running the code

Running the main application
```
python eight_puzzle_game.py
```

# K-Means Clustering

Recognise hand-written digits by loading the data from the Python
package as follows:

from sklearn.datasets import load digits
digits = load digits()

The dataset contain 1,797 samples and 64 features. I created own
kmeans algorithm to cluster and analyse the data by finding the
accuracy in the similarity of the digits within the data, using
Elbow method to give an optimal k value, using PCA graph method
and TSNE graph method to show the clustered data in the scatter
graph.

I created own kMeans class containing the functions are:
  initialise_centroids
  compute_centroids
  calculate_distance
  find_closest_cluster
  compute_SSE
  fit
  predict_likeliest_clusters

### Prerequisites and Install

What things you need to install the software and how to install
them

```
install python 3.6.0+
```
```
pip install scikit-learn
```
```
pip install matplotlib
```
```
pip install pandas
```
```
pip install numpy
```
```
pip install scipy
```

## Running the code

Running the main application
```
python k-means.py
```

#  Classification of urban areas

Analysing a real-world data set which I have used in my own research. 
The data set contains information on a variety of aspects of a city, such as the 
types of building, the types of points of interest (restaurants, cafes, museums, 
attractions, ...), and other interesting features which can be found in different 
areas of most cities. An interesting topic in the study of cities is what encourages 
different people to live in different parts of a city.

This creates a decision tree that uses features of urban environments can be used 
to predict which age group is the most present in each area.

### Prerequisites

What things you need to install the software and how to install
them

```
install python 3.6.0+
```
```
pip install scikit-learn
```
```
pip install matplotlib
```
```
pip install pandas
```
```
pip install scipy
```

## Running the code

Running the main application
```
python decision_tree.py
```

## Built With
* Python

## License

This project is licensed under the MIT License - see the
[LICENSE.md](LICENSE.md) file for details
