# 🌟 Best Practices for Module Organization

Let's learn how to organize our code to prevent circular imports before they happen!

## 📝 Instructions

1. Look at the current exercise file structure:
   ```
   03.3-best-practices/
   ├── app.py      # Entry file
   ├── models.py      # Data structures
   ├── utils.py       # Shared utilities
   ├── students.py    # Student operations
   └── courses.py     # Course operations
   ```

3. Complete the code in each file following these rules:
   - Keep shared code in `utils.py`
   - Define data structures in `models.py`
   - Use those structures in other modules

## 💡 Hint

When organizing modules, think about dependencies:
- What code needs to be shared?
- Which modules should import from which?
- Where should each piece of functionality live?

## ✅ Expected Output

When you run `students.py`:
```python
Student: Alice (ID: 1) enrolled in Course: Python 101 (Code: PY101)
```
