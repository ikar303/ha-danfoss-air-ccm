# Danfoss Air CCM - Parameters

## ✅ Potwierdzone

| Adres | Nazwa | Typ | Odczyt | Zapis | Status | Uwagi |
|------:|-------|-----|:------:|:-----:|--------|-------|
| 1008 | Alarm Code | WORD | ✅ | ❌ | OK | Kod alarmu |
| 5160 | Supply Step | BYTE | ✅ | ? | OK | Krok nawiewu 1-100 |
| 5161 | Extract Step | BYTE | ✅ | ? | OK | Krok wywiewu 1-100 |
| 5184 | Basic Supply Step | BYTE | ✅ | ✅ | OK | Bazowy krok nawiewu |
| 5185 | Basic Extract Step | BYTE | ✅ | ✅ | OK | Bazowy krok wywiewu |
| 5216 | Bypass | BYTE | ? | ? | Do sprawdzenia | Sterowanie |
| 5223 | Bypass Active | BOOL | ? | ❌ | Do sprawdzenia | Stan bypassu |
| 5226 | Filter Fouling | PERCENT | ? | ❌ | Do sprawdzenia | Zużycie filtra |
| 5231 | Filter Reset | BOOL | ? | ✅ | Do sprawdzenia | Reset filtra |
| 5232 | Relative Humidity | PERCENT | ✅ | ❌ | OK | Wilgotność |
| 5234 | Outdoor Temperature | TEMP | ✅ | ❌ | OK | T1 |
| 5235 | Supply Temperature | TEMP | ✅ | ❌ | OK | T2 |
| 5236 | Extract Temperature | TEMP | ✅ | ❌ | OK | T3 |
| 5237 | Exhaust Temperature | TEMP | ✅ | ❌ | OK | T4 |
| 5424 | Boost | BOOL | ? | ? | Do sprawdzenia | Boost |
| 5891 | Maximum Boost Step | BYTE | ? | ? | Do sprawdzenia | Maksymalny krok boost |
| 6016 | FanStep SP | BYTE | ? | ✅ | Do sprawdzenia | Zadany krok |
| 6017 | FanStep | BYTE | ✅ | ❌ | OK | Aktualny krok 1-10 |
| 6019 | Resultant FanStep | BYTE | ? | ❌ | Do sprawdzenia | Wynikowy krok |

---

## ❌ Błędne tropy

| Adres | Opis | Powód |
|------:|------|-------|
| 5200 | Actual Supply Fan Speed | Nie używać | Zwraca 0 |
| 5201 | Actual Exhaust Fan Speed | Nie używać | Zwraca 0 |

---

## TODO

- [ ] Bypass
- [ ] Bypass Active
- [ ] Filter Fouling
- [ ] Filter Reset
- [ ] Alarm Code
- [ ] Boost
- [ ] Harmonogram tygodniowy
- [ ] Profile