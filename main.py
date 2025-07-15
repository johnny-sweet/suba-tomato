import typer
from typing_extensions import Annotated
from rich.progress import track
from rich.prompt import Confirm, Prompt
from rich import print
import time
import winsound
import sys

pomo_count = 0

def notify():
    if sys.platform.startswith("win"):
        import winsound
        winsound.MessageBeep()
    else:
        print("\a", end="", flush=True)

def main(working_time: Annotated[int, typer.Argument()], break_time: Annotated[int, typer.Argument()]):
    global pomo_count

    print(f"Working time is {working_time} minutes.")
    print(f"Break time is {break_time} minutes.")

    for _ in track(range(working_time * 2), description="[bold yellow]working period[/bold yellow]..."):
        time.sleep(30)

    notify()
    
    print("Time for a break!")
    Prompt.ask("Press enter to start the break timer")
    for _ in track(range(break_time * 2), description="[bold green]break period[/bold green]..."):
        time.sleep(30)
    
    notify()    
    print("Break is over! You can restart the timer if you want.")
    restart = Confirm.ask("Do you want to restart the timer?")
    pomo_count += 1
    if restart:
        main(working_time, break_time)
    else:
        print(f"You completed {pomo_count} pomodoro interval{"s" if pomo_count > 1 else ""}!")
      
if __name__ == "__main__":
    typer.run(main)