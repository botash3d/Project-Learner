from app.core.database import SessionLocal
from app.models.curriculum import Curriculum , Node
from app.models.edge import Edge
from app.models.progress import User

def seed():
    db =SessionLocal()

    default_user = db.quert(User).filter(User.id==1).first()
    if not default_user:
        default_user = User(id=1)
        db.add(default_user)
        db.flush()

    try:
        python_curriculum = Curriculum(
            name="Python Path",
            description="A structured path from Python basics to advanced topics."
        )
        db.add(python_curriculum)
        db.flush()

        topics = [
            "Variables & Data Types",
            "Control Flow (if/else, loops)",
            "Functions",
            "Data Structures (lists, dicts, sets, tuples)",
            "File Handling",
            "Error Handling (try/except)",
            "Object-Oriented Programming",
            "Modules & Packages",
            "Comprehensions",
            "Decorators",
            "Generators & Iterators",
            "Working with APIs (requests)",
            "Virtual Environments & pip",
            "Testing (pytest)",
            "Async Python (asyncio)",
        ]
        nodes = {}
        for title in topics:
            node = Node(curriculum_id=python_curriculum.id,title=title)
            db.add(node)
            db.flush()
            nodes[title] = node

        prerequisites = [
            ("Variables & Data Types", "Control Flow (if/else, loops)"),
            ("Control Flow (if/else, loops)", "Functions"),
            ("Variables & Data Types", "Data Structures (lists, dicts, sets, tuples)"),
            ("Functions", "Error Handling (try/except)"),
            ("Data Structures (lists, dicts, sets, tuples)", "File Handling"),
            ("Functions", "Object-Oriented Programming"),
            ("Object-Oriented Programming", "Modules & Packages"),
            ("Data Structures (lists, dicts, sets, tuples)", "Comprehensions"),
            ("Functions", "Decorators"),
            ("Comprehensions", "Generators & Iterators"),
            ("Modules & Packages", "Working with APIs (requests)"),
            ("Modules & Packages", "Virtual Environments & pip"),
            ("Error Handling (try/except)", "Testing (pytest)"),
            ("Generators & Iterators", "Async Python (asyncio)"),
        ]

        for source_title, target_title in prerequisites:
            edge = Edge(
                source_node_id=nodes[source_title].id,
                target_node_id=nodes[target_title].id
            )
            db.add(edge)

        db.commit()
        print(f"Seeded '{python_curriculum.name}' with {len(topics)} nodes and {len(prerequisites)} edges.")

    except Exception as e:
        db.rollback()
        print(f"Seeding failed: {e}")
        raise
    finally:
        db.close()

if __name__=="__main__":
    seed()