# Ders 0 — Claude'u açmak ve kapatmak

Hepsi `<leader>a` altında (`<leader>` = boşluk). Boşluğa basıp bir saniye
bekle, which-key hepsini listeler.

| Tuş | Ne yapar |
| --- | --- |
| `<leader>aa` | Claude terminalini aç / kapat. Kapatınca oturum arkada yaşamaya devam eder |
| `<leader>af` | Terminale odaklan (açıkken) |
| `<leader>ac` | Bu klasördeki **son** oturumu sürdür |
| `<leader>ar` | Oturum listesinden seç |
| `<leader>ab` | Açık dosyayı bağlam olarak gönder |
| `<leader>as` | Seçili satırları gönder (önce `V` ile seç) |
| `<leader>ay` / `<leader>an` | Claude'un önerdiği diff'i kabul et / reddet |

Terminalden editöre dönmek: **`<C-h>`** — tek tuş, çıkar ve sola geçer. (`Esc Esc`
de terminal modundan çıkar; tek `Esc` Claude'un kendisine gider.)

Claude'a bağlam vermek için `<leader>y` grubu: `yf` bu dosyanın yolu + satır
(`nvim/ders-00-claude.md#L12`), `yp` mutlak yol, visual'da `yc` seçimi dosya
adı ve satır numarasıyla kod bloğu olarak panoya — sonra Claude'a yapıştır.

## Pratik

1. `<leader>aa` — terminal sağda açılsın.
2. `<C-h>` — bu dosyaya geri dön.
3. Aşağıdaki üç satırı `V` + `jj` ile seç, `<leader>as` ile gönder, Claude'a
   "bu ne?" diye sor.

```python
def f(xs):
    return sorted(set(xs))[-2]
```

4. `<leader>aa` ile kapat, tekrar `<leader>aa` ile aç — konuşma yerinde duruyor.
5. nvim'den tamamen çık (`:qa`), tekrar aç, `<leader>ac` — yine aynı konuşma.

Oturumlar **çalışma dizinine** bağlı: nvim'i `~/projects/drills` içinden
açmazsan bu oturumu göremezsin.
