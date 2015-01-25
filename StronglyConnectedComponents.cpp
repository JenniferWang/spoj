//Find strongly connected components in a graph
//implementation of Kosaraju’s algorithm
#include <iostream>
#include <list>
#include <stack>
#include <stdio.h>

using namespace std;

class Graph{
  int num_v;
  list<int> *adj; 
  void find_finishing_time(int num_v, bool visited[], stack<int> &trav_stack);
  void dfs(int start, bool visited[]);
public:
  Graph(int v);
  ~Graph();
  void add_edge(int u, int v);
  void printSCCs();
  Graph get_reverse_graph();
};

Graph::Graph(int v){
  this -> num_v = v;
  adj = new list<int>[v];
}

Graph::~Graph(){
  delete []adj;
}

void Graph::dfs(int start, bool visited[]){
  visited[start] = true;
  cout << start << " ";
  list<int>::iterator i;
  for (i = adj[start].begin(); i != adj[start].end(); i ++){
    if (! visited[*i]){
      dfs(*i, visited);
    }
  }
}

Graph Graph::get_reverse_graph(){
  Graph reversed(num_v);
  for (int v = 0; v < num_v; v ++){
    list<int>::iterator i;
    for (i = adj[v].begin(); i != adj[v].end(); ++i){
      reversed.adj[*i].push_back(v);
    }
  }
  return reversed;
}

void Graph::add_edge(int u, int v){
  adj[u].push_back(v);
}

void Graph::find_finishing_time(int node, bool visited[], stack<int> &trav_stack){
  visited[node] = true;
  list<int>::iterator i;
  for (i = adj[node].begin(); i != adj[node].end(); ++i){
    if (!visited[*i])
      find_finishing_time(*i, visited, trav_stack);
  }
  trav_stack.push(node);
}

void Graph::printSCCs(){
  stack<int> trav_stack;
  bool *visited = new bool[num_v];
  for (int i = 0; i < num_v; i ++)
    visited[i] = false;

  for (int i = 0; i < num_v; i ++){
    if (!visited[i])
      find_finishing_time(i, visited, trav_stack);
  }

  Graph reversed_graph = get_reverse_graph();

  for (int i = 0; i < num_v; i ++)
    visited[i] = false;

  while(trav_stack.empty() == false){
    int node = trav_stack.top();
    trav_stack.pop();
    if (!visited[node]){
      reversed_graph.dfs(node, visited);
      cout << endl;
    }
  }
}

int main(int argc, char *argv[]){
  // int u, v;
  // int num_v;
  // int num_e;
  // cin >> num_v >> num_e;
  // Graph g(num_v);
  // for (int i = 0; i < num_e; i ++){
  //   cin >> u >> v;
  //   g.add_edge(u, v);
  // }
  
  Graph g(5);
  g.add_edge(1, 0);
  g.add_edge(0, 2);
  g.add_edge(2, 1);
  g.add_edge(0, 3);
  g.add_edge(3, 4);
  cout << "Following are strongly connected components in given graph \n";
  g.printSCCs();
  return 0;
}
