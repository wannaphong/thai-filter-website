from datasets import load_dataset
from tqdm.auto import tqdm
import json
from block_web.block import check_block,check_block_title
from block_web.block_text import check
# ds = load_dataset("uonlp/CulturaX",
#                   language="th",
#                   use_auth_token=True,
#                   split="train",
#                   streaming=True)

with open("/ist/hplt12_clean.jsonl","w",encoding="utf-8") as out:
    print("/ist/hplt12/th_1.jsonl")
    with open("/ist/hplt12/th_1.jsonl", "r",encoding="utf-8-sig") as f:
        for line in tqdm(f,total=1784449):
            if line:
                t = json.loads(line)
                if check_block(t["url"]):
                    continue
                elif check_block_title(t["text"]):
                    _t = check(t["text"])["labels"][0] != "อื่น ๆ"
                    if _t:
                        continue
                ss = json.dumps({"meta": {"src":"hplt12",'url':t['url'],"collection":t['collection'],"id":t['id']}, "text": t['text']}, ensure_ascii=False)
                out.write(ss + "\n")
    print("/ist/hplt12/th_2.jsonl")
    with open("/ist/hplt12/th_2.jsonl", "r",encoding="utf-8-sig") as f:
        for line in tqdm(f,total=2805778):
            if line:
                t = json.loads(line)
                if check_block(t["url"]):
                    continue
                elif check_block_title(t["text"]):
                    _t = check(t["text"])["labels"][0] != "อื่น ๆ"
                    if _t:
                        continue
                ss = json.dumps({"meta": {"src":"hplt12",'url':t['url'],"collection":t['collection'],"id":t['id']}, "text": t['text']}, ensure_ascii=False)
                out.write(ss + "\n")
    print("/ist/hplt12/th_3.jsonl")
    with open("/ist/hplt12/th_3.jsonl", "r",encoding="utf-8-sig") as f:
        for line in tqdm(f,total=2716649):
            if line:
                t = json.loads(line)
                if check_block(t["url"]):
                    continue
                elif check_block_title(t["text"]):
                    _t = check(t["text"])["labels"][0] != "อื่น ๆ"
                    if _t:
                        continue
                ss = json.dumps({"meta": {"src":"hplt12",'url':t['url'],"collection":t['collection'],"id":t['id']}, "text": t['text']}, ensure_ascii=False)
                out.write(ss + "\n")
    print("/ist/hplt12/th_4.jsonl")
    with open("/ist/hplt12/th_4.jsonl", "r",encoding="utf-8-sig") as f:
        for line in tqdm(f,total=885833):
            if line:
                t = json.loads(line)
                if check_block(t["url"]):
                    continue
                elif check_block_title(t["text"]):
                    _t = check(t["text"])["labels"][0] != "อื่น ๆ"
                    if _t:
                        continue
                ss = json.dumps({"meta": {"src":"hplt12",'url':t['url'],"collection":t['collection'],"id":t['id']}, "text": t['text']}, ensure_ascii=False)
                out.write(ss + "\n")