# Author: Karthik Reddy Pagilla

import sys

def find_valid_neighbourhood(vertex, graph_size):
    neighbours = []
    neighbourhood = [(1, 1), (1, 0), (0, 1), (1, -1), (-1, 1), (0, -1), (-1, 0), (-1, -1)]
    x, y = vertex
    for u, v in neighbourhood:
        new_vertex = x+u, y+v
        if 0 <= (x + u) < graph_size and 0 <= (y + v) < graph_size:
            neighbours.append(new_vertex)

    return neighbours

def walk_through(graph, vertex, given_word, path, dict_words):
    word = given_word
    valid_word = ""
    path_traversed = path

    if len(path_traversed) == (len(graph) * len(graph[0])):
        return ""

    neighbours = find_valid_neighbourhood(vertex, len(graph))
    for neighbour in neighbours:
        if neighbour not in path_traversed:
            new_word = word + graph[neighbour[0]][neighbour[1]]
            path_traversed.append(neighbour)
            temp = walk_through(graph, neighbour, new_word, path_traversed, dict_words)
            if dictionary_check(dict_words, temp) is True and 3 <= (len(temp)) <= 16:
                valid_word = temp

    return valid_word

def boggle(graph, dict_words):
    word_list = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            word = walk_through(graph, (i, j), "", [], dict_words)
            if word is not "":
                word_list.append(word)
    return word_list

def slice_dictionary(dict_words, size):

    filtered_list = [x for x in dict_words if len(x) == size]

    return filtered_list

f = open('/content/american', 'r')
dict_words = []
lines = f.readlines()
for line in lines:
    dict_words.append(line.strip().lower())
f.close()

file = open('/content/input1', 'r')
lines = file.readlines()
n = 0
graph = []
for line in lines:
    tokens = list(line.strip().lower())
    graph.append(tokens)

def three_words(graph, vertex, path, new_word, result, dictionary, visited):
    path_travelled = path

    if len(path_travelled) > 16: 
        return result

    word = new_word

    neighbours = find_valid_neighbourhood(vertex, len(graph))

    for neighbour in neighbours:
        if neighbour not in path_travelled and neighbour not in visited:
            word = word + graph[neighbour[0]][neighbour[1]]
            print(word)
            path_travelled.append(neighbour)
            print(path_travelled)
            if len(path_travelled) == 3:
                sliced = slice_dictionary(dictionary, 3)
                if dict_check(sliced, word):
                    result.append(word)
                    word = word[:-1]
                    path_travelled = path_travelled[:-1]
                    visited.append(neighbour)
                else:
                    word = word[:-1]
                    path_travelled = path_travelled[:-1]
                    visited.append(neighbour)
            if len(path_travelled) < 3:
                path_travelled = path_travelled[:-1]
                visited.append(neighbour)
                three_words(graph, neighbour, path_travelled, word, result, dictionary, visited)
            if len(path_travelled) > 3:
                word = ""
                path_travelled = []
                visited = []

    return result

hell = three_words(graph, (0,3), [(0,3)], "a", [], dict_words, [])

def dict_check(dictionary, word):
    beg = 0
    end = len(dictionary)

    while beg <= end:
        mid = beg + ((end - beg) // 2)

        found = (word == dictionary[mid])
        great = (word > dictionary[mid])
        
        if(found):
            return found

        if (great):
            beg = mid + 1
        else:
            end = mid - 1

    return False