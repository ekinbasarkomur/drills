# Ders 8 — LSP: kodu anlayan editör

LSP (pyright, clangd, rust-analyzer) kodu **anlar**: hangi değişken nerede
tanımlı, bir fonksiyonu kim çağırıyor, bu satırda ne hata var. Tuşların çoğu
`g` ile başlar (**g**o).

## 1. Gitmek

| Tuş | Ne yapar |
| --- | --- |
| `gd` | tanıma git (**d**efinition) — fonksiyon nerede yazılmış |
| `gD` | bildirime git (C++'ta header) |
| `gr` | **r**eferanslar — bunu kim kullanıyor, liste |
| `gi` | **i**mplementation (trait/interface için) |
| `gy` | tipin tanımına git (t**y**pe) |
| `<C-o>` | geri dön (Ders 4) |

`gd` başka dosyaya götürebilir; `<C-o>` her zaman geri getirir.

### Pratik 1

`leetcode/pandas_track/lc0184_department_highest_salary.py`'yi aç. `check`
kelimesine git, `gd` → `_pd.py`'ye atlar. `<C-o>` ile dön. `frame`'e git,
`gr` → bu fonksiyonu çağıran her yer listede. `Esc`.

## 2. Anlamak

| Tuş | Ne yapar |
| --- | --- |
| `K` | imleçtekinin dokümanı (hover) — tip, imza, docstring |
| `<C-s>` (insert modda) | parantez içindeyken argümanları göster |
| `K` (C/C++'ta) | cppman — standart kütüphane man sayfası |

### Pratik 2

`.merge(`'in üstünde `K` — pandas'ın merge imzası. Pencereyi `K` bir daha
basarak içine gir, `q` ile kapat. Insert moda gir, `df.merge(` yaz, `<C-s>` —
argüman listesi. `Esc`, `u`.

## 3. Hatalar (diagnostics)

Kenardaki kırmızı/sarı işaretler ve altı çizili yerler.

| Tuş | Ne yapar |
| --- | --- |
| `]d` / `[d` | sonraki / önceki hata |
| `<leader>xl` | imleçteki hatanın tam metnini pencerede göster |
| `<leader>xx` | bu dosyadaki bütün hatalar, liste |
| `<leader>xX` | projedeki bütün hatalar |

### Pratik 3

Bir pandas dosyasında kasten hata yap: bir satıra `foo = bar` yaz. Kırmızı
işaret belirir. `]d` ile oraya git, `<leader>xl` ile oku: "bar is not
defined". `u`.

## 4. Değiştirmek

| Tuş | Ne yapar |
| --- | --- |
| `<leader>cr` | **yeniden adlandır** — bütün projede, her kullanımı |
| `<leader>ca` | **code action** — LSP'nin önerdiği düzeltmeler (import ekle, …) |
| `<leader>cf` | şimdi formatla (kaydederken zaten otomatik) |

`<leader>cr` ile `:%s` farkı: `cr` string içindeki ya da yorumdaki aynı
kelimeye dokunmaz, sadece gerçek referansları değiştirir.

### Pratik 4

Bir Python dosyasında yerel bir değişkenin üstünde `<leader>cr`, yeni ad yaz,
`Enter`. Her kullanım değişti. `u` ile geri al (tek `u` yeter).

## 5. Tamamlama (cmp)

Yazarken menü açılır:

| Tuş | Ne yapar |
| --- | --- |
| `<C-j>` / `<C-k>` ya da `Tab` / `S-Tab` | gez |
| `Enter` | seçili olanı kabul et |
| `<C-e>` | menüyü kapat |
| `<C-Space>` | menüyü zorla aç |
| `<C-l>` | supermaven'ın gri önerisini **tamamen** kabul et |
| `<M-l>` | gri öneriden **bir kelime** al |

Menü yokken `Enter` normal satır sonu — menü varken dikkat, seçili olanı
yapıştırır. İstemiyorsan önce `<C-e>`.

## Özet

```
gd  gr  K  <C-o>        git, kim kullanıyor, nedir, dön
]d  <leader>xl  xx      hatalar
<leader>cr  ca  cf      adlandır, düzelt, formatla
```

Oturdu mu? README'ye ✓, Ders 9: git.
