import typer
from typing_extensions import Annotated
from rich.progress import Progress, BarColumn, TextColumn
from rich.prompt import Confirm, Prompt
from rich import print
import time
import sys

pomo_count = 0

def notify():
    if sys.platform.startswith("win"):
        import winsound
        winsound.MessageBeep()
    else:
        print("\a", end="", flush=True)
        
        
def format_time_left(seconds_left):
    mins, secs = divmod(seconds_left, 60)
    return f"{mins:02}:{secs:02}"


def run_timer(total_intervals, description):
    total_seconds = total_intervals * 30
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
        TextColumn("Time left: {task.fields[time_left]}")
    ) as progress:
        task = progress.add_task(description, total=total_intervals, time_left=format_time_left(total_seconds))
        for i in range(total_intervals):
            time.sleep(30)
            seconds_left = (total_intervals - i - 1) * 30
            progress.update(task, advance=1, time_left=format_time_left(seconds_left))
            

def main(working_time: Annotated[int, typer.Argument()], break_time: Annotated[int, typer.Argument()]):
    global pomo_count

    print(f"Working time is {working_time} minutes.")
    print(f"Break time is {break_time} minutes.")

    run_timer(working_time * 2, "[bold yellow]working period[/bold yellow]...")
    notify()
    
    print("Time for a break!")
    Prompt.ask("Press enter to start the break timer")
    run_timer(break_time * 2, "[bold green]break period[/bold green]...")
    
    notify()    
    print("Break is over! You can restart the timer if you want.")
    restart = Confirm.ask("Do you want to restart the timer?")
    pomo_count += 1
    if restart:
        main(working_time, break_time)
    else:
        print(f"You completed {pomo_count} pomodoro interval{"s" if pomo_count > 1 else ""}!")
      
def app():
    typer.run(main)

if __name__ == "__main__":
    app() 