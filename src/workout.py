from tkinter import *

class WorkoutTool:
    def __init__(self, root):
        self.root = root
        self.root.title('Workout Tool')
        self.create_workout_frame()

    def create_workout_frame(self):
        self.workout_frame = LabelFrame(self.root, text='Workout', bg='black', fg='white', padx=10, pady=10)
        self.workout_frame.pack(padx=10, pady=10)
        # Add workout components here

if __name__ == '__main__':
    root = Tk()
    app = WorkoutTool(root)
    root.mainloop()