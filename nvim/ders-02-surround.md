# Ders 2 — Tırnak ve parantez: ekle, değiştir, sil

Ders 1'de tırnağın **içini** düzenledin (`ci"`). Bu derste tırnağın
**kendisini** ekleyip değiştiriyorsun. Plugin: `nvim-surround`. Üç komut:

| Komut | Adı | Ne yapar |
| --- | --- | --- |
| `ys` + ne kadar + karakter | **y**ou **s**urround | çevrele |
| `cs` + eski + yeni | **c**hange **s**urround | çevreleyeni değiştir |
| `ds` + karakter | **d**elete **s**urround | çevreleyeni kaldır |

"Ne kadar" kısmı Ders 1'dekiyle **aynı**: `iw`, `L`, `$`, `3w`, `ip`…

## 1. Ekle — `ys`

| Tuş | Sonuç |
| --- | --- |
| `ysiw"` | kelime → `"kelime"` |
| `ysiw)` | kelime → `(kelime)` |
| `ysiw(` | kelime → `( kelime )` — **açan** parantez boşluk koyar |
| `ysiw]` / `ysiw}` | köşeli / süslü |
| `yss"` | bütün satırı tırnağa al (`ss` = satır) |
| `ysL)` | imleçten satır sonuna kadar paranteze al |
| `ysiwt` | tag sorar: `div` yazarsan `<div>kelime</div>` |

Visual modda seçip **`S`** + karakter: `viw` sonra `S"`.

### Pratik 1a

`name`'i tırnağa al. Hedef: `print("name")`.

```python
print(name)
```

Nasıl: `name`'e git, `ysiw"`.

### Pratik 1b

Toplamı paranteze al. Hedef: `total = (a + b) * 2`.

```python
total = a + b * 2
```

Nasıl: `a`'ya git, `vee` ile `a + b`'yi seç (`e` kelime sonu, iki kez), `S)`.
Ya da seçmeden: `ys3w)` — üç kelime.

### Pratik 1c

Üç satırı `{ }` içine al. Hedef:

```
{
items
go
here
}
```

Satırlar:

```
items
go
here
```

Nasıl: `items`'a git, `V`, `jj`, `S{`. Satır seçimi + `S` çevreleyeni kendi
satırına koyar.

## 2. Değiştir — `cs`

| Tuş | Sonuç |
| --- | --- |
| `cs"'` | `"x"` → `'x'` |
| `cs'"` | tersi |
| `cs)]` | `(x)` → `[x]` |
| `cs(]` | aynı; açan/kapatan fark etmez, eski taraf için |
| `cs"<q>` | `"x"` → `<q>x</q>` |
| `cst"` | tag → tırnak |

### Pratik 2a

Tek tırnağı çift tırnak yap. İmleç tırnakların içinde olmalı.

```python
s = 'hello'
```

Nasıl: `hello`'ya git, `cs'"`.

### Pratik 2b

Tuple'ı listeye çevir. Hedef: `xs = [1, 2, 3]`.

```python
xs = (1, 2, 3)
```

Nasıl: parantez içine git, `cs(]`.

### Pratik 2c

`<b>`'yi `<strong>`'a çevir.

```html
<b>important</b>
```

Nasıl: `important`'a git, `cst<strong>` — `t` eski tag, sonra yeni tag'i yaz,
`Enter`.

## 3. Sil — `ds`

| Tuş | Sonuç |
| --- | --- |
| `ds"` | `"x"` → `x` |
| `ds)` | `(x)` → `x` |
| `dst` | tag'i kaldır, içeriği bırak |

### Pratik 3a

Gereksiz parantezi kaldır. Hedef: `return x + 1`.

```python
return (x + 1)
```

Nasıl: parantez içine git, `ds)`.

### Pratik 3b

Tırnağı kaldır. Hedef: `key = value`.

```python
key = "value"
```

## 4. Zincir — tipik düzenlemeler

Gerçek hayatta bunlar art arda gelir. Hepsi `.` ile tekrarlanabilir.

### Pratik 4a

Her satırdaki kelimeyi tırnağa al. İlkinde `ysiw"`, sonrakilerde `j` + `.`.

```
alpha
beta
gamma
```

### Pratik 4b

f-string yap: `"x"` → `f"x"`. Surround değil, Ders 1: tırnağa git, `F"`
(geriye tırnak bul), `i`, `f`, `Esc`. Ya da `H` + `f"` + `i`.

```python
msg = "hello {name}"
```

## Özet

```
ys  +  iw / L / 3w / ss   +   " ) ] } ' t
cs  +  eski  +  yeni
ds  +  karakter
```

Açan parantez (`(`) boşluk koyar, kapatan (`)`) koymaz. Visual'da `S`.

Oturdu mu? README'ye ✓, sıradaki Ders 3: arama ve değiştirme.
