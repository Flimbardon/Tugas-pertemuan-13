satuan = ['', ' One', ' Two', ' Three', ' Four',' Five', ' Six', ' Seven', ' Eight', ' Nine']

def terbilang(n):
    if n < 10 :
        return satuan[n]
    elif n >= 1000000000:
        return terbilang(n // 1000000000) + ' Billion' + terbilang(n % 1000000000)
    elif n >= 1000000:
        return terbilang(n // 1000000) + ' Million' + terbilang(n % 1000000) 
    elif n >= 1000:
        return terbilang (n//1000) + " Thousand" + terbilang(n%1000)
    elif n >= 100 :
        return terbilang (n//100) + " hundred" + terbilang(n%100) 
    elif n >= 20:
        if n // 10 == 2:
            return " Twenty" + terbilang(n%10)
        elif n // 10 == 3:
            return " Thirty" + terbilang(n%10)
        elif n // 10 == 5:
            return " Fifty" + terbilang(n%10)
        elif n // 10 == 8:
            return " Eighty" + terbilang(n%10)
        else :
            return terbilang(n // 10) + 'ty' + terbilang(n%10) 
    else:
        if n == 10:
            return ' Ten'
        elif n == 11:
            return ' Eleven'
        elif n == 12:
            return ' Twelve'
        elif n == 18:
            return ' Eighteen'
        else:
            return terbilang(n % 10) + 'teen'
            
            
        

#test

n = 9800000000
print(f'{n} = {terbilang(n)}')