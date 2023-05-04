# import evaluate
from summarizer import Summarizer
import os
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from summarizer import TransformerSummarizer

text = os.stat("text4.txt")
text_len = text.st_size
text_file = open("text4.txt",'r')
summary = os.stat("summerized4.txt")
summary_len = summary.st_size
summary_file = open("summerized4.txt",'r')
# rouge = evaluate.load('rouge')



# BERT MODEL
bert_model = Summarizer()
bert_summary = ''.join(bert_model(text_file.read(), min_length=60))
print("BERT SUMMARY\n")
print(bert_summary)
# bs = sent_tokenize(bert_summary)
# s = ""
# for i in bs:
#     for j in i:
#         if j!="\n":
#             s+=j
# file = open("bert_summerization.txt", "x")
# file.close()
# file = open("bert_summerization.txt", "a")
# file.write(str(s))
# bert_s = os.stat("bert_summerization.txt")
# bert_size = bert_s.st_size
# bert = open("bert_summerization.txt",'r')
# print("\n\nBERT SCORE : ",sentence_bleu(summary_file.readlines(), bert.readlines()))
# bert.close()
# os.remove("bert_summerization.txt")




# SUMY MODEL
LANGUAGE = "english"
parser = PlaintextParser.from_file("text1.txt", Tokenizer(LANGUAGE))
summarizer = LexRankSummarizer()
sumy_summary = summarizer(parser.document, 6)
print("SUMY SUMMERIZATION\n")
print(sumy_summary)
# file = open("sumy_summerization.txt", "x")
# file.close()
# for i in sumy_summary:
#     print(i)
#     file = open("sumy_summerization.txt", "a")
#     file.writelines(str(i))
#     file.close()
# sumy = open("Sumy_summerization.txt",'r')
# sumy_score = rouge.compute(predictions=sumy.readlines(), references=summary_file.readlines()
# sumy.close()
# os.remove("sumy_summerization.txt")





# Using XLNET
body = text_file.read()
model = TransformerSummarizer(transformer_type="XLNet",transformer_model_key="xlnet-base-cased")
result = model(body, min_length=60)
full = ''.join(result)
print("XLNET SUMMERIZATION\n")
print(full)
# print("\n\nXLNET SCORE : ",sentence_bleu(summary_file.readlines(), full))
