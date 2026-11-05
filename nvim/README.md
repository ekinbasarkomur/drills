# nvim dersleri

Her ders tek bir dosya. Dosyayı Neovim'de aç, baştan sona oku, "Pratik"
bölümlerinde yazılanı **o dosyanın içinde** yap. Yanlış gittiyse `u` ile geri
al; dosyayı kaydetmene gerek yok (`:e!` baştaki hâline döndürür).

| Ders | Konu | Neyi çözer | Durum |
| --- | --- | --- | --- |
| [00](ders-00-claude.md) | Claude'u açmak, kapatmak, seçim göndermek | | ✓ |
| [01](ders-01-yank-delete-paste.md) | `y` `d` `c` `p` ve text object'ler | panonu kaybetmeden kopyala-yapıştır; seçimi `J`/`K` ile taşı | |
| [02](ders-02-surround.md) | `nvim-surround` | tırnak, parantez ekle / değiştir / sil | |
| [03](ders-03-search-replace.md) | Arama ve değiştirme | `/` `*` `n`, `<leader>sr` dosyada, `<leader>sp` projede | |
| [04](ders-04-motion.md) | Hareket | `w b e`, `f t`, `%`, `{ }`, `gg G`, `:42`, `7j`, `<C-o>` geri | |
| [05](ders-05-file-tree.md) | Dosya ağacı (nvim-tree) | oluştur, yeniden adlandır, sil, taşı, açık dosyayı ağaçta bul | |
| [06](ders-06-windows-buffers.md) | Pencere ve buffer | split, boyut, `Tab`, `<leader>bd`; bir dosyadan diğerine taşıma | |
| [07](ders-07-telescope.md) | Telescope | `ff fg fb fr`, picker içinde gezinme, quickfix | |
| [08](ders-08-lsp.md) | LSP | `gd gr K`, rename, code action, `]d` ile hatalar arası | |
| [09](ders-09-git.md) | Git | hunk, blame, diff, stage | |
| [10](ders-10-agentic-review.md) | Agentic review | `<leader>y*` ile ajana yer göster; `gg → gv → go → ghp` ile değişikliği katman katman oku | |

Bir ders oturduğunda tabloya ✓ koy, sonrakine geç. Haftada bir-iki ders yeter;
amaç ezber değil, elin kendiliğinden gitmesi.
