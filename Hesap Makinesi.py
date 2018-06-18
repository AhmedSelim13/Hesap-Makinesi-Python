islem = input("Yapmak istediginiz islemi yaziniz: [toplama] [cikarma] [bolme] [carpma] [taban degistirme] ")
if islem == "toplama" :
	x = float(input("Toplamak istediginiz 1. sayiyi giriniz: "))
	y = float(input("Toplamak istediginiz 2. sayiyi giriniz: "))
	print(x + y)
elif islem == "cikarma" :
	x = float(input("Eksilmesini istediginiz sayiyi giriniz: "))
	y = float(input("Eksiltmek istediginiz miktari giriniz: "))
	print(x - y)
elif islem == "bolme" :
	x = float(input("Bölmek istediginiz sayiyi giriniz: "))
	y = float(input("Kaça bölmek istediginizi giriniz: "))
	print(x / y)
elif islem == "carpma" :
	x = float(input("Çarpmak istediginiz 1. sayiyi giriniz: "))
	y = float(input("Çarpmak istediginiz 2. sayiyi giriniz: "))
	print(x * y)
elif islem == "taban degistirme" :
	x = input("Sayinin ilk halinin tabanini giriniz: ")
	y = input("Sayiyi cevirmek istediginiz tabani giriniz: ")
	sayi = input(x + " tabanindan " + y + " tabanina cevirmek istediginiz sayiyi giriniz: ")
	if x == 10 :
		sayi = int(sayi)
		print(sayi)
		ikli = []
		g = x + " tabanindaki degeri: "
		x = int(x)
		while sayi >= 1 :
			kalan = sayi % y
			kalan = int(kalan)
			sayi = sayi / y
			sayi = int(sayi)
			kalan = str(kalan)
			ikli.append(kalan)
		ikli.reverse()
		hane = len(ikli)
		i = 0
		while hane > i :
			g = g + str(ikli[i])
			i = i + 1
		print(g)
	elif y == 10 :
		x = int(x)
		s = 0
		v = 0
		d = len(sayi) - 1
		while d >= 0:
			c = int(sayi[v])
			s = (c * (x ** d)) + s
			d = d - 1
			v = v + 1
		print(s)
	else :
		x = int(x)
		s = 0
		v = 0
		d = len(sayi) - 1
		while d >= 0:
			c = int(sayi[v])
			s = (c * (x ** d)) + s
			d = d - 1
			v = v + 1
		s = int(s)
		ikli = []
		g = y + " tabanindaki degeri: "
		y = int(y)
		while s >= 1 :
			kalan = s % y
			kalan = int(kalan)
			s = s / y
			s = int(s)
			kalan = str(kalan)
			ikli.append(kalan)
		ikli.reverse()
		hane = len(ikli)
		i = 0
		while hane > i :
			g = g + str(ikli[i])
			i = i + 1
		print(g)
else :
	print("Gecersiz islem girdiniz. Lütfen tekrar deneyiniz.")
