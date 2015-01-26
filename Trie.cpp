#include <iostream>
#include <string.h>

#define ARRAY_SIZE(a) sizeof(a) / sizeof(a[0])
#define ALPHABET_SIZE 26
#define CHAR_TO_INDEX(c) ((int)c - (int)'a')

using namespace std;

typedef struct TrieNode_ TrieNode;
struct TrieNode_{
  bool is_leaf;
  TrieNode *children[ALPHABET_SIZE];
};

class TrieTree{
  TrieNode *root;
  TrieNode *getNode(void);
  public:
    int count;
    TrieTree(){
      root = getNode();
      count = 0;
    }
    void insert(char key[]);
    bool search(char key[]);
    bool help_search_with_wildcard(TrieNode * pt, char key[], int level);
    bool search_with_wildcard(char key[]);
};

TrieNode* TrieTree::getNode(void){
  TrieNode *pNode = new TrieNode;
  if (pNode){
    pNode -> is_leaf = false;
    for (int i = 0; i < ALPHABET_SIZE; i ++){
      pNode -> children[i] = NULL;
    }
  }
  return pNode;
}

void TrieTree::insert(char key[]){
  int level;
  int length = strlen(key);
  int index;
  TrieNode *pCrawl = root;
  count ++;

  for (level = 0; level < length; level ++){
    index = CHAR_TO_INDEX(key[level]);
    if (!pCrawl -> children[index]){
      pCrawl -> children[index] = getNode();
    }
    pCrawl = pCrawl -> children[index];
  }
  pCrawl -> is_leaf = true;
}

bool TrieTree::search(char key[]){
  //printf("Now you are searching key %s\n", key);
  int level;
  int length = strlen(key);
  int index;
  TrieNode *pCrawl = root;
  for (level = 0; level < length; level ++){
    index = CHAR_TO_INDEX(key[level]);
    if (!pCrawl -> children[index])
      return false;
    pCrawl = pCrawl -> children[index];
  }
  return (pCrawl && pCrawl -> is_leaf);
}

bool TrieTree::help_search_with_wildcard(TrieNode* pt, char key[], int level){
  if (level == strlen(key))
    return pt -> is_leaf;
  if (key[level] == '*'){
    for (int i = 0; i < ALPHABET_SIZE; i ++){
      if (pt -> children[i] && help_search_with_wildcard(pt -> children[i], key, level + 1))
        return true;
    }
    return false;
  }
  int key_idx = CHAR_TO_INDEX(key[level]);
  if (pt -> children[key_idx])
    return help_search_with_wildcard(pt -> children[key_idx], key, level + 1);
  return false;
}

bool TrieTree::search_with_wildcard(char key[]){
  return help_search_with_wildcard(root, key, 0);
}

int main(){
  char keys[][8] = {"the", "a", "there", "answer", "any", "by", "bye", "their"};
  TrieTree trie;
  char output[][32] = {"Not present in trie", "Present in trie"};
  for(int i = 0; i < ARRAY_SIZE(keys); i++){
        trie.insert(keys[i]);
  }
  printf("%s --- %s\n", "the", output[trie.search_with_wildcard("the")]);
  printf("%s --- %s\n", "these", output[trie.search_with_wildcard("these")]);
  printf("%s --- %s\n", "their", output[trie.search_with_wildcard("their")]);
  printf("%s --- %s\n", "thaw", output[trie.search_with_wildcard("thaw")]);
  printf("%s --- %s\n", "th*", output[trie.search_with_wildcard("th*")]);
  printf("%s --- %s\n", "***he", output[trie.search_with_wildcard("***he")]);
  return 0;
}

