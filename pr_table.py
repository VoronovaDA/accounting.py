from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Genre", "Performers", "Song"]
x.add_row(["Folk music", "Bob Dylan", "Not Dark Yet"])
x.add_rows([["Country", "Beirut", "Brandenburg"], ["Johnny Cash", "Rhineland", "Rhineland"]])
x.add_column("Duration", ["00:05:46", "00:06:27", "00:03:38"])

print(x)
