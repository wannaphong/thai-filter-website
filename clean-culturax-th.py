from datasets import load_dataset
from tqdm.auto import tqdm
import json
from block_web.block import check_block,check_block_title
from block_web.block_text import check
ds = load_dataset("uonlp/CulturaX",
                  language="th",
                  use_auth_token=True,
                  split="train",
                  streaming=True)

with open("/ist/th_culturax_data_new.jsonl","w",encoding="utf-8") as out:
    for t in tqdm(ds,total=20960550+1):
        if check_block(t["url"]):
            continue
        elif check_block_title(t["text"]):
            _t = check(t["text"])["labels"][0] != "อื่น ๆ"
            if _t:
                continue
        # elif check(t["text"])["labels"][0] != "อื่น ๆ":
        #     continue
        else:
            ss = json.dumps({"meta": {"src":"uonlp/CulturaX",'source':t['source'],'url':t['url'],'timestamp':t['timestamp']}, "text": t['text']}, ensure_ascii=False)
            out.write(ss + "\n")