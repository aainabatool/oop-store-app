
###  `README.md`

```markdown
# Python OOP Store App

This project is a Python-based store inventory system that demonstrates core **Object-Oriented Programming (OOP)** principles, including:

- **Encapsulation**
- **Inheritance**
- **Polymorphism**
- **Abstraction**

It also supports reading item data from a CSV file.

---

## 📁 Project Structure

```

store/
├── main.py          # Main script to test the classes
├── item.py          # Base Item class
├── phone.py         # Phone subclass (inherits from Item)
├── keyboard.py      # Keyboard subclass (inherits from Item)
├── items.csv        # CSV file containing item data
├── .gitignore       # Git ignore file
└── README.md        # Project documentation

````

---

##  Features

- `Item` class with:
  - Encapsulated attributes (`__name`, `__price`)
  - Getters & setters for controlled access
  - Methods to apply discount and price increment
  - Class method to instantiate items from a CSV

- `Phone` and `Keyboard` subclasses demonstrate **inheritance** and **polymorphism**.

- Private methods for email-related functionality (abstraction, not exposed to the user).

---

## 🔧 How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/store-app.git
   cd store-app
````

2. Make sure `items.csv` exists in the same directory and contains:

   ```csv
   name,price,quantity
   Phone,1000,3
   Keyboard,500,5
   ```

3. Run the main script:

   ```bash
   python main.py
   ```

---

##  Technologies Used

* Python 3.13+
* CSV module (standard library)

---

