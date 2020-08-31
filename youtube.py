import webbrowser

url = input("Enter the YouTube URL : ")

url = url[:12]+'ss'+url[12:]

webbrowser.open(url)