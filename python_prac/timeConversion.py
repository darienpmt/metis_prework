def timeConversion(s):
    am_pm = s[-2:]
    hr = int(s[:2])

    if am_pm == 'PM':
        if hr != 12:
            return str(hr + 12) + s[2:-2]
        else:
            return str(hr) + s[2:-2]
    else:
        if hr != 12:
            return s[:-2]
        else:
            return '00' + s[2:-2]


    

    

    


print(timeConversion('12:59:00PM'))