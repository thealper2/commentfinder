# commentfinder

Bir web sitesinin kaynak kodlarındaki yorum satırlarını bulmaya yarayan bir araçtır.

## Gereksinimler

commentfinder aşağıdaki kütüphaneleri kullanır.

* Colorama
* Requests
* BeautifulSoup4

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/commentfinder.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

| Parametre    | Kullanımı |
| ---------    | --------- |
| --verbose    | Verbose. Çıktı göstermek için kullanılır. |
| --out        | Çıktının kaydedileceği dosya. |
| --recursive  | URL içindeki tüm dosyalara uygula |
| --url        | Tarama yapılacak URL adresi |

```bash
usage: commentfinder.py [-h] --url URL --out OUT [--recursive] [--verbose]

options:
  -h, --help   show this help message and exit
  --url URL
  --out OUT
  --recursive
  --verbose
```

## Örnekler

```python
python3 commentfinder.py --url TARGET --recursive --out target.txt -v
python3 commentfinder.py --url TARGET --out target.txt
```
