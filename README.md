# Soioe

A freshman's Python learning record — from basics to building a web scraper.

During the past semester of the 2025–2026 academic year, I haven't had many chances to practice coding, so I've decided to start right now.

## Learning Progress

| # | Topic | Contents |
|---|-------|----------|
| 01 | Basics | variables, types, print, f-strings |
| 02 | Control Flow | if/elif/else, while, for, range |
| 03 | Data Structures | list, tuple, dict, set |
| 04 | Functions | def, return, default params |
| 05 | Strings | strip, split, replace, join |
| 06 | Modules | import, math, random |
| 07 | File I/O | read, write, with |
| 08 | Project | a to-do list app |
| 09 | OOP Basics | class, `__init__`, `self`, methods |
| 10 | OOP Advanced | inheritance, override, `__str__` |
| 11 | OOP Project | to-do list rebuilt with classes |
| 12 | Exceptions | try/except/else/finally, raise, custom |
| 13 | Comprehensions | list / dict / set / generator |
| 14 | Iterators & Generators | `iter`/`next`, `yield` |
| 15 | Decorators | closures, `@decorator` |
| 16 | Context Managers | `with`, `__enter__`/`__exit__` |
| 17 | Type Hints | `typing`, annotations |
| 18 | Project | a novel scraper (requests + BeautifulSoup) |

## Projects

- [08-project](08-project/) — a to-do list (functions + file I/O)
- [11-oop-project](11-oop-project/) — the same idea, rebuilt with `Task` and `TodoList` classes
- [18-novel-scraper](18-novel-scraper/) — a novel scraper (requests + BeautifulSoup)
  - `alicesw_scraper.py` — v1: the first working version
  - `alicesw_scraper2.py` — v2: rewritten with the lessons learned (see below)

### Scraper v2 improvements

- Every chapter is appended to disk as it is downloaded, so an interrupted run keeps what it got; existing files are skipped on re-run
- A `visited` set guards against "next chapter" links that loop back
- All requests go through one `fetch()` helper with `raise_for_status()` — plus detection of the site's anti-scraping "提示信息" page, which returns HTTP 200
- A shared `requests.Session()` reuses connections and sets headers once
- A reusable `@retry` decorator (from lesson 15) replaces the inline retry loop
- Type hints on every function (lesson 17)

## How to Run

```bash
# 待办清单
python 11-oop-project/todo_oop.py

# 小说爬虫 v2(需先安装依赖;先设 LIMIT 控制下多少本)
python 18-novel-scraper/alicesw_scraper2.py
```

The scraper caches the novel list in `novels.json` so re-runs skip the listing pages.
