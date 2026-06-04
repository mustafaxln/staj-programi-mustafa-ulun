# Git — Temel Komutlar ve Is Akisi

> 📌 Hafta 03 · branch · commit · push · pull · merge · conflict

## Icindekiler

| Bölüm | |
|:---:|:---|
| 🆕 | [Repo baslatma veya clone](#repo-baslatma-veya-clone) |
| 📋 | [status](#status) |
| ➕ | [add](#add) |
| 💾 | [commit](#commit) |
| 📜 | [log](#log) |
| 🌿 | [branch](#branch) |
| 🔀 | [checkout veya switch](#checkout-veya-switch) |
| 🔗 | [merge](#merge) |
| ⚔️ | [Conflict cozerken izlenecek adimlar](#conflict-cozerken-izlenecek-adimlar) |
| ☁️ | [push ve pull mantigi](#push-ve-pull-mantigi) |

---

## Repo baslatma veya clone

**Yeni repo (yerelde):**

```bash
git init
```

**Var olan repoyu klonlama:**

```bash
git clone git@github.com:kullanici/repo-adi.git
cd repo-adi
```

Staj reposunda zaten clone edilmis bir klasorde calisiyorum; ilk kurulumda `clone`, sifirdan proje acarken `init` kullanilir.

---

## status

Calisma alaninin durumunu gosterir: hangi branch'tesin, hangi dosyalar degismis, neler commit'e hazir.

```bash
git status
```

Ornek cikti (commit oncesi):

```text
On branch feature/week-03-cli
Changes not staged for commit:
        modified:   cli_app.py

Untracked files:
        ../cheatsheets/git.md
```

| Durum | Anlami |
|---|---|
| Untracked | Git henuz takip etmiyor; once `git add` gerekir |
| Changes not staged | Dosya degisti ama henuz stage'e alinmadi |
| Changes to be committed | `git add` yapildi, commit bekliyor |

> ℹ️ **Untracked dosyalar branch degistirince silinmez.** Commit etmeden `main` ↔ `feature` gecsen de dosya diskte kalir; sadece commit'lenen icerik branch'ler arasinda farklilasir.

---

## add

Degisiklikleri bir sonraki commit icin **stage**'e alir.

```bash
git add dosya.py
git add .                    # bulundugun klasordeki tum degisiklikler
git add week-03/cli_app.py   # repo kokunden yol ile
```

Ornek (week-03 icindeyken):

```bash
cd week-03
git add cli_app.py
```

---

## commit

Stage'deki degisiklikleri yerel repoda kalici bir **snapshot** olarak kaydeder.

```bash
git commit -m "uygulamaya gorev ekleme ozelligi eklendi"
```

Ornek cikti:

```text
[feature/week-03-cli e08034c] uygulamaya gorev ekleme ozelligi eklendi
 1 file changed, 4 insertions(+), 1 deletion(-)
```

Kisa ve acik mesaj: ne eklendi / ne duzeltildi (hafta 03'te her ozellik ayri commit).

---

## log

Gecmis commit'leri listeler.

```bash
git log
git log --oneline    # tek satir ozet
```

Merge commit'lerinde iki parent gorunur; hangi branch'in birlestigini anlamaya yarar.

---

## branch

Mevcut branch'leri listeler; `*` bulundugun branch'i gosterir.

```bash
git branch
```

Ornek:

```text
* feature/week-03-cli
  main
```

| Komut | Islev |
|---|---|
| `git branch` | Yerel branch listesi |
| `git branch -a` | Uzak branch'ler dahil (fetch sonrasi) |
| `git checkout -b yeni-isim` | Yeni branch olustur **ve** ona gec |

Hafta 03 ornegi:

```bash
git checkout -b feature/week-03-cli
# Switched to a new branch 'feature/week-03-cli'
```

---

## checkout veya switch

Baska bir branch'e gecmek icin kullanilir (Git 2.23+ ile `switch` de var; ayni is icin).

```bash
git checkout main
git checkout feature/week-03-cli
```

Ornek:

```text
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```

**Yeni branch + gecis tek komutta:**

```bash
git checkout -b feature/week-03-cli
```

---

## merge

Baska bir branch'teki commit'leri, **su an uzerinde oldugun** branch'e birlestirir.

```bash
git checkout main
git merge feature/week-03-cli
```

Basarili merge ornegi:

```text
Merge made by the 'ort' strategy.
 week-03/cli_app.py | 44 +++++++++++++++++++++++++++++++++++++++++++-
 1 file changed, 43 insertions(+), 1 deletion(-)
```

**Fast-forward:** Hedef branch'te arada baska commit yoksa Git sadece pointer'i ileri alir:

```text
Updating 3e9458e..d8f396a
Fast-forward
 week-03/cli_app.py | 6 +++++-
```

| Senaryo | Ne yapilir |
|---|---|
| Feature'i main'e almak (yerel) | `checkout main` → `merge feature/...` |
| Main'deki son degisiklikleri feature'a almak | `checkout feature/...` → `merge main` |
| Uzak main guncellemesi | `checkout main` → `pull origin main` |

> 📌 Takim calismasinda `main`'e dogrudan merge yerine cogu zaman **pull request** kullanilir; kod inceleme ve otomatik testler PR uzerinden yapilir. Hafta 03'te hem GitHub PR hem yerel `merge` denedim — detay: [`week-03/README.md`](../week-03/README.md).

---

## Conflict cozerken izlenecek adimlar

Ayni dosyanin ayni satiri iki branch'te farkli degistirilirse **merge conflict** olusur.

**1.** Merge veya pull sonrasi hata:

```text
CONFLICT (content): Merge conflict in week-03/cli_app.py
Automatic merge failed; fix conflicts and then commit the result.
```

**2.** Dosyayi ac; conflict isaretlerini bul:

```text
<<<<<<< HEAD
print("Program sonlandirildi")
=======
print("Program sonlandirildi kendine cook iyi bak!")
>>>>>>> feature/week-03-cli
```

| Isaret | Anlami |
|---|---|
| `<<<<<<< HEAD` | Su anki branch'teki (ornegin `main`) surum |
| `=======` | Ayirici |
| `>>>>>>> feature/...` | Birlestirilen branch'teki surum |

**3.** Isaretleri **tamamen sil**; kalmasini istedigin kodu birak (veya ikisini birlestir).

**4.** Cozulmus dosyayi stage'e al ve merge commit'i tamamla:

```bash
git add week-03/cli_app.py
git commit -m "Merge conflict cozuldu"
```

**5.** Feature branch hala gerideyse, main'i feature'a cek:

```bash
git checkout feature/week-03-cli
git merge main
```

Conflict'ten kacinmak icin: ayni satiri iki branch'te ayri ayri degistirmemeye calis; mumkunse tek branch'te gelistir, digerini merge/pull ile guncelle.

---

## push ve pull mantigi

### Push

Yerel commit'leri **uzak repoya** (ornegin GitHub `origin`) gonderir.

```bash
git push origin feature/week-03-cli
```

Ilk push'ta branch uzakta yoksa olusturulur:

```text
 * [new branch]      feature/week-03-cli -> feature/week-03-cli
```

Sonraki push'lar ayni branch'i gunceller:

```text
   769a43a..9540dba  feature/week-03-cli -> feature/week-03-cli
```

### Pull / fetch

| Komut | Islev |
|---|---|
| `git fetch` | Uzak degisiklikleri indirir, yerel branch'i otomatik birlestirmez |
| `git pull origin main` | Uzak `main`'i indirip **mevcut branch'e merge** eder (genelde `main` uzerindeyken kullanilir) |

Ornek — uzak main guncellendi, yerel main eski:

```bash
git checkout main
git fetch
git pull origin main
```

```text
Updating a79cfbf..ab41734
Fast-forward
 week-03/cli_app.py | 1 +
```

### Akis ozeti (hafta 03)

```text
[yerel feature] --commit--> --push--> [GitHub feature]
                                              |
                                    pull request (GitHub UI)
                                              v
[yerel main]    <--pull----- [GitHub main]
      |
      +--- merge feature (yerel, istege bagli)
```

1. Feature branch'te kod yaz → `add` → `commit` → `push origin feature/...`
2. GitHub'da PR ac → `main` ile birlestir (inceleme / test)
3. Yerelde `git checkout main` → `git pull origin main` ile guncel main'i al
4. Gerekirse `git checkout feature/...` → `git merge main` ile feature'i senkronla

---

## Sik karsilasilan durumlar

| Problem | Cozum / not |
|---|---|
| `Your branch is ahead of 'origin/main' by N commits` | Yerelde commit var, henuz push yok → `git push origin main` |
| Branch degistirdim, dosyam kayboldu | Untracked ise hala diskte; commit edilmediyse her branch'te ayni |
| Merge conflict | Isaretleri sil, `add`, `commit` |
| Uzak main ile yerel main farkli | `git pull origin main` (once `fetch` de yapilabilir) |

Daha fazla hafta 03 baglami (CLI kodu, takildigim noktalar): [`week-03/README.md`](../week-03/README.md)
