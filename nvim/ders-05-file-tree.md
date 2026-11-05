# Ders 5 — Dosya ağacı (nvim-tree)

`<leader>e` ağacı açar/kapatır. Ağaç normal bir pencere: `j`/`k` ile gezersin,
`<C-l>` ile editöre dönersin, `<C-h>` ile ağaca geçersin. Ağaçta `g?` bütün
tuşları listeler.

Ağaçtayken tuşlar **farklı anlama gelir** — `x` burada kes, `H` gizli dosyaları
göster. Editördeki anlamları ağaçtan çıkınca geri gelir.

## 1. Gezinme ve açma

| Tuş | Ne yapar |
| --- | --- |
| `j` / `k` | aşağı / yukarı |
| `Enter` / `o` | dosyayı aç, klasörü aç/kapat |
| `Tab` | **önizle** — dosyayı açar ama imleç ağaçta kalır |
| `<C-v>` | dikey split'te aç |
| `<C-x>` | yatay split'te aç |
| `<C-t>` | yeni tab'da aç |
| `P` | üst klasöre (**P**arent) |
| `<BS>` | klasörü kapat |
| `E` / `W` | hepsini aç / kapat (**E**xpand, collapse… `W`) |
| `-` | kökü bir üst klasöre taşı |
| `<C-]>` | kökü imleçteki klasöre taşı |
| `q` | ağacı kapat |

### Pratik 1

`<leader>e`, `leetcode/` klasörünü `Enter` ile aç, `pandas_track/`'e in,
`Enter`. `lc0184_…`'e git, `Tab` ile önizle — dosya sağda açıldı, imleç
ağaçta. `j` ile bir alttakine `Tab` — önizleme değişti. `Enter` ile birine
gerçekten gir, `<C-h>` ile ağaca dön, `W` ile her şeyi kapat.

## 2. Oluştur, adlandır, sil

| Tuş | Ne yapar |
| --- | --- |
| `a` | yeni dosya/klasör (**a**dd); sonu `/` ile biterse klasör |
| `r` | yeniden adlandır (**r**ename) — tam ad |
| `e` | yeniden adlandır — sadece ad, uzantı sabit |
| `d` | sil, sorar (**d**elete) |
| `D` | çöpe at |
| `R` | ağacı yenile (**R**efresh) |

`a` ile klasör içinde dosya açmak için imleç o **klasörün** üstünde olmalı;
bir dosyanın üstündeysen o dosyanın yanına açar.

### Pratik 2

`nvim/` klasörünün üstüne git, `a`, `deneme.md` yaz, `Enter`. Dosya oluştu
ve açıldı. Ağaca dön, `r` ile `deneme2.md` yap. `d` ile sil, `y` ile onayla.

## 3. Kopyala, kes, yapıştır

| Tuş | Ne yapar |
| --- | --- |
| `c` | dosyayı kopyala (**c**opy) |
| `x` | dosyayı kes |
| `p` | yapıştır — imleç hangi klasördeyse oraya |
| `y` | dosya **adını** panoya |
| `Y` | göreli **yolunu** panoya |
| `gy` | mutlak yolunu panoya |

Taşıma = `x` + hedef klasöre git + `p`. İsim çakışırsa sorar.

### Pratik 3

`nvim/ders-00-claude.md`'nin üstünde `Y` bas, editöre geç, insert modda
`<C-r>+` ile yapıştır: `nvim/ders-00-claude.md` yazar. Claude'a "şu dosyaya
bak" derken yolu böyle alırsın. `u` ile geri al.

## 4. Açık dosyayı ağaçta bulma

Büyük projede "bu dosya nerede?" sorusu:

`<leader>E` — ağacı açar ve imleci editördeki dosyanın üstüne getirir
(`<leader>e` aç/kapat, büyük `E` "beni bul").

## 5. Filtre ve gizli dosyalar

| Tuş | Ne yapar |
| --- | --- |
| `H` | dotfile'ları göster/gizle (`.gitignore`, `.venv`…) |
| `I` | `.gitignore`'daki dosyaları göster/gizle |
| `f` | canlı filtre — yazdıkça ağaç daralır |
| `F` | filtreyi temizle |
| `S` | dosya adı ara (`/` ile aynı iş) |

### Pratik 5

`f`, `lc01` yaz — sadece 01xx dosyaları kaldı. `F` ile temizle.

## 6. Toplu iş — işaretle

| Tuş | Ne yapar |
| --- | --- |
| `m` | dosyayı işaretle / işareti kaldır (**m**ark) |
| `bd` | işaretlileri sil |
| `bmv` | işaretlileri taşı (hedef klasör sorar) |
| `bt` | işaretlileri çöpe at |

### Pratik 6

Üç dosyayı `m` ile işaretle, `bmv`, iptal et (`Esc`). İşaretleri `m` ile kaldır.

## Özet

```
<leader>e  E   aç/kapat, beni bul   <C-h> / <C-l>   ağaç ↔ editör
Enter  Tab     aç / önizle      a r d           oluştur, adlandır, sil
c x p          kopyala kes yapıştır
Y              yolu panoya      f F             filtre
g?             hepsi
```

Oturdu mu? README'ye ✓, Ders 6: pencereler ve buffer'lar.
