import sentiment

default_text = '''
    The FBI and several congressional committees are running multipronged
    investigations of possible cooperation between the Trump campaign and
    Russia and potential obstruction of justice by Trump. The president has
    repeatedly called the probe a "witch hunt" and a "phony story."
    '''

def main():
    result = sentiment.get_vector(default_text)
    print(result)

if __name__ == '__main__':
    main()
