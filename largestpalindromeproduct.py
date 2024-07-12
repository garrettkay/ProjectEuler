largestpalindrome = 9009

for i in range(850,1000):
    for j in range(i,1000):
        product = str(i*j)
        if product == product[::-1] and i*j > largestpalindrome:
            largestpalindrome = i*j

print(largestpalindrome)