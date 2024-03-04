import time
import os

def pomodoro_timer(pomodoro_duration, break_duration, num_cycles):
    total_pomodoro_minutes = 0
    total_break_minutes = 0
    for cycle in range(num_cycles):
        # Pomodoro cycle
        print("Pomodoro Cycle ", cycle + 1)
        countdown(pomodoro_duration)
        print("Time's up for Pomodoro!")
        
        total_pomodoro_minutes += pomodoro_duration // 60

        # Short break
        print("Take a short break!")
        countdown(break_duration)
        print("Back to work!")
        
        total_break_minutes += break_duration // 60

    # End message
    print("Goodbye! All Pomodoro cycles are complete.")
    print(f"Total Pomodoro minutes: {total_pomodoro_minutes} minutes")
    print(f"Total Break minutes: {total_break_minutes} minutes")
    print(f"Total Work minutes: {total_pomodoro_minutes + total_break_minutes} minutes")

def countdown(duration):
    for remaining in range(duration, 0, -1):
        minutes, seconds = divmod(remaining, 60)
        timeformat = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timeformat, end='\r')
        time.sleep(1)
    os.system('clear')  # for Windows use 'cls' instead of 'clear'

if __name__ == "__main__":
    while True:
        try:
            pomodoro_duration = int(input("Enter the duration of the Pomodoro (in minutes): "))
            break_duration = int(input("Enter the duration of the short break (in minutes): "))
            num_cycles = int(input("Enter the number of Pomodoro cycles: "))

            # Convert minutes to seconds
            pomodoro_duration *= 60
            break_duration *= 60

            # Check if inputs are valid
            if pomodoro_duration <= 0 or break_duration <= 0 or num_cycles <= 0:
                print("Invalid input. All values must be greater than 0.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer value.")
            continue
        else:
            # Inputs are valid, break out of the loop
            break

    pomodoro_timer(pomodoro_duration, break_duration, num_cycles)