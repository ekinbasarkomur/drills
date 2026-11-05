# Pratik — hareket ve seçim

Teori yok. Her blok: imleci **başlangıç** satırına koy, tek komutu yap, sonuç
**hedef** ile aynı olsun. Yanlışsa `u`. Dosyayı bozduysan `:e!`.

Her seti **üç tur** yap: ilkinde "nasıl" satırına bak, ikincisinde bakma,
üçüncüsünde zamanla. Haftada iki kez aç; eline oturunca seti geç.

---

## Set A — Satır uçları  `H` `L` `I` `A` `0`

**A1** — satırın sonuna git, `!` ekle. Hedef: `the end is here!`

```
the end is here
```

Nasıl: `A` `!` `Esc`. (`A` = sona git + insert.)

**A2** — satırın başına `# ` koy. Hedef: `# comment this`

```
comment this
```

Nasıl: `I` `# ` `Esc`. (`I` = ilk harfe git + insert; girinti varsa girintiden sonra.)

**A3** — imleci ortaya koy, `L` ile sona, `H` ile başa, `0` ile gerçek sütun 0'a.
Girintili satırda `H` ile `0` farklı yere gider; gör.

```
    indented line here
```

**A4** — imleçten satır sonuna kadar sil. İmleç `remove`'un `r`sinde.
Hedef: `keep this `

```
keep this remove all of this
```

Nasıl: `dL` (ya da `D`).

**A5** — imleçten satır **başına** kadar sil. İmleç `keep`'in `k`sinde.
Hedef: `keep this`

```
remove this keep this
```

Nasıl: `dH`.

**A6** — satır sonundaki `;`'ı sil. Hedef: `return x`

```
return x;
```

Nasıl: `L` `x`. (Ya da `$x`.)

**A7** — iki satırın sonuna `,` ekle, `.` ile tekrarlayarak.

```
alpha
beta
```

Nasıl: `A` `,` `Esc` — `j` `.`

**A8** — satırın sonuna git, **insert'e girmeden** son kelimeyi kopyala.
Hedef: pano = `last`

```
first middle last
```

Nasıl: `L` `yiw`.

---

## Set B — Kelime kelime  `w` `b` `e` `iw` `aw`

**B1** — `w` ile kelime kelime sona git, `b` ile başa dön. Kaç basış? (5 ileri, 5 geri)

```
one two three four five six
```

**B2** — `3w` ile üç kelime atla. İmleç `one`'da → `four`'da olmalı.

```
one two three four five six
```

**B3** — imleç `three`'de. `e` ile kelimenin sonuna, `ge` ile öncekinin sonuna.

```
one two three four
```

**B4** — `three`'ü sil, boşluk kalmasın. Hedef: `one two four`

```
one two three four
```

Nasıl: `daw`.

**B5** — `three`'ü `3` yap. Hedef: `one two 3 four`

```
one two three four
```

Nasıl: `ciw` `3` `Esc`.

**B6** — `three`'ü seç ve büyüt. Hedef: `one two THREE four`

```
one two three four
```

Nasıl: `viw` `U`. (`u` küçültür, `~` tersler.)

**B7** — `foo.bar.baz`'ı `W` ile tek kelime olarak atla; `w` ile kaç parça?

```
call foo.bar.baz now
```

Nasıl: `W` 1 atlar, `w` 5 (nokta ayırır).

**B8** — `two`'dan `four`'a kadar seç ve sil. Hedef: `one five`

```
one two three four five
```

Nasıl: `two`'da `v`, `2e` (iki kelime sonu… `four`'un sonu), `d`. Ya da `d3w`
sonra bir boşluk `x`. Ya da `two`'da `v`, `/five` + `Enter`, `h`, `d`.

---

## Set C — Satır satır seçme  `V` `Vj` `vip`

**C1** — üç satırı `V` ile seç, `d` ile sil. Hedef: sadece `keep`.

```
delete me
delete me too
and me
keep
```

Nasıl: `V` `jj` `d`. Ya da `3dd`.

**C2** — paragrafı seç. Hedef: boş satıra kadar hepsi seçili.

```
line one
line two
line three

next paragraph
```

Nasıl: `vip` (**i**nner **p**aragraph). `dip` siler, `yip` kopyalar.

**C3** — `def` bloğunu seç: `def` satırında `V`, `}` ile paragraf sonuna.

```python
def f():
    a = 1
    b = 2
    return a + b

def g():
    pass
```

**C4** — fonksiyon gövdesini girintile. Hedef: `x` ve `return` 4 boşluk içeride.

```python
def h():
x = 1
return x
```

Nasıl: `x = 1`'de `V` `j` `L`.

**C5** — üç satırı kopyala, en alta yapıştır. Hedef: 6 satır, aynı üçü tekrar.

```
a
b
c
```

Nasıl: `V` `jj` `y` — `G` — `p`.

**C6** — satırların yarısını seç: `v` ile `two`'dan `three`'nin ortasına.
`V` ile olmaz, `v` ile olur. Sil, hedef: `one thr`… gibi kırık bir satır.

```
one two
three four
```

Nasıl: `two`'da `v`, `j`, `d`.

---

## Set D — Seçimi taşıma  `J` `K` `H` `L` (visual)

**D1** — `move me`'yi en alta taşı. Hedef: a, b, c, move me.

```
move me
a
b
c
```

Nasıl: `V` `J` `J` `J`. Seçim seninle gelir.

**D2** — iki satırı birlikte yukarı taşı. Hedef: x, y, a, b.

```
a
b
x
y
```

Nasıl: `x`'te `V` `j` `K` `K`.

**D3** — bloğu bir seviye sağa, sonra sola. Hedef: değişmemiş.

```
unindented
unindented
```

Nasıl: `V` `j` `L` `H`.

**D4** — bloğu içeri al **ve** aşağı taşı, seçimi bırakmadan.

```
block
block
anchor
```

Nasıl: `V` `j` `L` `J`. Hedef: anchor, ␣␣␣␣block, ␣␣␣␣block.

**D5** — `else` bloğunu `if` bloğunun üstüne çıkar.

```python
if x:
    do_a()
else:
    do_b()
```

Nasıl: `else:`'de `V` `j` `K` `K`. Sonuç mantıksız ama hareket doğru.

**D6** — tek satırı normal modda taşı: `ddp` (aşağı), `ddkP` (yukarı).

```
first
second
```

Nasıl: `first`'te `dd` `p` → second, first.

---

## Set E — Karaktere zıplama  `f` `t` `F` `T` `;` `,`

**E1** — satır başında, `f(` ile paranteze, `;` ile sonrakine, `,` ile geri.

```
call(a) and call(b) and call(c)
```

**E2** — `,`'e kadar sil (virgül kalsın). Hedef: `f(, b)`

```
f(a_long_name, b)
```

Nasıl: `f(` `l` `dt,`.

**E3** — `,` dahil sil. Hedef: `f( b)`

```
f(a_long_name, b)
```

Nasıl: `f(` `l` `df,`.

**E4** — satır sonundan geriye, `F"` ile tırnağa. Sonra `T"` ile tırnağın bir sağına.

```
print("hello world")
```

Nasıl: `L` `F"` — `;` bir önceki tırnağa. `T"` tırnağın sağındaki `h`'ye.

**E5** — ikinci `=`'e git. Hedef: imleç `b = 2`'nin `=`'inde.

```
a = 1; b = 2; c = 3
```

Nasıl: `2f=` (sayı + f). Ya da `f=` `;`.

**E6** — `:` ile `;` arasını değiştir. Hedef: `key: NEW; rest`

```
key: value; rest
```

Nasıl: `f:` `ll` (iki sağ), `ct;` `NEW` `Esc`.

**E7** — `f` + `;` ile dört `x`'i tek tek `y` yap: `fx` `rx`… hayır — `fx` `ry` `;` `.`

```
x o x o x o x
```

Nasıl: `fx` `ry` sonra `;` `.` `;` `.` `;` `.` (`r` = bir karakteri değiştir).

---

## Set F — Aynı kelimeye zıplama  `*` `#` `n` `N`

**F1** — `count`'a git, `*`, `n` `n` `n`. Kaç tane? Sonra `#` ile geri.

```python
count = 0
for c in data:
    count += c.count
total = count
```

**F2** — `*` ile bul, `.` ile hepsini değiştir. Hedef: her `old` → `new`.

```
old one
not old
old again
```

Nasıl: ilk `old`'da `*` (imleç sonrakine atlar, önemli değil), `ciw` `new`
`Esc`, `n` `.`, `n` `.`.

**F3** — `*` kelime sınırı arar: `cat` için `*`, `catalog`'u atlar. Gör.

```
cat catalog cat concat
```

**F4** — `g*` sınırsız arar: `catalog` ve `concat`'i de bulur.

---

## Set G — Karışık (gerçek hayat)

**G1** — ortadaki argümanı virgülüyle sil. Hedef: `f(a, c)`

```python
f(a, b, c)
```

Nasıl: `fb` `v` `f,` `l` `d` — `b`'den virgül ve boşluk dahil seç, sil.
(`daw` burada işe yaramaz: `f(a, , c)` bırakır.)

**G2** — iki satırı birleştir. Hedef: `first second`

```
first
second
```

Nasıl: `J` (normal modda **J** = join; visual'daki taşıma değil).

**G3** — satırı ikiye böl. Hedef: `first` / `second` ayrı satırlarda.

```
first second
```

Nasıl: `fs` (second'ın s'si) `i` `Enter` `Esc`. Ya da `f ` (boşluk) `r` `Enter`.

**G4** — satırı kopyala, altına yapıştır, yapıştırdığında `a`'yı `b` yap.

```
a = 1
```

Nasıl: `yy` `p` `fa` `rb`. Hedef: `a = 1` / `b = 1`.

**G5** — parantez içini al, satır sonuna yapıştır. Hedef: `f(x) x`

```
f(x)
```

Nasıl: `yi(` `A` ` ` `<C-r>"` `Esc`. (`<C-r>"` insert modda panoyu yapıştırır.)

**G6** — iki kelimenin yerini değiştir. Hedef: `second first`

```
first second
```

Nasıl: `de` (first'ü kes → ` second`) `x` (baştaki boşluk; pano korunur)
`A` ` ` `Esc` `p`. Beş adım — Vim'de kelime takası için kısa yol yok; bazen
`ciw` ile yazmak daha hızlıdır, bunu bilmek de pratik.

**G7** — satırdaki tüm boşlukları `_` yap. Hedef: `a_b_c`

```
a b c
```

Nasıl: `:s/ /_/g` + `Enter`. Hareket değil, `:s` — bazen o daha kısa.

**G8** — 3. satıra git, oradaki kelimeyi kopyala, 1. satırın sonuna ekle.

```
header:
filler
value
```

Nasıl: `3G` (ya da `jj`) `yiw` `gg` `A` ` ` `<C-r>"` `Esc`. Hedef: `header: value`.

---

## Zaman tutma

Her set için üçüncü turda süre tut; bir sonraki haftada karşılaştır.

| Set | Tur 1 | Tur 2 | Tur 3 | Hafta 2 |
| --- | --- | --- | --- | --- |
| A | | | | |
| B | | | | |
| C | | | | |
| D | | | | |
| E | | | | |
| F | | | | |
| G | | | | |
