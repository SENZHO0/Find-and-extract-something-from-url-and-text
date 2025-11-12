url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

# pisah
parts = url.split("/")

for i in range(len(parts)):
    if parts[i].isdigit() and len(parts[i]) == 4:  # patokan dari tahun
        year = parts[i]
        month = parts[i + 1]
        day = parts[i + 2]
        break

print(f"Extracted date: \nYear : {year}\nMonth: {month}\nDay  : {day}")