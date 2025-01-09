# 🛠️ Fix the Circular Import

Now that we've seen the circular import error, let's fix it! We'll learn how to reorganize our code to avoid the circular dependency.

## 📝 Instructions

1. Create a new file called `utils.py` for shared code
2. Move the validation logic to `utils.py`
3. Update `app.py` and `validator.py` to use the shared code
4. Test that everything works now!

## 💡 Hint

Sometimes the best way to fix a circular import is to create a new module that both files can import from. Think about what code could be shared!

## ✅ Expected Output

When you run `app.py`:
```python
7  # Result of 4 + 3
12  # Result of 4 * 3