import os
from pathlib import Path
import glob
from urllib.parse import urlparse
from tqdm.auto import tqdm
from sentence_transformers import SentenceTransformer

source_path = Path(__file__).resolve()
source_dir = source_path.parent

web_list = []

for p in tqdm(list(glob.glob(os.path.join(source_dir,"*.txt")))):
    with open(p,"r") as f:
        for i in f.readlines():
            if i.startswith("#") == False and i!="" and i.startswith("!") == False and i.startswith("[") == False:
                web_list.append(i.strip().replace("||",""))
                if i.startswith("www") == False:
                    web_list.append("www."+i.strip())

word_block = set([
    "xxx",
    "หวย",
    "porn",
    "เย็ด",
    "พนันบอล",
    "คาสิโน",
    "slot",
    "สล็อต",
    "แทงบอล",
    "หวยฮานอย",
    "รูเล็ต",
    "แทงไฮโล",
    "บาคาร่า",
    "UFABET",
    "บิงโก",
    "ไฮโล",
    "น้ำเต้าปูปลา",
    "รูปโป๊",
    "แตกใน",
    "ลักหลับ",
    "แตกนอก",
    "หนังโป๊",
    "ufabtc",
    "ufabet",
    "ยูฟ่าเบท",
    "ข่มขืน",
    "ขืนใจ",
    "คาปาก",
    "คลิปหลุด",
    "ห้องลับ",
    "yed",
    "พนันกีฬา",
    "เเทงหวย",
    "เเทงบอล",
    "หวยลาว",
    "หวยมาเล",
    "gclub",
    "ป๊อกเด้ง",
    "ไพ่",
    "จีคลับ",
    "GClub",
    "GCLUB",
    "ขายตัว",
    "ช่วยตัวเอง",
    "รูปหลุด",
    "แอบถ่าย",
    "กาสิโน",
    "โดจิน",
    "แทงมวย",
    "เเทงมวย",
    "ชักว่าว",
    "ตกเบ็ด",
    "โป๊",
    "รุมโทม",
    "ท่าหมา",
    "ขายหี",
    "หี",
    "ควย",
    "เปิดซิง",
    "เสียซิง",
    "เสียตัว",
    "เสียสาว",
    "พนัน",
    "หวย",
    "ยาม้า",
    "ยาบ้า",
    "สาวขายตัว",
    "เฮโรอีน",
    "ฝิ่น",
    "เดิมพัน"
])

# web_set = set(web_list)

end_block=set([
    ".xyz"
])

def check_block_title(title):
    return any(item in title for item in word_block)

def check_block_word(domain):
    return any(item in domain for item in word_block)

# def check_url(domain):
#     return any(item in domain for item in end_block)

def check_block(url):
    if url =="" or url==None:
        return False
    domain = urlparse(url).netloc
    if domain in word_block:
        return True
    if check_block_word(domain):
        return True
    return False # check_url(domain)