# 155 · Min Stack — eager vs lazy `mins`

İki çözüm de O(1), iki yığın kullanıyor. Fark `mins` yığınına **ne zaman**
yazdıklarında. Ölçümler bu makinede, 30.000 push + 30.000 pop ile.

## Eager — her push'ta yaz

`mins` her zaman `stack` ile aynı boyda; her katta "o anki minimum" yazar.

```python
def push(self, val: int) -> None:
    self.stack.append(val)
    if self.min_stack:
        self.min_stack.append(min(val, self.min_stack[-1]))
    else:
        self.min_stack.append(val)

def pop(self) -> None:
    self.stack.pop()
    self.min_stack.pop()
```

## Lazy — yalnızca yeni minimum gelince yaz

`pop` ancak silinen eleman o anki minimumsa `mins`'ten çıkarır.

```python
def push(self, value: int) -> None:
    if not self.min_stack:
        self.min_stack.append(value)
    elif value <= self.min_stack[-1]:
        self.min_stack.append(value)
    self.stack.append(value)

def pop(self) -> None:
    popped = self.stack.pop()
    if self.min_stack[-1] == popped:
        self.min_stack.pop()
```

Rust karşılığı:

```rust
fn push(&mut self, value: i32) {
    self.stack.push(value);
    if let Some(smallest) = self.mins.last().cloned() {
        if value <= smallest {
            self.mins.push(value);
        }
    } else {
        self.mins.push(value);
    }
}

fn pop(&mut self) {
    let top = self.stack.pop().unwrap();
    let smallest = *self.mins.last().unwrap();
    if top == smallest {
        self.mins.pop();
    }
}
```

## Ölçüm

Rust (`rustc -O`, 2.000 tekrar):

| Girdi | eager | lazy | `mins` boyu (lazy) | Kazanç |
| --- | --- | --- | --- | --- |
| azalan (en kötü) | 283 ms | 218 ms | 30.000 | 1.3x |
| artan | 207 ms | 134 ms | 1 | 1.5x |
| rastgele | 236 ms | 107 ms | 11 | **2.2x** |

Python (5 koşunun en iyisi):

| Girdi | eager | lazy | Kazanç |
| --- | --- | --- | --- |
| azalan | 5.5 ms | 5.4 ms | 1.02x |
| artan | 5.4 ms | 4.4 ms | 1.21x |
| rastgele | 5.3 ms | 4.5 ms | 1.19x |

## Neden

- **Asıl kazanç bellekte.** Rastgele veride `mins` 30.000 yerine 11 elemanda
  kalıyor: tek bir cache line, hiç yeniden ayırma yok. Dokunulan bellek
  binlerce kat az. Rust'taki 2.2x'in kaynağı bu.
- **Python'da fark küçülüyor** (1.2x) çünkü zamanın çoğu yorumlayıcı yükünde
  geçiyor, önbellek etkisi yanında kayboluyor. Kalan kazanç her push'taki
  `min()` çağrısından kurtulmak.
- **En kötü durumda (azalan girdi)** `mins` yine tam boya çıkıyor ve avantaj
  dal tahmini seviyesine iniyor. Asimptotik bir fark değil, sabit çarpanda.

## Tuzaklar

- `value <= smallest` içindeki **`<=` şart**. `<` yazarsan tekrar eden
  minimumlar bozulur: `[2, 1, 1]`'de ikinci `1` `mins`'e girmez, ilkini
  pop'layınca minimum yanlışlıkla `2`'ye döner.
- Karşılığında `pop` pahalılaşıyor: artık `stack`'in tepesini okuyup
  karşılaştırmak gerekiyor. Push tarafındaki kazancın yanında önemsiz kalıyor.

## Ölçülüp elenen: `map_or` vs `match`

Bunların arasında fark **yok**, turdan tura yön değiştiriyor — gürültü.

```rust
// ayni koda derleniyor
let m = match self.mins.last() { Some(&cur) => value.min(cur), None => value };
let m = self.mins.last().map_or(value, |&cur| value.min(cur));
```

`vec![]` ile `Vec::new()` de aynı şey; `vec![]` boş hâlde doğrudan
`Vec::new()`'e açılıyor. LeetCode'un gösterdiği ms değerleri ortak makinenin
anlık yükü — aynı kodu iki kez gönderip 3 ms ile 40 ms arası sonuç almak normal.
