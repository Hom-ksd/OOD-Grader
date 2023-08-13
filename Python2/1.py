class translator:

    def deciToRoman(self, num):
        ans = "" 
        roman = {
            1000 : "M",    
            900 : "CM",    
            500 : "D",
            400 : "CD",
            100 : "C",
            90 : "XC",
            50 : "L",
            40 : "XL",
            10 : "X",
            9 : "IX",
            5 : "V",
            4 : "IV",
            1 : "I"
        }
        while num != 0:
            if num >= 1000:
                ans += roman[1000]
                num -= 1000
            elif num >= 900:
                ans += roman[900]
                num -= 900
            elif num >= 500:
                ans += roman[500]
                num -= 500
            elif num >= 400:
                ans += roman[400]
                num -= 400
            elif num >= 100:
                ans += roman[100]
                num -= 100
            elif num >= 90:
                ans += roman[90]
                num -= 90
            elif num >= 50:
                ans += roman[50]
                num -= 50
            elif num >= 40:
                ans += roman[40]
                num -= 40
            elif num >= 10:
                ans += roman[10]
                num -= 10
            elif num >= 9:
                ans += roman[9]
                num -= 9
            elif num >= 5:
                ans += roman[5]
                num -= 5
            elif num >= 4:
                ans += roman[4]
                num -= 4
            elif num >= 1:
                ans += roman[1]
                num -= 1
        return ans

        ### Enter Your Code Here ###

    def romanToDeci(self, s):   
        ans = 0
        i = 0
        while(1):
            if i >= len(s):
                break
                
            if s[i] == 'M': ans += 1000
            elif s[i] == 'D' : ans += 500
            elif s[i] == 'C' :
                if i + 1 < len(s) and s[i + 1] == 'M' :
                    ans += 900
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == 'D':
                    ans += 400
                    i += 1
                else:
                    ans += 100
            elif s[i] == 'L':
                ans += 50
            elif s[i] == 'X':
                if i + 1 < len(s) and s[i + 1] == 'C':
                    ans += 90
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == 'L':
                    ans += 40
                    i += 1
                else:
                    ans += 10
            elif s[i] == 'V':
                ans += 5
            elif s[i] == 'I':
                if i + 1 < len(s) and s[i + 1] == 'X':
                    ans += 9
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == 'V':
                    ans += 4
                    i += 1
                else:
                    ans += 1
            i += 1
        return ans


num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))