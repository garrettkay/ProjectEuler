sumdigit = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
sumten = 3
sumteens = 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8

sumtwenties = 6 * 10 + sumdigit
sumthirties = 6 * 10 + sumdigit
sumforties = 5 * 10 + sumdigit
sumfifties = 5 * 10 + sumdigit
sumsixties = 5 * 10 + sumdigit
sumseventies = 7 * 10 + sumdigit
sumeighties = 6 * 10 + sumdigit
sumnineties = 6 * 10 + sumdigit

sumdoubledigits = sumdigit + sumten + sumteens + sumtwenties + sumthirties + sumforties + sumfifties + sumsixties + sumseventies + sumeighties + sumnineties

sum = sumdigit * 100 + 7 * 900 + 3 * 891 + sumdoubledigits * 10 + 3 + 8

print(sum)