Author: CodeASAP.pl

- [Artykuł](https://blog.codeasap.pl/linux/luks-szyfrowane-pliki-jako-urzadzenia-blokowe/)


# Quick demo

W systemach klasy Unix, a więc i w Linux, możemy używać zwykłych plików jako odpowiednika dysków. Pliki te możemy formatować, a następnie montować i odmontowywać.
Na potrzeby demonstracji stworzymy plik o rozmiarze 8mb w całości wypełniony zerami.

## Tworzymy plik
```text
dd if=/dev/zero of=mydisk bs=1M count=8
```

Nasz plik odpowiada teraz czystej przestrzeni dyskowej.

```text
file mydisk
```

## Formatujemy

Plik następnie formatujemy. Użyję tutaj standardowego systemu plików ext4.

```text
mkfs.ext4 mydisk
```

Po sformatowaniu mamy w pliku odpowiednik partycji z gotowym systemem plików ext4.

```text
file mydisk
```

## Montujemy zasób

Tworzę katalog "mountpoint":
```text
mkdir mountpoint
```

a następnie montuję w nim nasz nowy "dysk".
Do zamontowania pliku potrzebujemy uprawnień administratora, posłużę się zatem komendą sudo.
```text
sudo mount mydisk mountpoint
```

W zamontowanym już zasobie utworzę katalog "test" i zmienię jego właściciela na swojego użytkownika.
```text
sudo mkdir -v mountpoint/test
sudo chown me mountpoint/test
```

W katalogu tym - już jako zwykły użytkownik - utworzę plik "date.txt" z aktualną datą.
```text
date > mountpoint/date.txt
```

Wyświetlam zawartość pliku:
```text
cat mountpoint/date.txt
```

## Odmontowujemy zasób

Odmontujemy nasz teraz zasób.
```text
sudo umount mountpoint
```

# Example testing

Jako przykład zastosowania pokażę wykorzystanie tego rozwiązania w ramach funkcjonalnego testu.
Moim celem jest sprawdzenie zachowania własnego skryptu w sytuacji, kiedy na dysku zabraknie miejsca.
Użyję tego pliku jako dysku, na którym umieszczę plik bazy danych sqlite3.
Następnie w interpreterze Python wykonam pętlę, która do tej bazy danych będzie dodawać kolejne rekordy,

## Demo

Montuję przygotowany zasób:
```text
sudo mount mydisk mountpoint
```

Następnie tworzę katalog "db" z uprawnieniami dla dowolnego użytkownika:
```text
sudo mkdir -m 777 mountpoint/db
```

W kolejnym kroku tworzę bazę danych sqlite z jedną tabelą i jedną kolumną typu tekstowego.
```text
sqlite3 mountpoint/db/test.db
```

```sql
CREATE TABLE test(content TEXT);
```

Uruchamiam teraz interpreter Python, importuję moduł sqlite3, tworzę obiekt połączenia do bazy danych
i uruchamiam pętlę dodającą rekordy. Zawartością rekordu niech będzie text o rozmiarze 2kb.

```python
import sqlite3
conn = sqlite3.connect("mountpoint/db/test.db")
while 1: conn.execute("INSERT INTO test(content) VALUES(?)", ("a" * 2048, ))
```

W pewnym momencie oczywiście na dysku zabraknie miejsca, a w skrypcie wystąpi wyjątek sqlite3.OperationalError. Zatem w prawdziwym programie moglibyśmy go przechwycić i odpowiednio zareagować.
