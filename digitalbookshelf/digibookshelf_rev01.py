def add_book(books, title, status):
    # 新しい本をブックシェルフに追加します。
        books.append({"title": title, "status": status})
 

def edit_book(books, old_title, new_title):
    # 指定された本のタイトルを編集します。
    for book in books:
        if book["title"] == old_title:
            book["title"] = new_title
            return True
    return False

def edit_status(books, title, status):
    # 指定された本のステータスを編集します。
    for book in books:
        if book["title"] == title:
            book["status"] = status
            return True
    return False

def search_book(books, keyword):
    #指定されたキーワードで本を検索します。
    found_books = []
    for book in books:
        if keyword.lower() in book["title"].lower():
            found_books.append(book)
    return found_books

def delete_book(books, title):
    #指定されたタイトルの本を削除します。
    for book in books:
        if book["title"] == title:
            books.remove(book)
            return True
    return False

def display_statistics(books):
    #ブックシェルフの統計情報を表示します。
    total_books = len(books)
    read_books = sum(1 for book in books if book["status"] == "read")
    unread_books = total_books - read_books
    print(f"Total books: {total_books}")
    print(f"Read books: {read_books}")
    print(f"Unread books: {unread_books}")


def display_menu():
    #ブックシェルフの操作メニューを表示します。
    print("================================================")    
    print("Welcome to your personal books digital library!")
    print("================================================")    
    print("1: Add a Book")
    print("2: Edit a Book")
    print("3: Search for Book")
    print("4: Delete a Book")
    print("5: View Library Stats")
    print("6: Exit app")


def display_statemenu():
    #ブック未読・既読ステータス選択メニューを表示します。
    print("Enter book status 1: read or 2: unread ")
    print("1: read")
    print("2: unread")
    print("9: back to menu")

def main():
    books = []
    slashs = "///////////////////"
    while True: #メニューごとの入力処理
        display_menu()
        choice = input("Please select from 1 to 6 \n")
        #メニュー１Add book の入力と表示
        if choice == "1": 
            title = input("Enter book title: ")
            if title.strip():  # 空のタイトルが入力された場合には本を追加しない
                while True:
                    display_statemenu()
                    status = input()
                    if status == "1" :
                        add_book(books, title, "read")
                        print(slashs)
                        print("registerd")                   
                        print(slashs)
                        print("\n")
                        break
                    elif status =="2":
                        add_book(books, title, "unread")
                        print(slashs)
                        print("registerd")                   
                        print(slashs)
                        print("\n")
                        break
                    elif status == "9":
                        print("\n")
                        break
                    else:
                        print("Please input 1 or 2\n")
            else:
                print("Invalid input \n")

        #メニュー2　登録済みbook情報編集 の入力と表示
        elif choice == "2":
            old_title = input("Enter old book title: ")
            new_title = input("Enter new book title: ")
            if new_title.strip():  # 空のタイトルが入力された場合には本を追加しない
                if edit_book(books, old_title, new_title):
                    while True:
                        display_statemenu()
                        status = input()
                        if status == "1" :
                            edit_status(books, title, "read")
                            print(slashs)
                            print("registerd")                   
                            print(slashs)
                            print("\n")
                            break
                        elif status =="2":
                            edit_status(books, title, "unread")
                            print(slashs)
                            print("registerd")                   
                            print(slashs)
                            print("\n")
                            break
                        elif status == "9":
                            print("\n")
                            break
                        else:
                            print("Please input 1 or 2\n")
                    print(slashs)
                    print("Book edited successfully.")
                    print(slashs)
                    print("\n")
                else:
                    print(slashs)
                    print("Book not found.")
                    print(slashs)
                    print("\n")
            else:
                print("Invalid input \n")
        #メニュー3　登録済みbookの検索 の入力と表示
        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            found_books = search_book(books, keyword)
            if found_books:
                print("Matching books:")
                for book in found_books:
                    print(f"{book['title']: <20} - {book['status']}")
                print("\n")
            else:
                print(slashs)
                print("No matching books found.")
                print(slashs)
                print("\n")
        #メニュー4　登録済みbook削除の入力と表示
        elif choice == "4":
            title = input("Enter book title to delete: ")
            if delete_book(books, title):
                print("Book deleted successfully.")
            else:
                print("Book not found.")
        #メニュー5　登録内容統計量の表示
        elif choice == "5":
            display_statistics(books)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please input a number between 1 and 6.")

if __name__ == "__main__":
    main()