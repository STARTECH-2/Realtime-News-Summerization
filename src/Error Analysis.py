from summarizer import Summarizer
import evaluate
import os
import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from nltk.tokenize import sent_tokenize
from heapq import nlargest

text = os.stat("text1.txt")
text_len = text.st_size
text_file = open("text1.txt",'r')
summary = os.stat("summerized1.txt")
summary_len = summary.st_size
summary_file = open("summerized1.txt",'r')
rouge = evaluate.load('rouge')

# BERT MODEL - NEEDS ATTENTION
# bert_model = Summarizer()
# bert_summary = ''.join(bert_model(text_file.read(), min_length=60))
# print("BERT SUMMARY\n")
# bs = sent_tokenize(bert_summary)
# file = open("bert_summerization.txt", "x")
# file.close()
# for i in bs:
#     print(i)
#     file = open("bert_summerization.txt", "a")
#     file.write(str(i))
#     file.close()
# bert = open("bert_summerization.txt",'r')
# bert_score = rouge.compute(predictions=bert.readlines(), references=summary_file.readlines())
# print("\n\nBERT SCORE :",bert_score)
# bert.close()
# os.remove("bert_summerization.txt")

# SUMY MODEL - SUCCESS
# LANGUAGE = "english"
# parser = PlaintextParser.from_file("text1.txt", Tokenizer(LANGUAGE))
# summarizer = LexRankSummarizer()
# sumy_summary = summarizer(parser.document, 6)
# print("SUMY SUMMERIZATION\n")
# file = open("sumy_summerization.txt", "x")
# file.close()
# for i in sumy_summary:
#     print(i)
#     file = open("sumy_summerization.txt", "a")
#     file.writelines(str(i))
#     file.close()
# sumy = open("Sumy_summerization.txt",'r')
# sumy_score = rouge.compute(predictions=sumy.readlines(), references=summary_file.readlines())
# print("\n\nSUMY SCORE :",sumy_score)
# sumy.close()
# os.remove("sumy_summerization.txt")

# USING NLTK - NEEDS ATTENTION

# tokens = word_tokenize(text_file.read())
# stop_words = stopwords.words('english')
# punctuation = punctuation + '\n'
# word_frequencies = {}
# for word in tokens:
#     if word.lower() not in stop_words:
#         if word.lower() not in punctuation:
#             if word not in word_frequencies.keys():
#                 word_frequencies[word] = 1
#             else:
#                 word_frequencies[word] += 1
# max_frequency = max(word_frequencies.values())
# for word in word_frequencies.keys():
#     word_frequencies[word] = word_frequencies[word]/max_frequency
# file_data = [line.strip() for line in open("text1.txt")]
# # file_data = text_file.read()
# sent_token = file_data
# sentence_scores = {}
# for sent in sent_token:
#     sentence = sent.split(" ")
#     for word in sentence:
#         if word.lower() in word_frequencies.keys():
#             if sent not in sentence_scores.keys():
#                 sentence_scores[sent] = word_frequencies[word.lower()]
#             else:
#                 sentence_scores[sent] += word_frequencies[word.lower()]
# select_length = int(len(sent_token)*0.3)
# summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
# final_summary = [word for word in summary]
# summary = ''.join(final_summary)
# print("NLTK SUMMERIZATION\n")
# print(summary)
# nltk_score = rouge.compute(predictions=summary, references=summary_file.read())
# print("\n\nNLTK SCORE :",nltk_score)