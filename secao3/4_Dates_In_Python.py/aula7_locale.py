# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps

import calendar
import locale

# ELE muda para o locale do PC. (idioma)
# locale.setlocale(locale.LC_ALL, 'pt_BR')
locale.setlocale(locale.LC_ALL, 'bulgarian')
# locale.setlocale(locale.LC_ALL, '')  # sem nada é o idioma da maquina


print(calendar.calendar(2024))
print(locale.getlocale())  # mostra o codigo q vc "usou/+padrao" do win
# ('pt_BR', 'cp1252')


local = locale.locale_alias  # mostra todas as locales.

for key in local:
    print(key)
