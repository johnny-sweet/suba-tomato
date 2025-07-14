import typer
from typing_extensions import Annotated
from rich.progress import track
import time


def main(working_time: Annotated[int, typer.Argument()], break_time: Annotated[int, typer.Argument()]):
    print(f"Working time is {working_time} minutes.")
    print(f"Break time is {break_time} minutes.")
    for _ in track(range(working_time * 2), description="working period..."):
        time.sleep(30)
    
    # TODO system notification
    
    print("Time for a break!")
    for _ in track(range(break_time * 2), description="break period..."):
        time.sleep(30)
        
    print("Break is over! You can restart the timer if you want.")
    restart = typer.confirm("Do you want to restart the timer?")
    if restart:
        main(working_time, break_time)
    else:
        print("Goodbye!")

if __name__ == "__main__":
    typer.run(main)