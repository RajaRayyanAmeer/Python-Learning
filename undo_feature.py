action_history_stack = []

def record_action(user_action):
    print("Performing action:", user_action)
    action_history_stack.append(user_action)

def undo_last_action():
    if action_history_stack:
        last_performed_action = action_history_stack.pop()
        print("Undoing action:", last_performed_action)
    else:
        print("Nothing to undo!")

record_action("Typed 'Hello'")
record_action("Bolded 'Raja'")
record_action("Deleted 'Rayyan'")

print("\nUndoing the recent actions...\n")
undo_last_action()
undo_last_action()
undo_last_action()
undo_last_action()