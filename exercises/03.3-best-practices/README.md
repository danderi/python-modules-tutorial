# 🌟 Best Practices for Module Organization

Let's learn how to organize our code to prevent circular imports before they happen!

## 📝 Instructions

1. Look at the current exercise file structure:
   ```
   03.3-best-practices/
   ├── school_system/
   │   ├── models.py      # Data structures
   │   ├── utils.py       # Shared utilities
   │   ├── students.py    # Student operations
   │   └── courses.py     # Course operations
   └── app.py            # Main entry point
   ```

2. Study how the modules are organized:
   - `models.py` contains data structures used by everyone
   - `utils.py` has shared functions
   - `students.py` and `courses.py` have specific operations
   - No circular dependencies between modules!

3. Try to create a new student and enroll them in a course using `app.py`

## 💡 Hint

When organizing modules, think about these questions:
- What code needs to be shared between modules?
- Which modules should depend on which others?
- Where should each piece of functionality live?

## ✅ Expected Output

When you run `app.py`, you should see:
```python
Student: Alice (ID: 1) enrolled in Course: Python 101 (Code: PY101)
```

## 🎯 Key Takeaways

1. Keep data structures in a separate module
2. Put shared utilities in their own module
3. Organize related functionality together
4. Think about dependencies before writing code