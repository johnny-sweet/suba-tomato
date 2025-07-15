# Suba-Tomato: *Su*per *Ba*sic Pomodoro Timer

Suba-Tomato is a minimal, distraction-free Pomodoro timer for your terminal. It does one thing: timing work and break intervals - no stats, no clutter.

## How to Use
After installation, simply run:

```
tomato 25 5
```

This starts a 25-minute work timer, followed by a 5-minute break. Adjust the numbers as you like.
You have to accept the break timer to begin by hitting ENTER (as it turned out to be more flexible this way).
At the end of the break you will be asked to restart a new interval with the same settings. 

## Install Instructions
Make sure you have pip installed: https://pip.pypa.io/en/stable/installation/
1. Clone this repository
2. Change into the project directory in your terminal:
   ```
   cd suba-tomato
   ```
3. Install locally with pip:
   ```
   pip install .
   ```

You can now use `tomato` from any terminal window.
