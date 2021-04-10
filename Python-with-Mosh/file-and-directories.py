from pathlib import Path

path = Path("ecommerce")
print(path.exists())

path = Path("ecommer")
print(path.exists())


path = Path("email")
print(path.mkdir())

path = Path("email")
print(path.rmdir())

# To find directory or filesystem
path = Path()
for file in (path.glob("*.py")):
    print(file)