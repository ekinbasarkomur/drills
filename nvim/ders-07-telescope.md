# Ders 7 — Telescope

Her şeyin bulanık arandığı tek pencere. Açılır, yazarsın, liste daralır,
`Enter`. Hepsi `<leader>f` altında (**f**ind).

## 1. Hangi picker ne zaman

| Tuş | Ne arar | Ne zaman |
| --- | --- | --- |
| `<leader>ff` | dosya **adı** | "lc0184'ü aç" |
| `<leader>fg` | dosya **içeriği** (live grep) | "`transform` nerede geçiyor" |
| `<leader>fb` | açık buffer'lar | "az önce baktığım dosya hangisiydi" |
| `<leader>fr` | son açılan dosyalar (**r**ecent) | "dün çalıştığım dosya" |
| `<leader>fh` | Neovim yardım sayfaları | "`:s` nasıl çalışıyordu" |
| `<leader>sw` | imleçteki kelime, projede | Ders 3 |
| `<leader>sf` | bu dosyada satırlar | Ders 3 |

Bulanık: `l184pd` yazsan `leetcode/pandas_track/lc0184…` bulur — sıra önemli,
aradaki harfler değil.

## 2. Picker içindeyken

| Tuş | Ne yapar |
| --- | --- |
| yazmak | daraltır |
| `<C-j>` / `<C-k>` | aşağı / yukarı |
| `Enter` | aç |
| `<C-v>` | dikey split'te aç |
| `<C-x>` | yatay split'te aç |
| `<C-t>` | yeni tab'da aç |
| `<C-p>` | önizlemeyi aç/kapat |
| `<C-q>` | **hepsini quickfix'e at** (aşağıda) |
| `Esc` | kapat (iki kez gerekebilir: önce insert'ten çıkar) |

### Pratik 1

`<leader>ff`, `2887` yaz, `Enter`. `<leader>fr` — az önce açtığın en üstte.
`<leader>ff`, `min stack` yaz (boşluk da olur), `<C-j>` ile Rust olanı seç,
`<C-v>` — yan yana açıldı. `<C-w>o` ile tek pencereye dön.

## 3. Quickfix — sonuç listesiyle çalışmak

Bir arama 20 sonuç verdiyse hepsini tek tek açmak yerine listeye alırsın:

| Tuş | Ne yapar |
| --- | --- |
| `<C-q>` (picker'da) | sonuçları quickfix'e gönder, listeyi altta aç |
| `]q` / `[q` | sonraki / önceki sonuç — dosyalar arasında atlar |
| `:copen` / `:cclose` | listeyi aç / kapat |
| `:cfirst` / `:clast` | ilk / son |
| `Enter` (listede) | o satıra git |

Ders 3'teki grug-far da `<leader>q` ile buraya atar.

### Pratik 2

`<leader>fg`, `check_eq!` yaz, `<C-q>`. Alttaki listede `Enter`. `]q` `]q`
`]q` — dosya dosya geziyorsun. `:cclose`.

### Pratik 3 — quickfix + değiştir

Quickfix'teki her dosyada aynı değişikliği yapmak:

```
:cdo s/eski/yeni/g | update
```

`cdo` = listedeki her girdi için çalıştır; `update` = değiştiyse kaydet.
Denemek için güvenli hedef: `<leader>fg` ile `Oturdu mu?` ara (sadece bu
klasördeki dersler), `<C-q>`, `:cdo s/Oturdu mu?/Oturdu mu?/g | update` —
hiçbir şey değişmez ama akışı görürsün.

## 4. Yardım bulmak

| Yol | Ne |
| --- | --- |
| `<leader>fh` + `surround` | plugin dokümanı |
| `:h ci"` | herhangi bir komutun yardımı |
| `K` (lua dosyasında) | imleçteki fonksiyonun yardımı |
| `<leader>` + bekle | which-key: o anda ne yapabilirsin |

### Pratik 4

`<leader>fh`, `text-objects` yaz, `Enter`. Vim'in bütün `iw`, `i"`, `ip`
listesi. `<C-o>` ile dön.

## Özet

```
<leader>ff  fg  fb  fr  fh      ad, içerik, buffer, son, yardım
<C-j> <C-k> Enter <C-v>         gez, aç
<C-q>  ]q  [q                   quickfix
```

Oturdu mu? README'ye ✓, Ders 8: LSP.
