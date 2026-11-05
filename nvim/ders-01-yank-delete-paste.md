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

### Pratik 1c

Satırı kopyala, altına yapıştır, kopyada `a`'yı `b` yap. Hedef: `a = 1` / `b = 1`.

```
a = 1
```

Nasıl: `yy` `p` `fa` `rb` — `r` tek karakteri değiştirir, insert'e girmez.

### Pratik 1d — birleştir, böl

İki satırı tek satır yap. Hedef: `first second`.

```
first
second
```

Nasıl: `first`'te `J` — normal modda **J** = **j**oin. (Visual'daki `J` taşır,
karıştırma: normal modda birleştirir.)

Sonra geri böl: `fs` (second'ın s'si) `i` `Enter` `Esc`.

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

### Pratik 2d

`three`'ü seç ve büyüt. Hedef: `one two THREE four`.

```
one two three four
```

Nasıl: `viw` `U`. (`u` küçültür, `~` tersler.)

### Pratik 2e

İki kelimenin yerini değiştir. Hedef: `second first`.

```
first second
```

Nasıl: `de` (first'ü kes → ` second`) `x` (baştaki boşluk; pano korunur)
`A` ` ` `Esc` `p`. Beş adım — Vim'de kelime takası için kısa yol yok; bazen
`ciw` ile yazmak daha hızlıdır. Bunu bilmek de pratik.

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

### Pratik 4c — satır ucu antrenmanı

Beşi art arda, her biri tek komut:

Sona `!` ekle. Hedef: `the end is here!`

```
the end is here
```

Nasıl: `A` `!` `Esc`.

Başa `# ` koy. Hedef: `# comment this`

```
comment this
```

Nasıl: `I` `# ` `Esc`.

Sondaki `;`'ı sil. Hedef: `return x`

```
return x;
```

Nasıl: `L` `x`.

İmleç `keep`'in `k`sinde: satır **başına** kadar sil. Hedef: `keep this`

```
remove this keep this
```

Nasıl: `dH`.

İki satırın sonuna `,` ekle, ikincisini `.` ile. 

```
alpha
beta
```

Nasıl: `A` `,` `Esc` — `j` `.`

### Pratik 4d

Girintili satırda `H` ile `0` farklı yere gider: `H` ilk harfe, `0` sütun 0'a.
İmleci ortaya koy, `L` sona, `H` başa, `0` gerçek başa.

```
    indented line here
```

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

### Pratik 5d — satır satır seçme

Üç satırı seç ve sil. Hedef: sadece `keep`.

```
delete me
delete me too
and me
keep
```

Nasıl: `V` `jj` `d`. (Ya da `3dd`.)

Paragrafı seç — boş satıra kadar hepsi.

```
line one
line two
line three

next paragraph
```

Nasıl: `vip` (**i**nner **p**aragraph). `dip` siler, `yip` kopyalar.

Üç satırı kopyala, en alta yapıştır. Hedef: 6 satır.

```
a
b
c
```

Nasıl: `V` `jj` `y` — `G` — `p`.

Satırın yarısından öbür satırın yarısına kadar seç ve sil. Hedef: `one thr`
gibi kırık bir satır.

```
one two
three four
```

Nasıl: `two`'da `v`, `j`, `d`. (`V` satır bütünüyle seçer, `v` karakterden.)

### Pratik 5e — seçimi taşıma antrenmanı

`move me`'yi en alta taşı. Hedef: a, b, c, move me.

```
move me
a
b
c
```

Nasıl: `V` `J` `J` `J`. Seçim seninle gelir.

İki satırı birlikte yukarı taşı. Hedef: x, y, a, b.

```
a
b
x
y
```

Nasıl: `x`'te `V` `j` `K` `K`.

Bloğu içeri al **ve** aşağı taşı, seçimi bırakmadan. Hedef: anchor,
␣␣␣␣block, ␣␣␣␣block.

```
block
block
anchor
```

Nasıl: `V` `j` `L` `J`.

`else` bloğunu `if` bloğunun üstüne çıkar.

```python
if x:
    do_a()
else:
    do_b()
```

Nasıl: `else:`'de `V` `j` `K` `K`. Sonuç mantıksız ama hareket doğru.

Tek satırı normal modda taşı: `dd` `p` aşağı, `dd` `k` `P` yukarı.

```
first
second
```

## 6. Geri alma ve tekrarlama

| Tuş | Ne yapar |
| --- | --- |
| `u` | geri al |
| `U` | ileri al (redo) — Shift = tersi, `p`/`P` gibi (`<C-r>` de çalışır) |
| `.` | **son değişikliği tekrarla** — `ciw` + yazı + `Esc` tek bir değişikliktir |
| `3u` | üç adım geri |

Shift kuralı dosyanın her yerinde: `p` altına / `P` üstüne, `n` ileri / `N`
geri, `J` aşağı / `K` yukarı, `u` geri / `U` ileri, `f` ileri / `F` geri.

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

### Pratik 6b — insert modda yapıştır

Parantez içini al, satır sonuna yapıştır. Hedef: `f(x) x`

```
f(x)
```

Nasıl: `yi(` `A` ` ` `<C-r>"` `Esc`. `<C-r>"` insert moddayken panoyu
yapıştırır; `<C-r>+` sistem panosunu. Terminalde (Claude'a) de aynı tuş.

3. satırdaki kelimeyi 1. satırın sonuna ekle. Hedef: `header: value`.

```
header:
filler
value
```

Nasıl: `jj` `yiw` `gg` `A` ` ` `<C-r>"` `Esc`.

## Özet — ezberlenecek olan sadece bu

```
y d c      +  iw  aw  i"  a"  i(  i[  i{  L  H
kopyala    ne kadar
sil
değiştir
```

Sol sütundan birini, sağ sütundan birini seç; 3 × 10 = 30 komut, hepsi aynı
mantık. `p` yapıştırır, `<leader>p` son kopyaladığını yapıştırır, `.` son
yaptığını tekrarlar, `u`/`U` geri/ileri.

Hepsi oturduysa README'de 01'e ✓ koy; Ders 2 hareket — buradaki `iw`, `L`
sütununu büyütür.
