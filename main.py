import os

# One sentence, 171 characters: the whole entry, written verbatim.
LINE = "Tell make.fun your app idea tonight in plain words and wake up to a first version you can actually tap and use \u2014 no code to learn, and you only pay for the one you'd keep."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
