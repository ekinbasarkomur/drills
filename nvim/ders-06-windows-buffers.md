# Ders 6 — Pencereler ve buffer'lar

Üç kavram, sık karıştırılır:

| Kavram | Ne | Nasıl düşün |
| --- | --- | --- |
| **buffer** | açılmış bir dosya, bellekte | sekme gibi — ama görünmek zorunda değil |
| **window** | ekrandaki bir bölme; bir buffer gösterir | çerçeve |
| **tab** | pencere düzeni | nadiren lazım, atla |

Yani 10 dosya açık olabilir (10 buffer) ama ekranda 2 pencere görürsün.

## 1. Buffer'lar arasında geçiş

| Tuş | Ne yapar |
| --- | --- |
| `Tab` / `S-Tab` | sonraki / önceki buffer |
| `<leader>fb` | buffer listesi (Telescope), yazarak seç |
| `<leader>bd` | bu buffer'ı kapat, önceki dosyaya düş |
| `<leader>bD` | görünmeyen **bütün** buffer'ları kapat (ajan 30 dosya açtıysa) |
| `<C-^>` | son iki dosya arasında zıpla (`<C-6>` ile aynı) |
| `<leader>w` | kaydet |
| `<leader>q` | pencereyi kapat |

### Pratik 1

`<leader>ff` ile `README.md`'yi aç, sonra `Makefile`'ı aç. `<C-^>` ile ikisi
arasında üç kez git-gel. `<leader>fb` ile listeyi gör. `<leader>bd` ile
Makefile'ı kapat — README'ye düşersin, ağaca değil.

## 2. Pencere açma ve kapatma

| Tuş | Ne yapar |
| --- | --- |
| `<C-w>v` | dikey böl (sağa yeni pencere, aynı dosya) |
| `<C-w>s` | yatay böl |
| `:vsplit dosya` | dikey böl ve o dosyayı aç |
| `<C-w>q` | bu pencereyi kapat (buffer kalır) |
| `<C-w>o` | diğer pencerelerin hepsini kapat (**o**nly) |
| `<C-h>` `<C-j>` `<C-k>` `<C-l>` | pencereler arası geçiş |
| `<C-Up>` `<C-Down>` `<C-Left>` `<C-Right>` | pencereyi büyüt / küçült |
| `<C-w>=` | hepsini eşitle |

### Pratik 2

`<C-w>v` — aynı dosya iki pencerede. Sağdakinde `G` ile sona git; soldaki
yerinde durur. `<C-h>` sola, `<C-l>` sağa. `<C-w>q` ile sağı kapat.

## 3. Bir dosyadan diğerine taşıma

Bu dersin asıl amacı. İki yol:

**Yol A — yan yana:**
1. `<C-w>v`, sağ pencerede `<leader>ff` ile hedef dosyayı aç
2. `<C-h>` sola, `V` ile satırları seç, `y`
3. `<C-l>` sağa, yere git, `p`

**Yol B — tek pencere:**
1. Seç, `y`
2. `<leader>ff` ile hedef dosyayı aç (ya da `<C-^>` ile az önce açtığına dön)
3. `p`

Pano register'da durduğu için dosya değiştirmek onu bozmaz.

### Pratik 3

Aşağıdaki fonksiyonu `nvim/deneme.md` diye yeni bir dosyaya taşı:

```python
def helper():
    return 42
```

Nasıl: `V` + `jj` + `d` (kes). `:e nvim/deneme.md` + `Enter` (yoksa oluşur).
`p`. `<leader>w`. `<C-^>` ile buraya dön; kaybolduğunu gör; `u` ile geri al.
Sonra `:!rm nvim/deneme.md` ile temizle (ya da ağaçtan `d`).

## 4. Terminal

| Tuş | Ne yapar |
| --- | --- |
| `<C-\>` | altta terminal aç/kapat (toggleterm) |
| `Esc Esc` | terminal modundan çık, normal moda |
| `<C-h>` | terminalden **tek tuşla** çık ve soldaki pencereye geç |
| `<C-k>` | normal moddayken üstteki pencereye |
| `i` | terminale geri gir |

Claude terminali de böyle bir pencere (Ders 0).

### Pratik 4

`<C-\>`, `make status` yaz, `Enter`. `Esc Esc`, `<C-k>` ile editöre (Claude sağdaysa `<C-h>` tek başına yeter). `<C-\>`
ile kapat, tekrar aç — çıktı yerinde.

## 5. Kaydetmeden çıkma dertleri

| Durum | Çözüm |
| --- | --- |
| "No write since last change" | `:w` sonra tekrar, ya da `:q!` (değişiklikleri at) |
| Hepsini kaydet ve çık | `:wqa` |
| Hepsini kaydetmeden çık | `:qa!` |
| Dosyayı diskteki hâline döndür | `:e!` |

## Özet

```
Tab  S-Tab  <C-^>   buffer gez        <leader>bd   kapat
<C-w>v  <C-w>s      böl               <C-w>q  <C-w>o   kapat
<C-h/j/k/l>         pencere gez       <C-ok>       boyut
<C-\>               terminal
```

Oturdu mu? README'ye ✓, Ders 7: Telescope.
