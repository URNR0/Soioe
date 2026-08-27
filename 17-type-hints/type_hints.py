def add(a: int, b: int) -> int:
    return a + b 

print(add(1, 3))

numbers: list[int] = [1, 3, 5, 7, 9]
keys: dict[str, int] = {"a": 1, "b": 2}
pair: tuple[int, str] = (1, "a")

def average(scores: list[int]) -> float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def find(name: str) -> int | None:
    names = ["Alice", "Bob", "Charlie", "David"]
    if name in names:
        return names.index(name)
    return None

print(average([90, 80, 70]))      
print(average([100, 100, 100]))   
print(average([]))                

print(find("Alice"))   
print(find("Bob"))     
print(find("Tom"))     

print(add("a", "b"))