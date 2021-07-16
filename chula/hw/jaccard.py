# Prog-06: Jaccard Similarity
# ??3?????21 Name ?

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOP_WORDS = stopwords.words('english')
STEMMER = PorterStemmer()

def read_tweets():
    f = open('biden.txt', encoding='utf-8')
    tweets = [line.strip() for line in f.readlines()]
    f.close()
    return tweets

def normalize_text( text ):
    words = []
    for w in word_tokenize(text.lower()):
        if w.isalnum() and w not in STOP_WORDS:
            words.append(STEMMER.stem(w))
    return get_unique( words )

def main():
    tweets = read_tweets()
    norm_tweets = []
    for t in tweets:
        norm_tweets.append( normalize_text(t) )

    print_width = 48
    while True:
        query = input('Query words   : ')
        if query == '': break
        n = int(input('No. of results: '))
        norm_query = normalize_text(query)
        top_n = top_n_similarity(norm_tweets, norm_query, n)
        if len(top_n) == 0:
            print('No matches found.')
        else:
            for tid, jc_coef in top_n:
                show_tweet(tid, tweets[tid], jc_coef, print_width)
        print('-' * print_width)

#--------------------------------------------------------
def get_unique( words ):
    unique_words = list()
    for i in words:
        if i not in unique_words:
            unique_words.append(i)
    return unique_words


def jaccard(words_1, words_2):
    f = []
    for i in words_1:
        for j in words_2:
            if i == j:
                f.append(i)
                break

    jaccard_coef = len(f)/((len(words_1)+len(words_2))-len(f))
    return jaccard_coef



def top_n_similarity(norm_tweets, norm_query, n):
    top_n = []
    for index, values in enumerate(norm_tweets):
        _jaccards = jaccard(norm_tweets[index], norm_query)
        top_n.append([index, _jaccards])
    top_n.sort(key=lambda jaccard: jaccard[1], reverse=True)
    top_n = top_n[:n]

    return top_n



def show_tweet(tweet_id, tweet_content, jc_coef, print_width):
    print()
    print("#{} ({})".format(tweet_id, round(jc_coef, 2)))
    string = '  '
    tweet_content = tweet_content.split()
    k = 1
    for i in tweet_content:
        if len(string) + len(i) > print_width*k:
            string+='\n'
            string+='  '
            k+=1
        string+=i
        string+=' '
    print(string)



#--------------------------------------------
main()
