# Définir une liste pour stocker les tâches
tasks = []

# Fonction pour ajouter une tâche
def add_task(description):
    tasks.append(description)
    print("Tâche ajoutée avec succès.")

# Fonction pour afficher la liste des tâches
def show_tasks():
    print("\nListe des tâches à faire:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

# Fonction pour marquer une tâche comme terminée
def complete_task(index):
    if 1 <= index <= len(tasks):
        completed_task = tasks.pop(index - 1)
        print(f"Tâche terminée : {completed_task}")
    else:
        print("Numéro de tâche invalide.")

# Boucle principale
while True:
    print("\n1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Marquer une tâche comme terminée")
    print("4. Quitter")

    choice = input("Choisissez une option : ")

    if choice == "1":
        task_description = input("Entrez la description de la tâche : ")
        add_task(task_description)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        task_index = int(input("Entrez le numéro de la tâche à terminer : "))
        complete_task(task_index)
    elif choice == "4":
        print("Au revoir !")
        break
    else:
        print("Option invalide. Veuillez choisir à nouveau.")
