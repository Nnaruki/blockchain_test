import hashlib
 
key = "abcdefg"
md5 = hashlib.md5(key.encode()).hexdigest()
sha256 = hashlib.sha256(key.encode()).hexdigest()
 
print(md5)
print(sha256)
