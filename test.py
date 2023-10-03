import pickle
#import tensorflow as tf
#tf.config.list_physical_devices('GPU')
#file = open('python_how_to_do_it_by_classifier_multiple_iid_to_code.pickle', 'rb')
text_word_vocab = pickle.load(open('text_word_vocab.pickle', 'rb'))
code_token_vocab = pickle.load(open('code_token_vocab.pickle', 'rb'))


print('Showing the pickled data:')

cnt = 0
for item in text_word_vocab:
    print('The data ', cnt, ' is : ', item)
    cnt += 1

count = 0
for item in code_token_vocab:
    print('The data ', count, ' is : ', item)
    count += 1