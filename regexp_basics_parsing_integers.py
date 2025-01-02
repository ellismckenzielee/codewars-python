# regexp basics - parsing integers
# https://www.codewars.com/kata/5682e1082cc7862db5000039

import re
def to_integer(string):
    matches = re.match(f"^[+-]*([0-9]+|(0x)[0-9a-fA-F]+|(0b)[0-1]+|(0o)[0-7]+)\Z", string)
    if matches:
        matched_num = matches.string
        if "0x" in matched_num:
            return int(matched_num, 16)
        elif "0b" in matched_num:
            return int(matched_num, 2)
        elif "0o" in matched_num:
            return int(matched_num, 8)
        else:
            return int(matched_num)
