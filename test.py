import re

val = "010123456781"
pattern = """^01[016789][0-9]\d{6,7}$"""

if re.match(pattern,val):
    print("""match""")
else:
    print("""mismatch""")




