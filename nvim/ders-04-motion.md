# Ders 4 — Hareket

Ok tuşların çalışıyor ve çalışmaya devam edecek. Bu ders "daha hızlı gitmek"
için değil, **"komut + ne kadar"** kalıbının sağ tarafını büyütmek için:
burada öğrendiğin her hareket `d`, `y`, `c`, `v` ile de çalışır.

## 1. Kelime

| Tuş | Ne yapar |
| --- | --- |
| `w` | sonraki kelimenin **başı** |
| `b` | önceki kelimenin başı (**b**ack) |
| `e` | bu kelimenin **sonu** (**e**nd) |
| `W` `B` `E` | aynısı ama noktalama kelimeyi bölmez: `foo.bar` tek kelime |
| `3w` | üç kelime |

### Pratik 1

`self.items.append(x)` satırında `self`'ten başla: `w` ile kaç basışta `x`'e
varırsın? `W` ile kaç basışta?

```python
self.items.append(x)
```

(`w`: 7, `W`: 1 — çünkü `W` için boşluğa kadar her şey tek kelime.)

## 2. Satır içinde

| Tuş | Ne yapar |
| --- | --- |
| `H` / `L` | satır başı / sonu (bizim ekledik; orijinalleri `^` / `$`) |
| `0` | gerçek ilk sütun, girinti dahil |
| `f` + karakter | satırda o karakteri **ileriye** bul (**f**ind) |
| `F` + karakter | geriye |
| `t` + karakter | karakterin **bir öncesine** kadar (**t**ill) |
| `;` / `,` | son `f`/`t`'yi tekrarla ileri / geri |

`f` ve `t`'nin farkı `d` ile anlaşılır: `df,` virgül **dahil** siler, `dt,`
virgüle **kadar** siler.

### Pratik 2a

İmleci satır başına koy, `f(` ile paranteze, `;` ile sonrakine git.

```python
result = compute(a, b) + other(c)
```

### Pratik 2b

`a, b` argümanlarını sil, parantezler kalsın. Hedef: `compute()`.

```python
compute(a, b)
```

Nasıl: `f(`, `l` (bir sağ), `dt)` — kapatana kadar sil. (Ders 1'deki `di(`
aynı işi yapar ve imleç nerede olursa olsun çalışır — genelde o daha iyi.)

## 3. Satırlar arası

| Tuş | Ne yapar |
| --- | --- |
| `gg` / `G` | dosya başı / sonu |
| `:42` + `Enter` | 42. satır |
| `42G` | aynı |
| `7j` / `7k` | 7 satır aşağı / yukarı |
| `{` / `}` | önceki / sonraki **boş satır** (paragraf) |
| `%` | eşleşen parantez — `(` `[` `{` üstündeyken karşısına |
| `<C-d>` / `<C-u>` | yarım sayfa aşağı / yukarı |
| `zz` | imleç satırını ekranın ortasına getir |

Sol kenardaki sayılar **relative**: imlecin satırı gerçek numara, diğerleri
uzaklık. "5 satır aşağıdaki satıra gitmek" = sol kenarda 5 yazan satır → `5j`.
Silmek için `5dd` ya da `d5j`.

### Pratik 3a

Aşağıdaki fonksiyonun sonundaki `}`'ye `%` ile git, sonra tekrar `%` ile başa dön.

```cpp
int f(int x) {
    if (x > 0) {
        return x;
    }
    return -x;
}
```

Nasıl: ilk satırdaki `{`'e git (`f{`), `%`.

### Pratik 3b

`%` ile bütün bloğu sil: `f{`, `d%`. Sonra `u` ile geri al. `y%` kopyalar,
`v%` seçer.

### Pratik 3c

Paragraf: `}` ile bir sonraki boş satıra atla, `{` ile geri gel. `dap` bir
paragrafı siler (**a** **p**aragraph), `yip` kopyalar.

```
first paragraph
still first

second paragraph
```

## 4. Geri dönme — jumplist

Uzağa her atlayışın (`gg`, `G`, `%`, `/`, `gd`, Telescope ile dosya açmak)
bir iz bırakır:

| Tuş | Ne yapar |
| --- | --- |
| `<C-o>` | geldiğin yere **geri** (**o**ut) — dosyalar arası da çalışır |
| `<C-i>` | ileri (bazı terminallerde `Tab` ile çakışır) |
| `''` | son atlamadan önceki satır |
| `gi` | son insert yaptığın yere git ve insert moda gir |

### Pratik 4

`gg`, sonra `G`, sonra `<C-o>` → başa döner. `<C-o>` bir daha → `gg`'den
önceki yere.

## 5. Ders 1 ile birleştir

Hareketlerin asıl gücü:

| Komut | Ne yapar |
| --- | --- |
| `dw` | kelimeyi sil |
| `d3w` | üç kelimeyi sil |
| `dG` | buradan dosya sonuna kadar sil |
| `dgg` | buradan dosya başına kadar |
| `y}` | paragraf sonuna kadar kopyala |
| `c%` | parantez bloğunu değiştir |
| `vf)` | paranteze kadar seç |
| `d/foo` + `Enter` | bir sonraki `foo`'ya **kadar** sil |

### Pratik 5

`# BEGIN` ile `# END` arasını sil (satırlar dahil).

```
keep
# BEGIN
remove
remove
# END
keep
```

Nasıl: `# BEGIN`'e git, `d/END` + `Enter` — `# END`'in başına kadar siler,
`# END` satırının kendisi kalır; `dd` ile onu da al. Ya da `V` ile seç, `}`
ile paragraf sonuna, `d`.

## Özet

```
w b e        kelime
f t ; ,      satırda karakter
H L 0        satır uçları
gg G :N      dosya
{ }  %       paragraf, eşleşen parantez
<C-o>        geri dön
```

Oturdu mu? README'ye ✓, Ders 5: dosya ağacı.
