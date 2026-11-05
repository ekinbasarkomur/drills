# Ders 1 — Kopyala, sil, yapıştır

Vim'de "kopyala" ve "sil" aynı ailedendir: ikisi de metni bir **register**'a
koyar. Kafa karışıklığının tek kaynağı bu — `d` aslında *cut*.

| Komut | Adı | Ne yapar | Panoya yazar mı |
| --- | --- | --- | --- |
| `y` | **y**ank | kopyala | evet |
| `d` | **d**elete | sil **ve** panoya al | evet |
| `c` | **c**hange | sil, panoya al, insert moda gir | evet |
| `x` | — | imleçteki karakteri sil | **hayır** (biz kapattık) |
| `p` / `P` | **p**ut | sonrasına / öncesine yapıştır | — |
| `<leader>p` | — | son **yank**'ı yapıştır, aradaki silmeleri yok say | — |

`y`, `d`, `c` tek başına bir şey yapmaz; arkasından **ne kadar** olduğunu
söylersin. Bu "ne kadar"a *motion* ya da *text object* denir ve üçünde de
aynıdır. Yani `yiw`'i öğrendiysen `diw` ve `ciw`'i de öğrenmiş oldun.

## 1. Satır

| Tuş | Ne yapar |
| --- | --- |
| `yy` | satırı kopyala |
| `dd` | satırı sil |
| `cc` | satırı sil, insert moda gir |
| `3yy` / `3dd` | üç satır |
| `p` | kopyalananı **altına** yapıştır (satır kopyalandıysa yeni satır açar) |
| `P` | **üstüne** yapıştır |

### Pratik 1a

Aşağıdaki listede `banana` satırını `cherry`'nin altına kopyala. Sonuç dört
satır olmalı: apple, banana, cherry, banana.

```
apple
banana
cherry
```

Nasıl: `banana`'ya git, `yy`, `cherry`'ye in (`j`), `p`.

### Pratik 1b

Aşağıda `WRONG` satırını sil, sonra `delta`'yı `alpha`'nın **üstüne** taşı.
Hedef: delta, alpha, beta, gamma.

```
alpha
beta
WRONG
gamma
delta
```

Nasıl: `WRONG`'a git, `dd`. `delta`'ya git, `dd` (artık panoda), `alpha`'ya
çık, `P` (büyük: üstüne).

## 2. Kelime

| Tuş | Ne yapar |
| --- | --- |
| `yiw` | **i**nner **w**ord — imleç neredeyse o kelimeyi kopyala |
| `diw` | kelimeyi sil, boşluklar kalır |
| `daw` | **a** word — kelimeyi **ve** yanındaki boşluğu sil (cümleden kelime çıkarırken bu) |
| `ciw` | kelimeyi sil, yerine yaz |
| `dw` | imleçten kelimenin sonuna kadar sil (`diw`'den farkı: imleç kelimenin ortasındaysa başı kalır) |
| `viw` | kelimeyi seç (visual) |

`i` = inner (sadece içi), `a` = around (çevresiyle). Bu ayrım tırnak ve
parantezde de aynı: `i"`, `a"`, `i(`, `a(`.

### Pratik 2a

Aşağıdaki cümlede `quick` kelimesini `slow` yap. Hedef: `the slow brown fox`.

```
the quick brown fox
```

Nasıl: `quick`'in herhangi bir harfine git, `ciw`, `slow` yaz, `Esc`.

### Pratik 2b

`brown` kelimesini cümleden çıkar, çift boşluk kalmasın. Hedef: `the quick fox`.

```
the quick brown fox
```

Nasıl: `brown`'a git, `daw`. (`diw` yapsaydın `the quick  fox` olurdu — iki
boşluk.)

### Pratik 2c

Birinci satırdaki `value` kelimesini kopyalayıp ikinci satırdaki `XXX`'in
üstüne yapıştır. Hedef: `result = value`.

```
total = value
result = XXX
```

Nasıl: `value`'ya git, `yiw`. `XXX`'e in, `viw` ile seç, `p`. Pano hâlâ
`value` — bir daha `viw` + `p` yapabilirsin, eskiden olduğu gibi `XXX` ile
takas olmaz.

## 3. Tırnak ve parantez içi

| Tuş | Ne yapar |
| --- | --- |
| `yi"` | çift tırnağın **içini** kopyala |
| `ci"` | içini sil, yerine yaz |
| `da"` | tırnaklarla birlikte sil |
| `ci(` / `ci)` | parantez içini değiştir (ikisi de aynı) |
| `ci[` `ci{` `ci<` | köşeli, süslü, açılı için aynısı |
| `cit` | HTML/XML **t**ag içi |

İmlecin tırnağın **içinde** olması gerekmez; aynı satırda tırnaktan **önce**
olması yeter, Vim ileriye bakar.

### Pratik 3a

`"hello"` içini `goodbye` yap.

```python
greeting = "hello"
```

Nasıl: satır başındayken `ci"`, `goodbye`, `Esc`. İmleç `g`'deyken bile çalışır.

### Pratik 3b

Fonksiyon çağrısının argümanlarını `a, b, c` yap.

```python
total = add(1, 2, 3)
```

Nasıl: `add`'in üstündeyken `ci(`, `a, b, c`, `Esc`.

### Pratik 3c

Birinci satırdaki liste içeriğini kopyala, ikinci satırdaki boş listenin içine
koy. Hedef: `second = [1, 2, 3]`.

```python
first = [1, 2, 3]
second = []
```

Nasıl: `first` satırında `yi[`. `second` satırında `]`'e git, `P` (öncesine).
Ya da imleci `[` ile `]` arasına koyup `p`.

## 4. Satırın bir kısmı

| Tuş | Ne yapar |
| --- | --- |
| `dL` | imleçten satır **sonuna** kadar sil (`L` = satır sonu, bizim ekledik; `D` de aynı) |
| `yL` | satır sonuna kadar kopyala |
| `cL` | satır sonuna kadar sil, yaz (`C` de aynı) |
| `dH` | imleçten satır **başına** kadar sil |
| `I` / `A` | satır başına / sonuna git ve insert moda gir |

### Pratik 4a

Yorumu sil. Hedef: `x = compute(a)`.

```python
x = compute(a)  # TODO: remove this comment
```

Nasıl: `#`'e git (`f#` — **f**ind `#`), `dL`. Sonra kalan boşluklar için `x`
iki kez, ya da `#`'ten önceki boşluğa gidip `dL`.

### Pratik 4b

Satırın sonuna `, c` ekle. Hedef: `call(a, b, c)`.

```python
call(a, b)
```

Nasıl: `A` → sonuna atlar ve insert modda — ama `)` dan sonra. `$` ile sona
git, `i` ile `)`'in önüne gir, `, c` yaz. Daha kısası: `f)` + `i`.

## 5. Visual mod — önce seç, sonra işle

Yukarıdakilerin hepsi "komut + ne kadar". Bazen önce ne kadar olduğunu
**görmek** istersin:

| Tuş | Ne yapar |
| --- | --- |
| `v` | karakter karakter seç |
| `V` | satır satır seç |
| `<C-v>` | dikdörtgen (blok) seç |
| seçiliyken `y` / `d` / `c` / `p` | kopyala / sil / değiştir / üstüne yapıştır |
| seçiliyken `J` `K` | seçimi aşağı / yukarı **taşı** (bizim ekledik) |
| seçiliyken `H` `L` | seçimi sola / sağa **girintile** |
| `gv` | son seçimi geri getir |

### Pratik 5a

Üç satırı `V` ile seç, `J` ile `end`'in altına taşı. Hedef: end, one, two, three.

```
one
two
three
end
```

Nasıl: `one`'a git, `V`, `jj`, `J` — seçim bir satır aşağı kaydı. Bir daha `J`.
Seçim kaybolmadı, istediğin kadar bas.

### Pratik 5b

`def` bloğunun gövdesini bir seviye içeri al.

```python
def f():
x = 1
return x
```

Nasıl: `x = 1`'e git, `V`, `j`, `L`. Seçim duruyor; fazla gittiysen `H`.

### Pratik 5c — blok seçim

Üç satırın başına aynı anda `# ` koy.

```
first line
second line
third line
```

Nasıl: `first`'ün `f`'sine git, `<C-v>`, `jj` (üç satırda birer karakterlik
sütun seçildi), `I` (büyük I — blok insert), `# ` yaz, `Esc`. Esc'ye basınca
üç satıra birden uygulanır.

## 6. Geri alma ve tekrarlama

| Tuş | Ne yapar |
| --- | --- |
| `u` | geri al |
| `<C-r>` | ileri al (redo) |
| `.` | **son değişikliği tekrarla** — `ciw` + yazı + `Esc` tek bir değişikliktir |

### Pratik 6

`foo`'yu `bar` yap, sonra diğer `foo`'larda sadece `n` + `.` ile devam et.

```
foo one
foo two
foo three
```

Nasıl: ilk `foo`'da `ciw`, `bar`, `Esc`. `/foo` + `Enter` ile sonrakine git
(ya da `*` ile imleçteki kelimeyi ara), `.` bas. `n`, `.`. Üç değişiklik, bir
kez yazdın.

## Özet — ezberlenecek olan sadece bu

```
y d c      +  iw  aw  i"  a"  i(  i[  i{  L  H
kopyala    ne kadar
sil
değiştir
```

Sol sütundan birini, sağ sütundan birini seç; 3 × 10 = 30 komut, hepsi aynı
mantık. `p` yapıştırır, `<leader>p` son kopyaladığını yapıştırır, `.` son
yaptığını tekrarlar.

Hepsi oturduysa README'de 01'e ✓ koy; Ders 2 `nvim-surround` — tırnak ve
parantezleri **eklemek** ve **değiştirmek** (bu derste sadece içlerini
düzenledik).
