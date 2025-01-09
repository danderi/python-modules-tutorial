# 🔍 Spot the Circular Import

Oh no! We have two Python files that are trying to use each other's functions. Let's see what happens when we try to run them!

## 📝 Instructions

1. Look at the two files: `app.py` and `validator.py`
2. Try to understand why they cause a circular import
3. Run the code and see what error you get
4. Take notes on what the error message tells you

## 💡 Hint

When you see this error:
```
ImportError: cannot import name '...' from partially initialized module '...' (most likely due to a circular import)
```
It means your modules are trying to import each other!

## ✅ Expected Output

You should see an import error when you try to run `app.py`. This is normal - we'll fix it in the next exercise! 🛠️