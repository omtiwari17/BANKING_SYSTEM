# BANKING SYSTEM

A simple desktop banking application built with Python and Tkinter. It simulates core banking operations like creating accounts, deposits, withdrawals, viewing details, and closing accounts. The project is structured around multiple GUI modules, each handling one part of the workflow.

## Features

* **Login and Progress Screen** – Entry point with authentication and a splash/progress bar.
* **Dashboard** – Main navigation window linking all other features.
* **Add Account** – Create a new customer record with details and optional photo.
* **Deposit** – Add money to an existing account.
* **Withdrawal** – Withdraw money, with balance updates.
* **View Account** – Search and display account details.
* **Close Account** – Deactivate or remove an existing account.

## Project Structure

```
BANKING_SYSTEM/
├─ AddAccount.py        # GUI for creating accounts
├─ CloseAccount.py      # Handles closing/deactivating accounts
├─ DashBoard.py         # Main navigation window
├─ Login.py             # Login interface
├─ ProgressBar.py       # Startup splash / progress bar
├─ ViewAccount.py       # Account search and detail view
├─ deposit.py           # Deposit workflow
├─ withdrawal.py        # Withdrawal workflow
├─ Image/               # GUI icons, logos, static images
└─ dbphoto/             # Stored customer photos
```

## How it works

* The app starts with the **Login** screen, followed by a **ProgressBar** splash.
* After logging in, users land on the **Dashboard**, where they can choose actions.
* Each feature (Add Account, Deposit, Withdrawal, View Account, Close Account) is a separate Tkinter module, called from the dashboard.
* Customer photos are saved in the `dbphoto/` folder, while UI assets live in `Image/`.

## Purpose

This is an educational/demo project showing how a desktop GUI app can tie together different banking workflows. It can be used as a reference for learning Tkinter, handling multiple windows, and organizing a Python project into modular scripts.

## Author

Developed by [@omtiwari17](https://github.com/omtiwari17).
