# Python üzerinde hata yönetimi Try - Except ile sağlanır.

# Try bloğu içerisine hata riski yüksek olan bölümler eklenir.

# Herhangi bir hata yaşandığında Except bloğu ile hata yönetimi gerçekleştirilir.

try:
    print("Bilge Adam Akademi")
except :
    print("Bu bir hata mesajidir!")

    # Bazı Hata tipleri (Exceptions - istisnalar)
    # IOError => Eğer bir dosya açılamazsa bu exception(isnista çalışacaktır)
    # ImportError => Python modülü bulunamaması durumu
    # ValueError => Tip-Değer uyuşmazlığı hatası
    # EOFError => End Of file Hatası => input() gibi fonksiyonlarda dosyanın sonuna bir değer okuyamadan atlanması durumu.

# Örnek =>

try:
    dosya = open("testYazi","r")
    dosya.write("Bu dosya hata kontrolu icin acilmıstir.")
except IOError:
    print("Dosya bulunamadı!")
    dosya.close()

# Finally bloğu => Try sırasında bir hata alınsa da alınmasa da çalışan bloktur.
# Kullanımı zorunlu değildir.

 # Üstteki örneği finally ile genişletirsek

try:
    dosya = open("testYazi", "r")
    try:
        dosya.write("Bu dosya hata kontrolu icin acilmıstir.")
    finally:
        print("Dosya ile ilgili hata varsa da yoksa da dosyayı kapatıyorum")
        dosya.close()
except IOError:
    print("Dosya bulunamadı!")

try:
    deger = int(input("Lütfen Bir Sayı Giriniz: ")) # Sayı olmayan bir değer alınmalıdır.
    deger %=2
# except IOError: bu şekilde yanlış exception tipi belirtirsek program kapanacaktır çünkü hata tipimiz ValueError olmalıdır.
except ValueError :# Eğer hata tipi doğru belirtilmezse proje kapanacaktır. Ancak ValueError sayesinde bunu engelleyebiliyoruz.
    print("Veri tipi hatası var!")

# Breakpoint ve Debugging
# Mantıksal Hatalar Exception ile çözülemeyebilirler. Yazılımcı kaynaklı hatalar için Debug yöntemi ile adım adım kodlarımızın çalıştırılmasını takip edebiliriz.
# Hata alma ihtimaliniz olan kod bloğunun sol tarafındaki sütuna tıklayarak kırmızı top şeklinde olan breakpointlerden koyuyoruz.
# Daha sonrasında ise programı debug modunda çalıştırıyoruz. (Shift+F9) kısayolu ile çalıştırabilirsiniz.
# Program breakpoint koydugunuz noktaya gelince duracak ve size adım adım kodunuzu takip etme ve içlerindeki değerleri görme şansı verecektir.
# F8 tuşuna basarak adım adım kodunuzda ilerleyebilirsiniz.

# Breakpoint ile ilerlerken üzerinde durduğu satır daha çalıştırılmamış kod bloğudur.
# Bir değer ile ilgili anlık bir değer ataması gerçekleştirmek ve sonucuna bakmak isterseniz sol alt köşedeki debugger ekranından değişkenimize tıklayarak evaluate expression seçebilir ve açılan ekranda üstteki satırda istediğimiz işlemi deneyebiliriz.
# New Watch özelliği ile herhangi bir değeri ayrıca takip ekranımıza ekleyebiliriz.
# Bunun için debugger ekranında sağ tuş tıklayarak New Watch işaretlememiz ve takip etmek istediğimiz değerin ismini bulmamız gerekmektedir.


# input olarak sayı girerek breakpoint denemesi yapabiliriz.


sayi = int(input("Lütfen bir sayı giriniz : "))

yeniSayi = sayi + 30 # Watch Ekranında yeniSayi takibi yapabiliriz.

print(sayi,yeniSayi)