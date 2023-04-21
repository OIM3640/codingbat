def xyz_there(str):
    """
    Return True if the given string contains an appearance of "xyz" 
    where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
    """
    xyz_count = 0
    if len(str) == 3:
        return "xyz" in str
    for i in range(len(str)-3):
        if "xyz" in str[i:i+4] and "." not in str[i]:
            xyz_count += 1
        elif "xyz" in str[i:i+4] and "." in str[i]:
            xyz_count -= 1
    return xyz_count > 0


print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))
