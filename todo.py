# Simple To-Do List App

tasks = []

def show_menu():
    print("\n--- قائمة المهام ---")
    print("1. عرض المهام")
    print("2. إضافة مهمة")
    print("3. حذف مهمة")
    print("4. خروج")
  print("5. خروج")
while True:
    show_menu()
    choice = input("اختر رقم العملية: ")

    if choice == '1':
        print("\nمهامك الحالية:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    elif choice == '2':
        new_task = input("اكتب المهمة الجديدة: ")
        tasks.append(new_task)
        print("تمت الإضافة بنجاح!")
    elif choice == '3':
        task_num = int(input("أدخل رقم المهمة المراد حذفها: "))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("تم الحذف!")
        else:
            print("رقم غير صالح.")
    elif choice == '4':
        print("مع السلامة!")
         if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("تم الحذف!")
        else:
            print("رقم غير صالح.")
    elif choice == '5':
        print("مع السلامة!")
        break
    else:

        

        print("اختيار خاطئ، حاول مرة أخرى.")
