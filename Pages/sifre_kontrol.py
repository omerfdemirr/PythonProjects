def sifre_gecerli_mi(sifre):
    """Şifrenin belirlenen kurallara uyup uymadığını kontrol eder."""
    if len(sifre) < 8:
        return False

    buyuk_harf_var_mi = any(karakter.isupper() for karakter in sifre)
    kucuk_harf_var_mi = any(karakter.islower() for karakter in sifre)
    rakam_var_mi = any(karakter.isdigit() for karakter in sifre)
    sembol_var_mi = any(karakter in "!@#$%^&*()_-+=<>?/|{}[]~" for karakter in sifre)

    return all([buyuk_harf_var_mi, kucuk_harf_var_mi, rakam_var_mi, sembol_var_mi])

while True:
    sifre = input("Şifre girin: ")

    if sifre_gecerli_mi(sifre):
        print("Şifre başarılı!")
        break
    else:
        print("Şifre kurallara uymuyor, tekrar deneyin.")
        print("- En az 8 karakter olmalı")
        print("- En az 1 büyük harf")
        print("- En az 1 küçük harf")
        print("- En az 1 rakam")
        print("- En az 1 sembol (!@# vs.)\n")