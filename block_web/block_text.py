import os
from tqdm.auto import tqdm
from transformers import pipeline


classifier = pipeline("zero-shot-classification", model="MoritzLaurer/ernie-m-base-mnli-xnli",device="cuda:1") # MoritzLaurer/multilingual-MiniLMv2-L12-mnli-xnli

candidate_labels = ["มีเนื้อหาส่งเสริมการพนัน คาสิโน บาคาร่า บ่อน โฆษณาพนัน", "มีเนื้อหารูปโป๊ คลิปโป๊ หาคู่เย็ด สาวขายตัว", "อื่น ๆ","มีการซื้อขายยาเสพติด เช่น ขายยาบ้า ขายยาเสียสาว ขายฝิ่น ขายเฮโรอีน"]
def check(text):
    output = classifier(text, candidate_labels, multi_label=False)
    return output