# Ders 3 — Arama ve değiştirme

Dört ölçek var; her birinin kendi aracı:

| Ölçek | Araç | Tuş |
| --- | --- | --- |
| Bu dosyada **bul** | `/` | `/kelime` |
| Bu dosyada **değiştir** | `:s` | `<leader>sr` |
| Projede **bul** | Telescope | `<leader>fg` / `<leader>sw` |
| Projede **değiştir** | grug-far | `<leader>sp` |

## 1. Dosyada bul

| Tuş | Ne yapar |
| --- | --- |
| `/foo` + `Enter` | ileriye doğru ara; yazarken eşleşmeler sarı yanar |
| `?foo` | geriye doğru |
| `n` / `N` | sonraki / önceki (ekranın ortasına gelir — bizim ekledik) |
| `*` / `#` | **imleçteki kelimeyi** ara, ileri / geri — yazmana gerek yok |
| `<leader>/` | sarıları temizle |
| `<leader>sf` | dosyada bulanık arama, Telescope listesiyle |

Arama **küçük/büyük harf duyarsız**, ama büyük harf yazarsan duyarlı olur
(`smartcase`): `/foo` → `Foo`'yu da bulur, `/Foo` → sadece `Foo`.

### Pratik 1a

`count` kelimesinin kaç kez geçtiğini bul, hepsini `n` ile gez.

```python
count = 0
for item in items:
    if item.count > 0:
        count += item.count
print(count)
```

Nasıl: ilk `count`'a git, `*`. Sağ altta `[1/4]` yazar. `n` `n` `n`.
`<leader>/` ile sarıyı kapat.

### Pratik 1b

`.` karakteri regex'te "herhangi bir karakter"dir. Gerçek noktayı aramak için
`\.` yazarsın. Aşağıda `item.count`'u ara: `/item\.count`.

```python
item.count
itemXcount
```

İkincisi eşleşmemeli.

## 2. Dosyada değiştir — `:s`

Komut `:s/eski/yeni/`. Başına aralık, sonuna bayrak gelir:

| Komut | Ne yapar |
| --- | --- |
| `:s/a/b/` | bu satırda, ilk `a` |
| `:s/a/b/g` | bu satırda, **hepsi** (**g**lobal) |
| `:%s/a/b/g` | **bütün dosyada** (`%` = her satır) |
| `:%s/a/b/gc` | her birinde sor (**c**onfirm): `y` evet, `n` hayır, `a` kalan hepsi, `q` çık |
| `:'<,'>s/a/b/g` | seçili satırlarda — visual'da `:` basınca `'<,'>` kendi gelir |

Hepsini hatırlamana gerek yok:

| Tuş | Ne yapar |
| --- | --- |
| `<leader>sr` | imleçteki kelime için `:%s/\<kelime\>//gI` hazır gelir; sen yeniyi yaz, `Enter` |
| `<leader>sr` (visual) | seçili metin için aynısı |

`\<` ve `\>` kelime sınırı — `count`'u değiştirirken `counter`'a dokunmaz.
`I` büyük/küçük harfe duyarlı yapar.

### Pratik 2a

Bütün `foo`'ları `bar` yap.

```python
foo = 1
foobar = foo + 1
print(foo, foobar)
```

Nasıl: bir `foo`'ya git, `<leader>sr`, `bar`, `Enter`. `foobar` değişmedi —
kelime sınırı sayesinde. Hedef: `bar = 1`, `foobar = bar + 1`, `print(bar, foobar)`.

### Pratik 2b

Sadece 2. ve 3. satırdaki `x`'leri `y` yap, 1. satır kalsın.

```
x x x
x x x
x x x
```

Nasıl: 2. satıra git, `V`, `j`, `:` — komut satırında `:'<,'>` belirir —
`s/x/y/g`, `Enter`.

### Pratik 2c

Tek tek onaylayarak: `old`'ları `new` yap ama 2. satırdakini atla.

```
old one
old two
old three
```

Nasıl: `:%s/old/new/gc` + `Enter`. `y`, `n`, `y`.

## 3. Projede bul

| Tuş | Ne yapar |
| --- | --- |
| `<leader>fg` | **live grep** — yazdıkça bütün projede arar |
| `<leader>sw` | imleçteki kelimeyi projede ara |

Sonuç listesinde: `<C-j>` / `<C-k>` ile gez, `Enter` ile aç, `Esc` ile kapat.
`<C-q>` hepsini **quickfix** listesine atar (bkz. Ders 7).

### Pratik 3a

`drills` projesinde `transform("max")` geçen dosyaları bul.

Nasıl: `<leader>fg`, `transform` yaz. Listede birini `Enter` ile aç. `<C-o>`
ile geri dön (jumplist, Ders 4).

### Pratik 3b

Bu dosyadaki `grug` kelimesine git, `<leader>sw`. Hangi dosyalarda geçiyor?

## 4. Projede değiştir — grug-far

`<leader>sp` sağda bir panel açar:

```
Search:   (ne arıyorsun)
Replace:  (ne olacak; boş bırakırsan sadece arar)
Filter:   (hangi dosyalar; örn. *.py)
----
sonuçlar, dosya dosya, bağlamıyla
```

| Tuş | Ne yapar |
| --- | --- |
| `Tab` | sonraki alana geç |
| `Enter` (sonuçta) | o satıra git |
| `<leader>r` | **hepsini değiştir** |
| `<leader>q` | sonuçları quickfix'e at |
| `<leader>c` | paneli kapat |
| `g?` | bütün tuşlar |

Değiştirmeden önce sonuçlara bakıp istemediğin satırları **`dd` ile listeden
silebilirsin**; sadece kalanlar değişir. Visual'da `<leader>sp` seçili metni
arama alanına koyar.

### Pratik 4a

Bu klasördeki (`nvim/`) tüm derslerde `Hedef:` kelimesini ara. Replace'i boş
bırak, sadece bak. Kaç dosyada geçiyor?

Nasıl: `<leader>sp`, `Hedef:` yaz, `Tab` `Tab` ile Filter'a geç, `nvim/*.md`
yaz. `<leader>c` ile kapat.

### Pratik 4b — gerçek değişiklik, geri alınabilir

`drills` projesinde `python_files = ["lc*.py"]` satırını bul (tek dosyada,
`pyproject.toml`). grug-far ile `lc*` → `lc*` yap (yani hiçbir şey değiştirme
ama akışı gör): Search `lc\*`, Replace `lc*`, `<leader>r`. Sonra
`git diff` ile hiçbir şey değişmediğini doğrula.

## Özet

```
/  *  n  N  <leader>/          dosyada bul
<leader>sr   :%s/a/b/gc        dosyada değiştir
<leader>fg   <leader>sw        projede bul
<leader>sp                     projede değiştir
```

Oturdu mu? README'ye ✓, Ders 4: hareket.
