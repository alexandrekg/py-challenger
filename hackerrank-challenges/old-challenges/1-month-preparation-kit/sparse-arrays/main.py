def matchingStrings(strings, queries):
    results = []
    for query in queries:
        counter = 0

        for string in strings:
            if query == string:
                counter += 1
        results.append(counter)

    return results

if __name__ == '__main__':
    strings = ['ab', 'ab', 'abc']
    queries = ['ab', 'abc', 'bc']
    matchingStrings(strings, queries)
