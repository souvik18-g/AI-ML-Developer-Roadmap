def is_palindrome(s):
    s = s.lower()

    if s == s[::-1]:
        return True
    else:
        return False

print("madam:", is_palindrome("madam"))
print("python:", is_palindrome("python"))