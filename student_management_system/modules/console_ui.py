from rich.console import Console
from rich.table import Table

console = Console()

def print_menu():
    console.print("\n[bold cyan]===== Student Management System =====[/bold cyan]")
    console.print("[green]1.[/green] Add Student")
    console.print("[green]2.[/green] View Students")
    console.print("[green]3.[/green] Search Student")
    console.print("[green]4.[/green] Update Student")
    console.print("[green]5.[/green] Delete Student")
    console.print("[green]6.[/green] Export Students to CSV")
    console.print("[green]7.[/green] Import Students from CSV")
    console.print("[green]8.[/green] Exit")
    console.print("[cyan]===================================[/cyan]")

def print_students_table(students):
    table = Table(title="All Student Records")
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Name", style="magenta")
    table.add_column("Course", style="green")
    table.add_column("Marks", style="yellow", justify="center")
    for s in students:
        table.add_row(s['id'], s['name'], s['course'], str(s['marks']))
    console.print(table)

def print_message(msg, style="white"):
    console.print(f"[{style}]{msg}[/{style}]")