from datasets import load_dataset
from tqdm.auto import tqdm
import ujson
from block_web.block import check_block,check_block_title

with open("/mark14/raw_thai/hplt12_clean.jsonl","w",encoding="utf-8") as out:
    with open("/mark14/raw_thai/hplt12.jsonl", "r",encoding="utf-8-sig") as f:
        for line in tqdm(f,total=8192707):
            if line:
                t = ujson.loads(line)
                if check_block(t["meta"]["url"]):
                    continue
                elif check_block_title(t["text"]):
                    continue
                out.write(line)
