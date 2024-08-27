import numpy as np
import datetime
import io

words = None
vectors = None
matches = [""] * 20
wordCount = 0
dimCount = 0

def main():
    global words, vectors, matches, wordCount, dimCount
    inputFile = 'INFO 6143 Week8\FastText100K\FastText100K.txt'

    print("Loading Dictionary....")
    print(datetime.datetime.now())
    load_vectors(inputFile)
    print(datetime.datetime.now())
    print("Dictionary Loaded....")
    print()
    print("Lab #4 Aondokator Joseph and Bernardo da Silva")
    print()
    print("Analogies take the form: A is to B as C is to D")
    print("Example: 'man is to woman as king is to queen'")
    print()
    print("Enter the previous example as: man woman king")
    print("The computer will return the full solution: man is to woman as king is to queen")
    print()

    analogy = "a"
    while analogy != "":
        print()
        print("Lab #4 Aondokator Joseph and Bernardo da Silva")
        print("Enter 3 analogy word tokens: ")
        analogy = input()

        analogy_args = analogy.split(' ')

        if analogy != "":
            if len(analogy_args) != 3:
                print("Must be 3 words, Please redo")
            else:
                print("Processing analogy...")

                vect1 = get_vect(analogy_args[0])
                vect2 = get_vect(analogy_args[1])
                vect3 = get_vect(analogy_args[2])

                vect4 = add_vect(vect2, vect1, -1)
                vect5 = add_vect(vect4, vect3, 1)

                vect6 = np.zeros(dimCount)

                for i in range(len(matches)):
                    matches[i] = ""

                for i in range(len(words)):
                    for j in range(dimCount):
                        vect6[j] = vectors[i, j]
                    cos_similarity = calculate_cosine_similarity(vect5, vect6)
                    match_vect(i, cos_similarity)

                for i in range(len(matches)):
                    args_m = matches[i].split('_')
                    found = False

                    for j in range(len(analogy_args)):
                        if analogy_args[j] == args_m[1]:
                            found = True

                    if not found:
                        # print(args_m[1])
                        print(f"{analogy_args[0]} is to {analogy_args[1]} as {analogy_args[2]} is to {args_m[1]}")
                        print()
                        print("Debug information (top similarities)")
                        print()

                        for x in range(1, len(matches)):
                            print(matches[x].replace("_", " "))

                        break

def load_vectors(fname):
    global words, vectors, wordCount, dimCount
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    wordCount, dimCount = map(int, fin.readline().split())
    words = []
    vectors = []
    for line in fin:
        tokens = line.rstrip().split(' ')
        words.append(tokens[0])
        vectors.append(list(map(float, tokens[1:])))
    vectors = np.array(vectors)



def get_vect(word):
    global words, vectors, dimCount
    vec = np.zeros(dimCount)

    for i in range(wordCount):
        if word == words[i]:
            for j in range(dimCount):
                vec[j] = vectors[i, j]

    return vec

def add_vect(vec1, vec2, op):
    global dimCount
    vec = np.zeros(dimCount)

    for j in range(dimCount):
        if op == 1:
            vec[j] = vec1[j] + vec2[j]
        else:
            vec[j] = vec1[j] - vec2[j]

    return vec

def match_vect(x, cos_sim):
    global words, matches
    s_cos_sim = str(cos_sim)
    d_cos_sim = 0.0

    for i in range(len(matches)):
        if matches[i] != "":
            args = matches[i].split('_')
            d_cos_sim = float(args[0])
        else:
            d_cos_sim = 0.0

        if cos_sim > d_cos_sim:
            matches[-1] = s_cos_sim + "_" + words[x]
            matches.sort(reverse=True)

            break

def calculate_cosine_similarity(vec_a, vec_b):
    dot_prod = dot_product(vec_a, vec_b)
    magnitude_of_a = magnitude(vec_a)
    magnitude_of_b = magnitude(vec_b)

    return dot_prod / (magnitude_of_a * magnitude_of_b)

def dot_product(vec_a, vec_b):
    dot_prod = 0
    for i in range(len(vec_a)):
        dot_prod += (vec_a[i] * vec_b[i])

    return dot_prod

def magnitude(vector):
    return np.sqrt(dot_product(vector, vector))


main()