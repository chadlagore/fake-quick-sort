import textblob as tb


def get_vector(text):
    blob = tb.TextBlob(text)
    return {
        'language': blob.detect_language(),
        'number_of_sentences': len(blob.sentences),
        'avg_sentence_polarity': sum([
            i.sentiment.polarity for i in blob.sentences
        ]) / len(blob.sentences),
        'avg_sentence_subjectivity': sum([
            i.sentiment.subjectivity for i in blob.sentences
        ]) / len(blob.sentences),
        'avg_sentence_length': sum([
            len(i) for i in blob.sentences
        ]) / len(blob.sentences),
        'avg_spelling': sum(
            [i.spellcheck()[0][1] for i in blob.words
        ]) / len(blob.words)
    }
