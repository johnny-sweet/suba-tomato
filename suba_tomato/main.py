import typer
from typing_extensions import Annotated
from rich.progress import Progress, BarColumn, TextColumn
from rich.prompt import Confirm, Prompt
from rich import print
import time
import sys
import os
from rich.panel import Panel
from rich.align import Align

pomo_count = 0

def notify(is_break: bool) -> None: 
    if sys.platform.startswith("win"):
        import winsound
        winsound.MessageBeep()
    elif sys.platform.startswith("darwin"):
        if is_break:
            os.system("say -v Kate 'Time for a break'")
        else:
            os.system("say -v Kate 'Break is over'")
    else: 
        print("\a", end="", flush=True)


def format_time_left(seconds_left: int) -> str:
    mins, secs = divmod(seconds_left, 60)
    return f"{mins:02}:{secs:02}"


def run_timer(total_intervals: int, description: str) -> None:
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

    if pomo_count == 0:
        info_panel = Panel(
            Align.center(
            f"[bold yellow]Working time:[/bold yellow] [cyan]{working_time}[/cyan] minutes\n"
            f"[bold green]Break time:[/bold green] [cyan]{break_time}[/cyan] minutes\n\n"
            f"[bold magenta]POMODORO INTERVAL {pomo_count + 1}[/bold magenta]"
            ),
            expand=False,
            border_style="magenta"
        )
        print(info_panel)
    else:
        print("\033c", end="")
        interval_text = f"[bold magenta]POMODORO INTERVAL {pomo_count + 1}[/bold magenta]"
        print(Panel(Align.center(interval_text), expand=False, border_style="magenta"))

    run_timer(working_time * 2, "[bold yellow]working period[/bold yellow]...")
    notify(is_break=True)
    
    print("Time for a break!")
    Prompt.ask("Press enter to start the break timer")
    run_timer(break_time * 2, "[bold green]break period[/bold green]...")
    
    notify(is_break=False)    
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