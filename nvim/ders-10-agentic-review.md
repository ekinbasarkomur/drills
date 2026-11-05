# Ders 10 — Ajanla çalışmak: bağlam ver, değişikliği incele

Kodun çoğunu Claude yazıyorsa editörün işi **yazmak değil okumak**. Bu ders iki
yönlü: Claude'a "şuraya bak" demek, Claude'un yaptığını katman katman görmek.

## 1. Claude'a yer göstermek — `<leader>y`

| Tuş | Panoya ne koyar | Örnek |
| --- | --- | --- |
| `<leader>yf` | göreli yol + satır | `leetcode/pandas_track/lc0184_….py#L16` |
| `<leader>yp` | mutlak yol + satır | `/Users/…/lc0184_….py#L16` |
| `<leader>yc` (visual) | seçim, dosya adı ve satır numarasıyla kod bloğu | aşağıda |

`yc` çıktısı:

````
```python filename="leetcode/pandas_track/lc0184_department_highest_salary.py" line=16
def department_highest_salary(employee, department):
```
````

Claude bunu alınca hangi dosya, hangi satır olduğunu bilir; "bu ne" diye
sormana gerek kalmaz.

Üç yol, hangisi ne zaman:

| İhtiyaç | Yol |
| --- | --- |
| "Şu satıra bak" | `<leader>yf`, Claude'a yapıştır |
| "Bu bloğu açıkla / düzelt" | `V` ile seç, `<leader>yc`, yapıştır |
| Claude editörde açıksa | `V` ile seç, `<leader>as` — pano yok, doğrudan gider |

### Pratik 1

Bu dosyada `<leader>yf` bas; bildirimde yolu gör. Claude terminalini aç
(`<leader>aa`), `<C-r>+` ile yapıştır (terminal insert modundayken `<C-r>+`
panoyu yapıştırır), "bu dosyada kaç başlık var?" diye sor. `<C-h>` ile dön.

## 2. Claude'un yaptığını görmek — dört katman

Yukarıdan aşağı, kaba taneden ince taneye:

| Katman | Tuş | Ne görürsün | Ne zaman |
| --- | --- | --- | --- |
| 0 | `<leader>gg` | **lazygit**: hangi dosyalar değişmiş, commit, push | her zaman önce bu |
| 1 | `<leader>gv` | **codediff**: her dosya yan yana eski/yeni, solda ağaç | 3+ dosya değiştiyse |
| 2 | `<leader>go` | **overlay**: eski satırlar yeni satırların üstüne çizilir; `]c` ile gez | tek dosyada "tam ne oldu" |
| 3 | `<leader>ghp` | **hunk**: tek bir değişikliğin eski hâli | karar anı: `ghs` tut / `ghr` at |

### lazygit içinde

| Tuş | Ne yapar |
| --- | --- |
| `j` / `k` | gez |
| `Tab` / `[` `]` | paneller arası (dosyalar, dallar, commit'ler) |
| `Enter` (dosyada) | hunk hunk aç |
| `Space` | stage / unstage |
| `a` | hepsini stage et |
| `d` | değişikliği at (sorar) |
| `c` | commit (mesaj yaz, `Enter`) |
| `P` | push |
| `e` | dosyayı editörde aç |
| `?` | bütün tuşlar |
| `q` | kapat |

### Pratik 2 — uçtan uca

1. Claude'a şunu söyle: "`nvim/ders-01-yank-delete-paste.md` ve
   `nvim/ders-02-surround.md` dosyalarının en sonuna `<!-- reviewed -->`
   satırı ekle."
2. `<leader>gg` — iki dosya değişmiş. `q`.
3. `<leader>gv` — ikisi yan yana, solda ağaç. Ağaçta `j`/`k`, `Enter`. `q`.
4. `<leader>ff` ile ders-01'i aç, `<leader>go` — eklenen satır overlay'de.
   `]c` ile oraya git. `<leader>go` ile kapat.
5. `<leader>ghp` — hunk'ı gör. Bunu istemiyorsun: `<leader>ghr` — gitti.
6. `<leader>gg`, ders-02'de `Space` ile stage, `c`, mesaj `test`, `Enter`.
   `q`.
7. Geri al: terminalde `git reset --soft HEAD~1` sonra `git checkout -- nvim/`.
   Ya da Claude'a "son commit'i geri al ve değişiklikleri at" de.

## 3. Buffer temizliği

Claude 20 dosyaya dokunduysa `Tab` ile gezmek işkence olur:

| Tuş | Ne yapar |
| --- | --- |
| `<leader>bD` | görünmeyen bütün buffer'ları kapat, kaydedilmemişlere dokunmaz |
| `<leader>fb` | kalan buffer'lar |

## 4. İş bölümü — kim neyi yapar

| İş | Araç |
| --- | --- |
| Problemi tarif et, dosya/satır göster | `<leader>yf` `yc` `as` |
| Kodu yazdır | Claude |
| Ne değiştiğini gör | `gg` → `gv` → `go` → `ghp` |
| Küçük düzeltme | kendin, Ders 1–4 |
| Beğenmediğini at | `ghr` |
| Commit | `gg` içinde `c`, ya da Claude'a söyle |

Drill'lerde tersine: kodu **sen** yazarsın, Claude'a sadece "nerede hata var"
diye sorarsın — `<leader>yc` ile ilgili bloğu gönderip.

## Özet

```
<leader>yf  yc  as     Claude'a yer göster
<leader>gg             lazygit — önce buraya bak
<leader>gv  go  ghp    dosyalar → satırlar → hunk
<leader>ghs ghr        tut / at
<leader>bD             buffer'ları süpür
```

Bu, 10 dersin sonu. README'deki tabloyu doldur; hangileri oturmadıysa o dersi
bir hafta sonra tekrar aç.
