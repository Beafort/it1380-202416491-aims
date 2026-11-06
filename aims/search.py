def search_by_title(title, cart):
  for item in cart.items:
      if(item.title == title):
        return item