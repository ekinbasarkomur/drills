# Ders 9 — Git

Bu ders satır düzeyi: **gitsigns**. Repo düzeyi (lazygit, çok dosyalı diff)
Ders 10'da.

## 1. Kenardaki işaretler

Sol kenarda:

| İşaret | Anlamı |
| --- | --- |
| yeşil `▎` | eklenmiş satır |
| sarı `▎` | değişmiş satır |
| kırmızı `` | buradan satır silinmiş |

Değişen her bölgeye **hunk** denir. Git'in her şeyi `<leader>g` altında; hunk işleri bir alt seviyede, `<leader>gh`.

## 2. Hunk'lar arasında gezmek

| Tuş | Ne yapar |
| --- | --- |
| `]c` / `[c` | sonraki / önceki değişiklik (**c**hange) |
| `<leader>ghp` | hunk'ı **önizle** — eski hâli ile yan yana, küçük pencerede |
| `<leader>gd` | bütün dosyayı diff görünümünde aç (**d**iff this) |

### Pratik 1

Bir dosyada üç ayrı yere birer satır ekle (ya da değiştir). `gg`, sonra `]c`
`]c` `]c` — üç değişikliği gez. Birinde `<leader>ghp` — ne değişmiş gör, `q`.
`<leader>gd` — tam diff; sol eski, sağ yeni. `<C-w>o` ile kapat.

## 3. Hunk'ı geri al / stage et

| Tuş | Ne yapar |
| --- | --- |
| `<leader>ghr` | hunk'ı **geri al** (**r**eset) — dosyadaki o değişiklik silinir |
| `<leader>ghs` | hunk'ı **stage** et — commit'e hazırla |
| `<leader>ghS` | bütün dosyayı stage et |
| `<leader>gb` | bu satırı kim, ne zaman, hangi commit'te yazmış (**b**lame) |

`ghr` tehlikelidir: değişikliğin gider. Ama `u` ile geri gelir.

### Pratik 2

Pratik 1'deki üç değişiklikten ortadakine `]c` ile git, `<leader>ghr` —
kayboldu. `u` — geldi. İlkine git, `<leader>ghs` — işaret rengi değişti,
stage'lendi. `<leader>gb` — kendi adını görürsün.

## 4. Terminalde git

Commit, push, log için `<leader>gg` (lazygit, Ders 10). Terminalden de olur:
`<C-\>` ile aç, `git status`, `git add`, `git commit`.

Faydalı:

```
git diff            kaydedilmemiş değişiklikler
git diff --staged   stage'lenmiş olanlar
git log --oneline   tarih
git checkout -- f   dosyayı son commit'e döndür
```

## 5. Review akışı — şimdilik

Claude bir şey değiştirdiğinde:

1. `<leader>ff` ile dosyayı aç
2. `]c` ile değişiklikleri gez, her birinde `<leader>ghp`
3. İstemediğini `<leader>ghr` ile at
4. Kalanı `<leader>ghS` ile stage et, terminalde commit

Çok dosyalı akış Ders 10'da.

## Özet

```
]c  [c          değişiklikler arasında
<leader>ghp gd  gör
<leader>ghr ghs geri al, stage et
<leader>gb      kim yazmış
```

Oturdu mu? README'ye ✓, Ders 10: ajanla çalışmak.
