import wikipedia

user_choice = input("Enter a page title or phrase to search: ")

while user_choice != "":
    try:
        page_selected = wikipedia.page(user_choice)
        print(f"Title: {page_selected.title}")
        print(f"Url: {page_selected.url}")
        print(f"Summary: {page_selected.summary}")
        user_choice = input("Enter a page title or phrase to search: ")
    except wikipedia.DisambiguationError as e:
        print(e.options)
        user_choice = input("Enter a page title or phrase to search: ")

