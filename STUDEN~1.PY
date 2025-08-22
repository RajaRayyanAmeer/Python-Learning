"""
STUDENT ADMISSION RANKING SYSTEM
A Binary Search Tree (BST) based application to manage and rank student admissions by their scores.
"""


class StudentNode:
    """Represents a single student in our ranking system"""

    def __init__(self, name, app_id, score):
        self.name = name  # Student's full name
        self.app_id = app_id  # Unique application ID
        self.score = score  # Admission score (0-100)
        self.left = None  # Reference to student with lower score
        self.right = None  # Reference to student with higher score


class StudentBST:
    """Manages the student records using a Binary Search Tree structure"""

    def __init__(self):
        self.root = None

    def insert(self, name, app_id, score):
        """Adds a new student to the ranking system"""
        new_student = StudentNode(name, app_id, score)
        if self.root is None:
            self.root = new_student
            return True
        return self._insert_helper(self.root, new_student)

    def _insert_helper(self, current, new_student):
        """Helper function to find the right spot for a new student"""
        if new_student.score < current.score:
            if current.left is None:
                current.left = new_student
                return True
            return self._insert_helper(current.left, new_student)
        elif new_student.score > current.score:
            if current.right is None:
                current.right = new_student
                return True
            return self._insert_helper(current.right, new_student)
        else:
            print(f"\n⚠️ A student with score {new_student.score} already exists!")
            return False

    def in_order_traversal(self):
        """Displays all students sorted by their scores (low to high)"""
        if self.root is None:
            print("\nNo students in the system yet. Please add some students first.")
            return
        print("\n📋 Student List (Sorted by Score):")
        print("-" * 50)
        self._in_order_helper(self.root)
        print("-" * 50)

    def _in_order_helper(self, node):
        """Recursive helper to print students in order"""
        if node:
            self._in_order_helper(node.left)
            print(f"🎓 {node.name} (ID: {node.app_id}) - Score: {node.score}")
            self._in_order_helper(node.right)

    def search(self, score):
        """Finds a student by their exact score"""
        return self._search_helper(self.root, score)

    def _search_helper(self, node, score):
        """Recursive helper for student search"""
        if node is None:
            return None
        if node.score == score:
            return node
        return self._search_helper(node.left if score < node.score else node.right, score)

    def print_range(self, x, y):
        """Displays students within a specific score range"""
        if self.root is None:
            print("\nNo students in the system yet. Please add some students first.")
            return
        print(f"\n🔍 Students with scores between {x} and {y}:")
        print("-" * 50)
        self._range_helper(self.root, x, y)
        print("-" * 50)

    def _range_helper(self, node, x, y):
        """Recursive helper for range queries"""
        if node:
            if x < node.score:
                self._range_helper(node.left, x, y)
            if x <= node.score <= y:
                print(f"🎓 {node.name} (ID: {node.app_id}) - Score: {node.score}")
            if y > node.score:
                self._range_helper(node.right, x, y)

    def get_rank(self, score):
        """Calculates how many students have lower scores than given score"""
        if self.root is None:
            print("\nNo students in the system yet. Please add some students first.")
            return -1
        rank = self._count_below(self.root, score)
        return rank

    def _count_below(self, node, score):
        """Recursive helper for rank calculation"""
        if node is None:
            return 0
        if node.score < score:
            return 1 + self._count_below(node.left, score) + self._count_below(node.right, score)
        return self._count_below(node.left, score)


def get_valid_input(prompt, input_type=int, min_val=0, max_val=100):
    """Safely gets and validates user input with helpful error messages"""
    while True:
        try:
            value = input_type(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}")
                continue
            return value
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}")


def main():
    """Main program loop with user-friendly interface"""
    bst = StudentBST()

    # Preload sample data (15 students)
    sample_students = [
        ("Raja Rayyan Ameer", "23-CP-25", 75),
        ("Muhammad Yahya Khan", "23-CP-15", 77),
        ("Tehman Hassan", "23-CP-11", 78),
        ("Malik Shahzaib", "23-SE-57", 88),
        ("Ali Adeem", "23-SE-08", 95),
        ("Muhammad Hassnain", "23-CS-87", 82),
        ("Rayyan Ahmad", "23-CS-89", 90),
        ("Muhammad Ahmad", "23-CP-07", 79),
        ("Rana Ali", "23-CS-54", 87),
        ("Mujawaad Khan", "23-CP-01", 83),
        ("Awais Ali", "23-SE-02", 91),
        ("Umama Hanif", "23-CP-19", 84),
        ("Ahmad Basil", "23-CP-99", 89),
        ("Badar Ali", "23-WD-01", 81),
        ("Abdullah Illyas", "23-AI-01", 86)
    ]

    # Uncomment to preload sample data
    # for student in sample_students:
    #     bst.insert(*student)

    print("\n" + "=" * 50)
    print("🏫 Welcome to Student Admission Ranking System")
    print("=" * 50)

    while True:
        print("\nMain Menu:")
        print("1.  Add New Student")
        print("2.  Find Student by Score")
        print("3.  View All Students (Sorted)")
        print("4.  View Students in Score Range")
        print("5.  Check Student Rank")
        print("6.  Exit System")
        print("-" * 30)

        choice = get_valid_input("Please choose an option (1-6): ", min_val=1, max_val=6)

        if choice == 1:
            print("\n➕ Add New Student")
            print("-" * 30)
            name = input("Student Name: ").strip()
            while not name:
                print("Name cannot be empty!")
                name = input("Student Name: ").strip()

            app_id = input("Application ID: ").strip()
            while not app_id:
                print("ID cannot be empty!")
                app_id = input("Application ID: ").strip()

            score = get_valid_input("Admission Score (0-100): ")

            if bst.insert(name, app_id, score):
                print(f"\n Success! {name} has been added with score {score}")

        elif choice == 2:
            print("\n Find Student by Score")
            print("-" * 30)
            score = get_valid_input("Enter score to search: ")
            student = bst.search(score)
            if student:
                print(f"\n Found: {student.name} (ID: {student.app_id}) with score {student.score}")
            else:
                print("\n No student found with that score")

        elif choice == 3:
            bst.in_order_traversal()

        elif choice == 4:
            print("\n View Students in Score Range")
            print("-" * 30)
            print("Enter the score range to view:")
            x = get_valid_input("Minimum score: ")
            y = get_valid_input("Maximum score: ")
            if x > y:
                print("\n Error: Minimum must be ≤ maximum")
            else:
                bst.print_range(x, y)

        elif choice == 5:
            print("\n Check Student Rank")
            print("-" * 30)
            score = get_valid_input("Enter student's score to check rank: ")
            rank = bst.get_rank(score)
            if rank >= 0:
                print(f"\n Ranking: {rank} students scored below {score}")

        elif choice == 6:
            print("\n" + "=" * 50)
            print("Thank you for using the Student Admission Ranking System!")
            print("=" * 50)
            break


if __name__ == "__main__":
    main()