from tkinter import *
import psycopg2

class WorkoutTool:
    def __init__(self, root):
        self.root = root
        self.root.title('Workout Tool')
        self.root.configure(bg='black')
        self.create_workout_frame()

    def create_workout_frame(self):
        self.workout_frame = LabelFrame(self.root, text='Workout Tracker', bg='black', fg='white', padx=10, pady=10)
        self.workout_frame.pack(padx=10, pady=10)

        Label(self.workout_frame, text='Enter workout type', font='arial 10 bold', bg='black', fg='#228B22').grid(row=1, column=0)
        self.workout_entry = Entry(self.workout_frame, width=50, bg='#228B22', fg='yellow', borderwidth=10, font='arial 10 bold')
        self.workout_entry.grid(row=1, column=1)

        Label(self.workout_frame, text='Duration (minutes)', font='arial 10 bold', bg='black', fg='#228B22').grid(row=3, column=0)
        self.duration_entry = Entry(self.workout_frame, width=50, bg='#228B22', fg='yellow', borderwidth=10, font='arial 10 bold')
        self.duration_entry.grid(row=3, column=1)

        Button(self.workout_frame, text='Log Workout', command=self.log_workout, bg='#228B22', fg='white', font='arial 10 bold').grid(row=5, column=1)

    def log_workout(self):
        workout_type = self.workout_entry.get()
        duration = self.duration_entry.get()
        # Add logic to log workout to database
        print(f'Logging workout: {workout_type} for {duration} minutes')

if __name__ == '__main__':
    root = Tk()
    app = WorkoutTool(root)
    root.mainloop()