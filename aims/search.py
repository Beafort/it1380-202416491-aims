def search_by_title(keyword, cart):
  return [dvd for dvd in cart.items if keyword.lower() in dvd.title.lower()]
